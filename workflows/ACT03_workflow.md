# ACT03 Workflow: From an LGU Question to a GIS Analysis Plan

**Official slot:** Day 2, 2:00 PM to 2:45 PM

**Required output:** One-page GIS analysis plan

**Working CRS:** WGS 84 / UTM zone 51N, EPSG:32651

## Objective

Translate an LGU decision question into a defensible sequence of data requirements, GIS operations, intermediate outputs, checks, assumptions, and limitations. AI may structure the plan, but QGIS and human/domain validation determine whether the plan is acceptable.

## Scenario

The LGU wants to screen which Lipa City barangays may warrant further examination for evacuation planning based on mapped flood exposure, population, and proximity to evacuation facilities.

Do not ask AI to decide which barangay is officially high-risk or priority.

## ACT03 datasets

Use these files explicitly:

1. `data/act03/generated/ACT03_Lipa_Training_UTM51N.gpkg`
   * `lipa_barangays_reference`
   * `facilities_synthetic`
   * `roads_synthetic`
   * `flood_hazard_synthetic`
2. `data/act03/ACT03_lipa_barangays_PSA_2024.csv`
3. `data/act03/ACT03_DATASET_MANIFEST.csv`

If the generated GeoPackage is not present, run:

```bash
python scripts/build_act03_lipa_boundary.py
```

The barangay geometry is reference/NAMRIA-derived rather than an LGU-certified legal boundary. PSA names, PSGC codes, urban/rural classification, and 2024 population are official reference attributes. Facilities, roads, and flood hazard features are synthetic training data.

## Decision question

> Which Lipa City barangays may warrant further examination for evacuation planning based on mapped flood exposure, population, and proximity to evacuation facilities?

## Timed procedure

1. **Inspect and verify, 7 minutes:** Confirm 72 barangays, join key, available fields, layer alignment, and EPSG:32651.
2. **Write the decision question, 5 minutes:** State what the available data can answer and what it cannot answer.
3. **AI plan, 8 minutes:** Ask AI for a sequenced workflow without giving it an invented buffer distance, priority score, travel-time assumption, or hazard threshold.
4. **Group verification, 15 minutes:** Review every proposed input, field, spatial operation, intermediate output, validation check, and limitation against the QGIS layers.
5. **Critique and revise, 7 minutes:** Reject or revise at least one unsupported AI suggestion.
6. **Consolidate, 3 minutes:** Save the one-page GIS analysis plan.

## Required plan columns

| Step | Required input | Required field | Proposed QGIS operation | Purpose | Expected output | Verification | Limitation |
|---|---|---|---|---|---|---|---|

## Prompt scaffold

```text
I am preparing a GIS analysis for evacuation planning in Lipa City, Batangas.

My working barangay layer is a reference Lipa City boundary layer in
WGS 84 / UTM zone 51N (EPSG:32651). Official/reference attributes include
PSGC code, barangay name, urban/rural classification, and 2024 population.

Available supporting layers are synthetic training facilities, roads, and
flood-hazard polygons.

My decision question is:
[write the question]

Propose a sequence of QGIS spatial-analysis operations that could help answer
the question. For every step identify the required input, required field,
QGIS operation, purpose, expected output, verification check, and limitation.

Do not invent missing data, policy thresholds, buffer distances, travel
times, facility capacity rules, flood depth, road condition, or government
standards. Mark unavailable information as a data gap. Do not decide which
barangay is officially high-risk or priority.
```

## Expected reasoning

A defensible plan normally begins with source/CRS/join checks, separates population from hazard exposure, uses overlay/intersection only for mapped exposure, treats facility proximity as straight-line unless a network method is actually available, treats road accessibility as a separate question, and records missing operational information.

## Verification

Confirm that every proposed operation has an available input and produces an output used by the next step.

Reject or revise any AI suggestion that:

1. invents a threshold;
2. calls straight-line distance travel time;
3. treats intersection as proof of damage;
4. assumes a mapped facility is operational;
5. uses facility capacity as sufficient without occupancy/condition data;
6. assumes roads are passable;
7. creates a composite priority score without an approved weighting method.

## Required final output

`ACT03_Group##_GIS_Analysis_Plan.pdf` or the facilitator-approved editable equivalent.

The plan must contain:

1. Decision question
2. Datasets and required fields
3. Sequenced GIS operations
4. Expected outputs
5. Verification checks
6. Data gaps and known limitations
7. One rejected or revised AI recommendation

**AI assists. QGIS verifies. People decide.**
