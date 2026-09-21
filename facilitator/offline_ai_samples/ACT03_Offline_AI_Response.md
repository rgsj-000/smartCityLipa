# ACT03 Offline AI Response

## User prompt

Plan a QGIS analysis to screen barangays for evacuation planning using barangays, facilities, roads, and flood_hazard in EPSG:32651. Do not invent thresholds or unavailable data.

## AI response

1. Validate CRS, geometry, dates, unique identifiers, and required fields.
2. Select or intersect barangays with flood_hazard and retain hazard LEVEL.
3. Select facilities that intersect the hazard and summarize FAC_TYPE, CAPACITY, and STATUS.
4. Join population by verified BRGY_CODE.
5. Review road proximity, but do not treat straight-line distance as travel time.
6. Document missing road condition, travel time, occupancy, structural condition, flood depth, and policy thresholds.
7. Present screening results for domain and field validation.

## What is correct

The sequence begins with data checks, separates exposure and access, and avoids unsupported priority thresholds.

## What needs verification

Participants must select the exact QGIS tools, inspect intermediate results, and confirm which decision criteria the LGU recognizes.

## Potential errors

The phrase “road proximity” remains vague. A road network layer does not automatically contain passability or travel-time data.

## Facilitator explanation

Ask which step AI cannot complete without policy guidance. A group that invents a one-kilometre threshold must identify and defend its source or remove it.

## Improved prompt

Require a table with input, operation, purpose, output, verification, assumption, and limitation for every step.
