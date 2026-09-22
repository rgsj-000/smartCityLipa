from __future__ import annotations

import importlib.util
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_act02_joined_shapefile.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("act02_builder", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load ACT02 joined shapefile builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sample_boundaries() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "psgc_code": ["401014001", "0401014003"],
            "name": ["Adya boundary", "Anilao boundary"],
        },
        geometry=[box(121.10, 13.90, 121.11, 13.91), box(121.11, 13.90, 121.12, 13.91)],
        crs="EPSG:4326",
    )


def sample_attributes() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "psgc_10_digit": ["0401014001", "0401014003"],
            "barangay_name": ["Adya", "Anilao"],
            "urban_rural": ["Urban", "Rural"],
            "population_2024": [2144, 5019],
        }
    )


def test_prepare_joined_layer_uses_activity02_field_names_and_utm51n():
    builder = load_builder()
    result = builder.prepare_joined_layer(sample_boundaries(), sample_attributes())

    assert list(result.columns) == [
        "PSGC10",
        "BRGY_NAME",
        "URBAN_RUR",
        "POP2024",
        "GEO_STAT",
        "GEO_LIMIT",
        "geometry",
    ]
    assert result.crs.to_epsg() == 32651
    assert result["PSGC10"].tolist() == ["0401014001", "0401014003"]
    assert result["BRGY_NAME"].tolist() == ["Adya", "Anilao"]
    assert result["POP2024"].tolist() == [2144, 5019]
    assert "POP_BAND" not in result.columns
    assert all(len(field) <= 10 for field in result.columns if field != "geometry")


def test_prepare_joined_layer_rejects_unmatched_barangay():
    builder = load_builder()
    attrs = sample_attributes().iloc[[0]].copy()

    with pytest.raises(RuntimeError, match="without matching ACT02 attributes"):
        builder.prepare_joined_layer(sample_boundaries(), attrs)
