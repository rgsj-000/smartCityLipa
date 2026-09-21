#!/usr/bin/env python3
"""Regenerate machine-readable checks and the ACT05 evidence map.

The script uses only Python's standard library plus Matplotlib. It reads the
training GeoPackage directly, so the expected results remain traceable to the
same synthetic data opened in QGIS.
"""

from __future__ import annotations

import json
import sqlite3
import struct
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Polygon


ROOT = Path(__file__).resolve().parents[1]
GPKG = ROOT / "data" / "processed" / "lipa_training.gpkg"
OUTPUTS = ROOT / "outputs"
SCREENSHOTS = OUTPUTS / "screenshots"


def polygon_from_gpkg(blob: bytes) -> list[tuple[float, float]]:
    """Read the first ring from the package's simple Polygon geometry."""
    wkb = blob[8:]
    byte_order = "<" if wkb[0] == 1 else ">"
    geometry_type = struct.unpack(byte_order + "I", wkb[1:5])[0]
    if geometry_type != 3:
        raise ValueError(f"Expected Polygon WKB type 3, found {geometry_type}")
    ring_count = struct.unpack(byte_order + "I", wkb[5:9])[0]
    if ring_count < 1:
        raise ValueError("Polygon has no rings")
    point_count = struct.unpack(byte_order + "I", wkb[9:13])[0]
    offset = 13
    points = []
    for _ in range(point_count):
        points.append(struct.unpack(byte_order + "dd", wkb[offset : offset + 16]))
        offset += 16
    return points


def bounds(points: list[tuple[float, float]]) -> tuple[float, float, float, float]:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return min(xs), min(ys), max(xs), max(ys)


def intersects(left: tuple[float, float, float, float], right: tuple[float, float, float, float]) -> bool:
    return not (
        left[2] <= right[0]
        or left[0] >= right[2]
        or left[3] <= right[1]
        or left[1] >= right[3]
    )


with sqlite3.connect(GPKG) as connection:
    barangays = [
        {"code": code, "name": name, "points": polygon_from_gpkg(geom)}
        for code, name, geom in connection.execute(
            "SELECT BRGY_CODE, BRGY_NAME, geom FROM barangays ORDER BY BRGY_CODE"
        )
    ]
    hazards = [
        {
            "id": hazard_id,
            "hazard": hazard,
            "level": level,
            "source": source,
            "reference_date": reference_date,
            "points": polygon_from_gpkg(geom),
        }
        for hazard_id, hazard, level, source, reference_date, geom in connection.execute(
            "SELECT HAZ_ID, HAZARD, LEVEL, SOURCE, REF_DATE, geom "
            "FROM flood_hazard ORDER BY HAZ_ID"
        )
    ]

intersection_results: dict[str, list[str]] = {}
for barangay in barangays:
    barangay_bounds = bounds(barangay["points"])
    intersection_results[barangay["name"]] = [
        hazard["level"]
        for hazard in hazards
        if intersects(barangay_bounds, bounds(hazard["points"]))
    ]

expected = {
    "training_data_status": "synthetic_training_only",
    "accountability_statement": "AI assists. QGIS verifies. People decide.",
    "ACT02": {
        "boundary_tests": {
            "4999": "Low",
            "5000": "Medium",
            "10000": "Medium",
            "10001": "High",
            "null": "Unknown",
        },
        "verification_method": (
            "Use the QGIS expression preview, temporarily substitute each literal "
            "for POP_TOTAL, read the preview result, and do not save the literal tests."
        ),
    },
    "ACT05": {
        "method": "Polygon bounding-box intersection for the supplied rectangular synthetic layers",
        "barangay_hazard_intersections": intersection_results,
        "hazard_records": [
            {
                "HAZ_ID": hazard["id"],
                "HAZARD": hazard["hazard"],
                "LEVEL": hazard["level"],
                "SOURCE": hazard["source"],
                "REF_DATE": hazard["reference_date"],
            }
            for hazard in hazards
        ],
        "limitation": (
            "Intersection shows mapped exposure only. It does not establish damage, "
            "risk, urgency, travel time, or an operational priority."
        ),
    },
}

OUTPUTS.mkdir(parents=True, exist_ok=True)
SCREENSHOTS.mkdir(parents=True, exist_ok=True)
(OUTPUTS / "expected_results.json").write_text(
    json.dumps(expected, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

colors = {"High": "#D95F4C", "Moderate": "#F0B44D"}
fig, ax = plt.subplots(figsize=(15, 8.75), dpi=120)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#F3F7F8")

for barangay in barangays:
    patch = Polygon(
        barangay["points"],
        closed=True,
        facecolor="#F9FBFB",
        edgecolor="#173742",
        linewidth=1.8,
        zorder=1,
    )
    ax.add_patch(patch)

for hazard in reversed(hazards):
    patch = Polygon(
        hazard["points"],
        closed=True,
        facecolor=colors[hazard["level"]],
        edgecolor=colors[hazard["level"]],
        alpha=0.48,
        linewidth=2.2,
        zorder=2 if hazard["level"] == "Moderate" else 3,
    )
    ax.add_patch(patch)

for barangay in barangays:
    xmin, ymin, xmax, ymax = bounds(barangay["points"])
    levels = intersection_results[barangay["name"]]
    if not levels:
        evidence = "No mapped hazard\nintersection"
    elif levels == ["High", "Moderate"]:
        evidence = "High + Moderate\nintersections"
    else:
        evidence = f"{levels[0]} hazard\nintersection"
    ax.text(
        (xmin + xmax) / 2,
        (ymin + ymax) / 2,
        f"{barangay['name']}\n{evidence}",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        color="#0B2736",
        zorder=5,
        bbox={"boxstyle": "round,pad=0.28", "facecolor": "white", "alpha": 0.76, "edgecolor": "none"},
    )

ax.set_xlim(363800, 370200)
ax.set_ylim(1535800, 1540200)
ax.set_aspect("equal", adjustable="box")
ax.grid(color="#D8E3E7", linewidth=0.8, zorder=0)
ax.ticklabel_format(style="plain", useOffset=False)
ax.set_title(
    "Decision support map: verified flood hazard intersections",
    fontsize=23,
    fontweight="bold",
    color="#0B2736",
    pad=22,
)
ax.legend(
    handles=[
        Patch(facecolor=colors["High"], edgecolor=colors["High"], alpha=0.55, label="High flood hazard polygon"),
        Patch(facecolor=colors["Moderate"], edgecolor=colors["Moderate"], alpha=0.55, label="Moderate flood hazard polygon"),
        Patch(facecolor="#F9FBFB", edgecolor="#173742", label="Barangay boundary"),
    ],
    loc="lower left",
    frameon=True,
    framealpha=0.94,
    title="Directly mapped evidence",
    fontsize=10.5,
    title_fontsize=11,
)
ax.text(
    0.99,
    0.02,
    "SYNTHETIC TRAINING DATA | EPSG:32651\nIntersection is exposure evidence, not damage or priority.",
    transform=ax.transAxes,
    ha="right",
    va="bottom",
    fontsize=10.2,
    color="#5D7079",
)
ax.set_xlabel("Easting (m)", color="#5D7079")
ax.set_ylabel("Northing (m)", color="#5D7079")
plt.tight_layout()
fig.savefig(SCREENSHOTS / "ACT05_01_Decision_Support_Map.png", bbox_inches="tight")
plt.close(fig)
