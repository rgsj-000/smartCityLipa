from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "ACT01_barangay_profile_RAW.csv"
OUTPUT = ROOT / "data" / "processed" / "ACT02_QGIS_Assistant.gpkg"

INTEGER_FIELDS = {
    "record_id",
    "population_2024",
    "estimated_households",
    "pwd_count_synth",
    "school_count_synth",
    "health_facility_count_synth",
    "evacuation_center_count_synth",
    "evacuation_capacity_synth",
    "streetlight_count_synth",
    "fire_incidents_2025_synth",
    "flood_incidents_2025_synth",
}

REAL_FIELDS = {
    "area_km2_synth",
    "population_density_synth",
    "senior_citizen_pct_synth",
    "children_0_14_pct_synth",
    "low_income_household_pct_synth",
    "internet_access_pct_synth",
    "improved_water_access_pct_synth",
    "solid_waste_collection_coverage_pct_synth",
    "road_length_km_synth",
    "paved_road_pct_synth",
    "avg_emergency_response_min_synth",
}


def sqlite_type(field: str) -> str:
    if field in INTEGER_FIELDS:
        return "INTEGER"
    if field in REAL_FIELDS:
        return "REAL"
    return "TEXT"


def convert(field: str, value: str):
    value = value.strip() if isinstance(value, str) else value
    if value == "":
        return None
    if field in INTEGER_FIELDS:
        return int(value)
    if field in REAL_FIELDS:
        return float(value)
    return value


def create_core_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        PRAGMA application_id = 1196444487;
        PRAGMA user_version = 10200;

        CREATE TABLE gpkg_spatial_ref_sys (
            srs_name TEXT NOT NULL,
            srs_id INTEGER NOT NULL PRIMARY KEY,
            organization TEXT NOT NULL,
            organization_coordsys_id INTEGER NOT NULL,
            definition TEXT NOT NULL,
            description TEXT
        );

        CREATE TABLE gpkg_contents (
            table_name TEXT NOT NULL PRIMARY KEY,
            data_type TEXT NOT NULL,
            identifier TEXT UNIQUE,
            description TEXT DEFAULT '',
            last_change DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
            min_x DOUBLE,
            min_y DOUBLE,
            max_x DOUBLE,
            max_y DOUBLE,
            srs_id INTEGER,
            CONSTRAINT fk_gc_r_srs_id FOREIGN KEY (srs_id)
                REFERENCES gpkg_spatial_ref_sys(srs_id)
        );

        CREATE TABLE gpkg_geometry_columns (
            table_name TEXT NOT NULL,
            column_name TEXT NOT NULL,
            geometry_type_name TEXT NOT NULL,
            srs_id INTEGER NOT NULL,
            z TINYINT NOT NULL,
            m TINYINT NOT NULL,
            CONSTRAINT pk_geom_cols PRIMARY KEY (table_name, column_name),
            CONSTRAINT uk_gc_table_name UNIQUE (table_name),
            CONSTRAINT fk_gc_tn FOREIGN KEY (table_name)
                REFERENCES gpkg_contents(table_name),
            CONSTRAINT fk_gc_srs FOREIGN KEY (srs_id)
                REFERENCES gpkg_spatial_ref_sys(srs_id)
        );
        """
    )

    conn.executemany(
        "INSERT INTO gpkg_spatial_ref_sys VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                "Undefined Cartesian SRS",
                -1,
                "NONE",
                -1,
                "undefined",
                "undefined Cartesian coordinate reference system",
            ),
            (
                "Undefined Geographic SRS",
                0,
                "NONE",
                0,
                "undefined",
                "undefined geographic coordinate reference system",
            ),
            (
                "WGS 84 geodetic",
                4326,
                "EPSG",
                4326,
                'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433]]',
                "longitude/latitude coordinates in decimal degrees on the WGS 84 spheroid",
            ),
        ],
    )


def build() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()

    with SOURCE.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fields = reader.fieldnames or []

    if not fields:
        raise RuntimeError("ACT01 source CSV has no header")

    conn = sqlite3.connect(OUTPUT)
    try:
        create_core_tables(conn)

        column_sql = ["fid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL"]
        column_sql.extend(f'"{field}" {sqlite_type(field)}' for field in fields)
        conn.execute(
            f'CREATE TABLE "act02_barangay_profile" ({", ".join(column_sql)})'
        )

        placeholders = ", ".join("?" for _ in fields)
        field_sql = ", ".join(f'"{field}"' for field in fields)
        insert_sql = (
            f'INSERT INTO "act02_barangay_profile" ({field_sql}) '
            f'VALUES ({placeholders})'
        )
        conn.executemany(
            insert_sql,
            [[convert(field, row.get(field, "")) for field in fields] for row in rows],
        )

        conn.execute(
            """
            CREATE TABLE act02_activity_info (
                id INTEGER PRIMARY KEY,
                activity_id TEXT NOT NULL,
                title TEXT NOT NULL,
                purpose TEXT NOT NULL,
                source_table TEXT NOT NULL,
                source_field TEXT NOT NULL,
                output_field TEXT NOT NULL,
                output_type TEXT NOT NULL,
                training_rule TEXT NOT NULL,
                verification TEXT NOT NULL,
                data_note TEXT NOT NULL
            )
            """
        )
        conn.execute(
            """
            INSERT INTO act02_activity_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                1,
                "ACT02",
                "QGIS Assistant",
                "Generate, explain, test, and correct a QGIS Field Calculator expression.",
                "act02_barangay_profile",
                "population_2024",
                "population_band_synth",
                "TEXT",
                "Low below 5,000; Medium 5,000 through 10,000; High above 10,000; Unknown for NULL. Training-only classification.",
                "Test 4999, 5000, 10000, 10001, and NULL; inspect Adya, Anilao, Latag, and Balintawak.",
                "Contains official PSA reference fields plus synthetic training fields inherited from ACT01. Not for operational decisions.",
            ),
        )

        conn.executemany(
            """
            INSERT INTO gpkg_contents
                (table_name, data_type, identifier, description, srs_id)
            VALUES (?, 'attributes', ?, ?, NULL)
            """,
            [
                (
                    "act02_barangay_profile",
                    "act02_barangay_profile",
                    "ACT02 editable barangay profile for QGIS Field Calculator exercise",
                ),
                (
                    "act02_activity_info",
                    "ACT02 Activity Info",
                    "Activity metadata and verification instructions",
                ),
            ],
        )

        conn.commit()
        result = conn.execute("PRAGMA integrity_check").fetchone()[0]
        if result != "ok":
            raise RuntimeError(f"GeoPackage integrity check failed: {result}")

        geometry_columns_exists = conn.execute(
            """
            SELECT COUNT(*)
            FROM sqlite_master
            WHERE type = 'table' AND name = 'gpkg_geometry_columns'
            """
        ).fetchone()[0]
        if geometry_columns_exists != 1:
            raise RuntimeError("GeoPackage is missing gpkg_geometry_columns")

        count = conn.execute(
            "SELECT COUNT(*) FROM act02_barangay_profile"
        ).fetchone()[0]
        if count != 72:
            raise RuntimeError(f"Expected 72 barangay records, found {count}")
    finally:
        conn.close()

    print(f"Created {OUTPUT.relative_to(ROOT)} with {len(rows)} barangay records")


if __name__ == "__main__":
    build()
