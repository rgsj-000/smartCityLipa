#!/usr/bin/env python3
"""Build the Activity 02 prejoined Lipa City barangay shapefile package."""

from __future__ import annotations

import argparse
import shutil
import tempfile
import urllib.request
from pathlib import Path

import geopandas as gpd
import pandas as pd

DEFAULT_SOURCE_URL = (
    "https://github.com/bendlikeabamboo/barangay-boundaries-repository/"
    "releases/download/v2026.4.13.0/barangays.geojson"
)
LIPA_PSGC_PREFIX = "0401014"
EXPECTED_BARANGAYS = 72
EXPECTED_POPULATION_2024 = 387392
TARGET_CRS = "EPSG:32651"
OUTPUT_BASENAME = "ACT02_lipa_barangays_JOINED_UTM51N"


def normalize_psgc(series: pd.Series) -> pd.Series:
    return (
        series.astype(str)
        .str.strip()
        .str.replace(r"\.0$", "", regex=True)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(10)
    )


def find_code_column(gdf: gpd.GeoDataFrame) -> str:
    for candidate in ("psgc_code", "PSGC_CODE", "ADM4_PCODE", "adm4_pcode"):
        if candidate in gdf.columns:
            return candidate
    raise RuntimeError(f"No PSGC field found in boundary source: {list(gdf.columns)}")


def prepare_joined_layer(
    boundaries: gpd.GeoDataFrame, attributes: pd.DataFrame
) -> gpd.GeoDataFrame:
    code_col = find_code_column(boundaries)
    boundary = boundaries[[code_col, "geometry"]].copy()
    boundary["PSGC10"] = normalize_psgc(boundary[code_col])
    boundary = boundary[["PSGC10", "geometry"]]

    attrs = attributes.copy()
    attrs["PSGC10"] = normalize_psgc(attrs["psgc_10_digit"])
    attrs = attrs[["PSGC10", "barangay_name", "urban_rural", "population_2024"]]

    if boundary["PSGC10"].duplicated().any():
        raise RuntimeError("Duplicate PSGC codes found in boundary geometry")
    if attrs["PSGC10"].duplicated().any():
        raise RuntimeError("Duplicate PSGC codes found in ACT02 attributes")

    joined = boundary.merge(attrs, on="PSGC10", how="left", validate="one_to_one")
    if joined["barangay_name"].isna().any():
        missing = joined.loc[joined["barangay_name"].isna(), "PSGC10"].tolist()
        raise RuntimeError(
            "Boundary polygons without matching ACT02 attributes: " + ", ".join(missing)
        )

    joined = gpd.GeoDataFrame(joined, geometry="geometry", crs=boundaries.crs)
    joined = joined.to_crs(TARGET_CRS)
    joined = joined.rename(
        columns={
            "barangay_name": "BRGY_NAME",
            "urban_rural": "URBAN_RUR",
            "population_2024": "POP2024",
        }
    )
    joined["GEO_STAT"] = "REF_NAMRIA"
    joined["GEO_LIMIT"] = "Training reference; not LGU certified legal/cadastral boundary"

    return joined[
        ["PSGC10", "BRGY_NAME", "URBAN_RUR", "POP2024", "GEO_STAT", "GEO_LIMIT", "geometry"]
    ]


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, destination)


def build(repo_root: Path, source_url: str = DEFAULT_SOURCE_URL) -> Path:
    source_csv = repo_root / "data" / "raw" / "ACT01_barangay_profile_RAW.csv"
    output_zip = repo_root / "data" / "processed" / f"{OUTPUT_BASENAME}_shapefile.zip"

    attrs = pd.read_csv(
        source_csv,
        dtype={"psgc_10_digit": str, "correspondence_code": str},
    )
    if len(attrs) != EXPECTED_BARANGAYS:
        raise RuntimeError(f"Expected {EXPECTED_BARANGAYS} ACT02 rows, found {len(attrs)}")
    if int(attrs["population_2024"].sum()) != EXPECTED_POPULATION_2024:
        raise RuntimeError("ACT02 population total does not match the expected 2024 Lipa total")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        source_geojson = tmp / "barangays.geojson"
        download(source_url, source_geojson)
        boundaries = gpd.read_file(source_geojson)
        code_col = find_code_column(boundaries)
        normalized = normalize_psgc(boundaries[code_col])
        lipa = boundaries[normalized.str.startswith(LIPA_PSGC_PREFIX, na=False)].copy()
        if len(lipa) != EXPECTED_BARANGAYS:
            raise RuntimeError(
                f"Expected {EXPECTED_BARANGAYS} Lipa boundary polygons, found {len(lipa)}"
            )

        joined = prepare_joined_layer(lipa, attrs)
        if len(joined) != EXPECTED_BARANGAYS:
            raise RuntimeError(f"Expected {EXPECTED_BARANGAYS} joined polygons, found {len(joined)}")

        shp_dir = tmp / OUTPUT_BASENAME
        shp_dir.mkdir()
        shp_path = shp_dir / f"{OUTPUT_BASENAME}.shp"
        joined.to_file(shp_path, driver="ESRI Shapefile", encoding="UTF-8")

        required = [".shp", ".shx", ".dbf", ".prj", ".cpg"]
        missing = [suffix for suffix in required if not (shp_dir / f"{OUTPUT_BASENAME}{suffix}").exists()]
        if missing:
            raise RuntimeError("Missing shapefile components: " + ", ".join(missing))

        output_zip.parent.mkdir(parents=True, exist_ok=True)
        if output_zip.exists():
            output_zip.unlink()
        archive_base = output_zip.with_suffix("")
        shutil.make_archive(str(archive_base), "zip", root_dir=shp_dir)

    return output_zip


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-url", default=DEFAULT_SOURCE_URL)
    args = parser.parse_args()
    output = build(args.repo_root, args.source_url)
    print(f"Created {output}")


if __name__ == "__main__":
    main()
