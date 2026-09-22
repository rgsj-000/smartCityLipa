#!/usr/bin/env python3
"""
Build the ACT03 Lipa City reference boundary package.

Boundary source:
  bendlikeabamboo/barangay-boundaries-repository
  Curated Philippine barangay boundaries derived from NAMRIA shapefiles and
  enriched with PSA PSGC codes.

IMPORTANT:
  The generated barangay geometry is a REFERENCE training boundary, not an
  LGU-certified cadastral or legal boundary.

Official/reference attributes:
  Philippine Statistics Authority PSGC City of Lipa listing / 2024 POPCEN.

Outputs are written to data/act03/generated/.
"""

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
TARGET_CRS = "EPSG:32651"
EXPECTED_POPULATION_2024 = 387392


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading boundary source: {url}")
    urllib.request.urlretrieve(url, destination)


def normalize_psgc(series: pd.Series) -> pd.Series:
    """Normalize PSGC values to zero-padded 10-character strings."""
    return (
        series.astype(str)
        .str.strip()
        .str.replace(r"\.0$", "", regex=True)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(10)
    )


def find_code_column(gdf: gpd.GeoDataFrame) -> str:
    candidates = [
        "psgc_code",
        "PSGC_CODE",
        "ADM4_PCODE",
        "adm4_pcode",
    ]
    for col in candidates:
        if col in gdf.columns:
            return col
    raise RuntimeError(
        "Could not locate a PSGC/barangay code field. "
        f"Available columns: {list(gdf.columns)}"
    )


def build(source_url: str, repo_root: Path) -> None:
    act03_dir = repo_root / "data" / "act03"
    generated = act03_dir / "generated"
    generated.mkdir(parents=True, exist_ok=True)

    psa_csv = act03_dir / "ACT03_lipa_barangays_PSA_2024.csv"
    facilities_geojson = act03_dir / "ACT03_facilities_SYNTHETIC.geojson"
    roads_geojson = act03_dir / "ACT03_roads_SYNTHETIC.geojson"
    flood_geojson = act03_dir / "ACT03_flood_hazard_SYNTHETIC.geojson"

    required = [psa_csv, facilities_geojson, roads_geojson, flood_geojson]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing ACT03 source files:\n  " + "\n  ".join(missing)
        )

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        national_geojson = tmp / "barangays.geojson"
        download(source_url, national_geojson)

        print("Reading Philippine barangay boundaries...")
        boundaries = gpd.read_file(national_geojson)
        code_col = find_code_column(boundaries)
        boundaries[code_col] = normalize_psgc(boundaries[code_col])

        lipa = boundaries[
            boundaries[code_col].str.startswith(LIPA_PSGC_PREFIX, na=False)
        ].copy()

        if len(lipa) != EXPECTED_BARANGAYS:
            raise RuntimeError(
                f"Expected {EXPECTED_BARANGAYS} Lipa barangay polygons, "
                f"but found {len(lipa)}. Review source version/matching before use."
            )

        official = pd.read_csv(
            psa_csv,
            dtype={"psgc_10_digit": str, "correspondence_code": str},
        )
        official["psgc_10_digit"] = normalize_psgc(official["psgc_10_digit"])

        if official["psgc_10_digit"].duplicated().any():
            raise RuntimeError("Duplicate PSGC codes found in PSA reference table.")

        if int(official["population_2024"].sum()) != EXPECTED_POPULATION_2024:
            raise RuntimeError(
                "PSA population total does not match the expected City of Lipa "
                f"2024 POPCEN total of {EXPECTED_POPULATION_2024:,}."
            )

        if len(official) != EXPECTED_BARANGAYS:
            raise RuntimeError(
                f"Expected {EXPECTED_BARANGAYS} PSA attribute rows, "
                f"but found {len(official)}."
            )

        lipa = lipa.rename(columns={code_col: "boundary_psgc_code"})
        lipa["boundary_psgc_code"] = normalize_psgc(lipa["boundary_psgc_code"])
        lipa = lipa.merge(
            official,
            left_on="boundary_psgc_code",
            right_on="psgc_10_digit",
            how="left",
            validate="one_to_one",
        )

        if lipa["barangay_name"].isna().any():
            missing_codes = lipa.loc[
                lipa["barangay_name"].isna(), "boundary_psgc_code"
            ].tolist()
            raise RuntimeError(
                "Boundary polygons without matching PSA rows: "
                + ", ".join(missing_codes)
            )

        lipa["geometry_source_status"] = "REFERENCE_NAMRIA_DERIVED"
        lipa["geometry_use_limitation"] = (
            "Reference training boundary; not LGU-certified cadastral/legal geometry"
        )

        lipa_wgs84 = lipa.to_crs("EPSG:4326")
        wgs84_path = generated / "ACT03_lipa_barangays_REFERENCE_WGS84.geojson"
        lipa_wgs84.to_file(wgs84_path, driver="GeoJSON")

        lipa_utm = lipa.to_crs(TARGET_CRS)
        gpkg_path = generated / "ACT03_lipa_barangays_REFERENCE_UTM51N.gpkg"
        if gpkg_path.exists():
            gpkg_path.unlink()
        lipa_utm.to_file(gpkg_path, layer="lipa_barangays", driver="GPKG")

        shp_dir = tmp / "ACT03_lipa_barangays_REFERENCE_UTM51N"
        shp_dir.mkdir()
        shp_path = shp_dir / "ACT03_lipa_barangays_REFERENCE_UTM51N.shp"
        lipa_utm.to_file(shp_path, driver="ESRI Shapefile")
        zip_base = generated / "ACT03_lipa_barangays_REFERENCE_UTM51N_shapefile"
        zip_path = Path(str(zip_base) + ".zip")
        if zip_path.exists():
            zip_path.unlink()
        shutil.make_archive(str(zip_base), "zip", root_dir=shp_dir)

        full_gpkg = generated / "ACT03_Lipa_Training_UTM51N.gpkg"
        if full_gpkg.exists():
            full_gpkg.unlink()

        lipa_utm.to_file(
            full_gpkg,
            layer="lipa_barangays_reference",
            driver="GPKG",
        )

        facilities = gpd.read_file(facilities_geojson).to_crs(TARGET_CRS)
        facilities.to_file(full_gpkg, layer="facilities_synthetic", driver="GPKG")

        roads = gpd.read_file(roads_geojson).to_crs(TARGET_CRS)
        roads.to_file(full_gpkg, layer="roads_synthetic", driver="GPKG")

        flood = gpd.read_file(flood_geojson).to_crs(TARGET_CRS)
        flood.to_file(full_gpkg, layer="flood_hazard_synthetic", driver="GPKG")

        print("ACT03 dataset build complete.")
        print(f"  Barangays: {len(lipa_utm)}")
        print(f"  CRS: {lipa_utm.crs}")
        print(f"  WGS84 GeoJSON: {wgs84_path}")
        print(f"  UTM 51N GeoPackage: {gpkg_path}")
        print(f"  UTM 51N Shapefile ZIP: {zip_path}")
        print(f"  Combined ACT03 GeoPackage: {full_gpkg}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-url",
        default=DEFAULT_SOURCE_URL,
        help="Override the public Philippine barangay boundary GeoJSON URL.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing data/act03.",
    )
    args = parser.parse_args()
    build(args.source_url, Path(args.repo_root).resolve())


if __name__ == "__main__":
    main()
