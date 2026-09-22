# ACT03 Data Guide: Lipa City Analysis Assistant

## Scope

ACT03 is a 45-minute planning exercise. Participants start from an LGU decision question and produce a defensible GIS analysis plan. They are not expected to declare actual barangays as high-risk or priority locations.

## Geographic foundation

The working barangay layer is generated from a public Philippine barangay boundary dataset documented as NAMRIA-derived and PSGC-enriched. The training build filters Lipa City by PSGC prefix `0401014` and validates that 72 barangay features are present.

The generated geometry is a **reference training boundary**, not an LGU-certified legal or cadastral boundary.

## Official/reference attributes

`data/act03/ACT03_lipa_barangays_PSA_2024.csv`

Fields:

| Field | Meaning |
|---|---|
| `psgc_10_digit` | PSA 10-digit barangay PSGC |
| `correspondence_code` | PSA correspondence code |
| `barangay_name` | PSA barangay name |
| `urban_rural` | PSA urban/rural classification |
| `population_2024` | 2024 POPCEN population |
| `source_status` | `OFFICIAL_REFERENCE` |
| `source_url` | PSA source page |

The 72 population values sum to **387,392**, matching the PSA City of Lipa 2024 POPCEN total.

## Synthetic supporting layers

### Facilities

`ACT03_facilities_SYNTHETIC.csv` and `ACT03_facilities_SYNTHETIC.geojson`

Twenty-four fictional training facilities. Names, capacities, statuses, barangay assignments, and coordinates are synthetic. The CSV includes WGS84 longitude/latitude and derived EPSG:32651 easting/northing.

### Roads

`ACT03_roads_SYNTHETIC.geojson`

Eight fictional line features for accessibility workflow planning. They do not represent the Lipa City road network and must not be used for travel time, passability, routing, or engineering conclusions.

### Flood hazard

`ACT03_flood_hazard_SYNTHETIC.geojson`

Four fictional flood polygons. They exist only to let participants reason about overlay/intersection and to distinguish mapped exposure from actual damage, depth, probability, or risk.

## Build outputs

Running `python scripts/build_act03_lipa_boundary.py` creates:

| Output | CRS | Use |
|---|---|---|
| `ACT03_lipa_barangays_REFERENCE_WGS84.geojson` | EPSG:4326 | Source/reference copy |
| `ACT03_lipa_barangays_REFERENCE_UTM51N.gpkg` | EPSG:32651 | Metric barangay layer |
| `ACT03_lipa_barangays_REFERENCE_UTM51N_shapefile.zip` | EPSG:32651 | SHP package |
| `ACT03_Lipa_Training_UTM51N.gpkg` | EPSG:32651 | Recommended ACT03 QGIS dataset |

## Decision question

> Which Lipa City barangays may warrant further examination for evacuation planning based on mapped flood exposure, population, and proximity to evacuation facilities?

The activity must not convert that screening question into an official risk ranking.

## Minimum verification

Participants should verify:

1. Lipa barangay feature count is 72.
2. Barangay PSGC codes join one-to-one to the PSA table.
3. Working CRS is EPSG:32651 before metric analysis.
4. Synthetic facilities are not treated as verified operational facilities.
5. Straight-line proximity is not called travel time.
6. Synthetic flood intersection is not called actual flood damage.
7. Any threshold or scoring rule has a stated source or is left unresolved.
8. Missing operational datasets are recorded as limitations.
