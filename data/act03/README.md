# ACT03 Dataset Package

ACT03 uses real Lipa City administrative names and official PSA reference attributes, combined with clearly labeled reference/synthetic spatial data for training.

## Required files

| File | Status | CRS | Purpose |
|---|---|---|---|
| `ACT03_lipa_barangays_PSA_2024.csv` | Official reference attributes | N/A | 72 Lipa City barangays, PSGC codes, urban/rural class, 2024 POPCEN |
| `ACT03_facilities_SYNTHETIC.csv` | Synthetic training | EPSG:4326 + EPSG:32651 XY | Facility attributes and coordinates |
| `ACT03_facilities_SYNTHETIC.geojson` | Synthetic training | EPSG:4326 | Facility points |
| `ACT03_roads_SYNTHETIC.geojson` | Synthetic training | EPSG:4326 | Road lines for accessibility discussion |
| `ACT03_flood_hazard_SYNTHETIC.geojson` | Synthetic training | EPSG:4326 | Flood polygons for exposure workflow planning |
| `ACT03_DATASET_MANIFEST.csv` | Documentation | N/A | Provenance, CRS, and use limitations |

## Generated boundary files

Run:

```bash
python scripts/build_act03_lipa_boundary.py
```

The script downloads the public Philippine barangay boundary GeoJSON, filters Lipa City using PSGC prefix `0401014`, joins the PSA reference attributes, and writes:

```text
data/act03/generated/
  ACT03_lipa_barangays_REFERENCE_WGS84.geojson
  ACT03_lipa_barangays_REFERENCE_UTM51N.gpkg
  ACT03_lipa_barangays_REFERENCE_UTM51N_shapefile.zip
  ACT03_Lipa_Training_UTM51N.gpkg
```

Use `ACT03_Lipa_Training_UTM51N.gpkg` for the activity. Its project/layer CRS is **WGS 84 / UTM zone 51N, EPSG:32651**.

## Data status

`ACT03_lipa_barangays_PSA_2024.csv` contains official/reference values from the Philippine Statistics Authority City of Lipa PSGC listing and 2024 POPCEN.

The generated boundary geometry is sourced from the public `barangay-boundaries-repository`, which documents its barangay polygons as derived from NAMRIA shapefiles and enriched/matched to PSA PSGC codes. For this training package, the geometry is deliberately labeled **REFERENCE_NAMRIA_DERIVED**. It is not represented as an LGU-certified cadastral or legal boundary.

Facilities, roads, hazard polygons, capacities, statuses, and other ACT03 operational-looking values are synthetic. They must not be used for actual evacuation, engineering, DRRM, land-use, or public-safety decisions.

## ACT03 join key

Use the 10-digit PSGC code.

```text
boundary_psgc_code  ↔  psgc_10_digit
```

Expected Lipa City count: **72 barangays**.

## Why EPSG:32651?

The source boundary is preserved once in EPSG:4326 for traceability. The working copy is reprojected to EPSG:32651 so participants can evaluate metric distance, proximity, buffer, and area operations in meters.

## Activity rule

AI may propose a workflow. Participants must verify layer names, fields, CRS, spatial relationships, thresholds, and limitations in QGIS before accepting the plan.

**AI assists. QGIS verifies. People decide.**
