# ACT05 Offline AI Response

## User prompt

Write an LGU decision-support brief using only these verified facts: a synthetic polygon intersection identified five training barangays with some mapped hazard overlap; the project includes ten synthetic facilities; the analysis does not include flood depth, road passability, structural condition, occupancy, or a forecast. Separate Observation, Interpretation, Limitation, and Possible Action.

## AI response

**Observation:** The synthetic spatial intersection identifies five training barangays with some overlap with the mapped flood-hazard polygons. The project contains ten synthetic facility points.

**Interpretation:** The mapped overlap can support a preliminary review of which areas and facilities need further exposure and readiness checks.

**Limitation:** The result does not establish flood depth, current road passability, facility structural condition, occupancy, forecast timing, actual damage, or the need for an evacuation order.

**Possible Action:** The responsible LGU offices may validate the source data, current field conditions, facility readiness, and approved decision criteria before adapting the workflow for operational planning.

## What is correct

The response preserves the supplied counts, separates evidence layers, and avoids issuing a decision.

## What needs verification

Confirm the selection count in QGIS and ensure that “some overlap” matches the actual spatial predicate used.

## Potential errors

AI may convert overlap into “affected,” add a forecast, or recommend immediate evacuation. None of those claims follows from the supplied facts.

## Facilitator explanation

Have groups highlight every noun, number, and action phrase. Each must trace to GIS evidence, stated limitation, or authorized responsibility.

## Improved prompt

Add the exact analysis method, data sources, verified numeric results, and intended reader. Tell AI to flag any sentence it cannot support.
