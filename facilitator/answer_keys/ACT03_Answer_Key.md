# ACT03 Answer Key: Analysis Assistant

## Expected procedure

Participants define the decision question, inspect available layers and fields, ask AI for a workflow, then critique every operation and assumption. A defensible plan separates exposure, facility access, capacity, condition, and policy priority.

## Expected result

A strong plan includes:

1. Confirm sources, dates, CRS, geometry validity, and unique identifiers.
2. Intersect or spatially select barangays and facilities with `flood_hazard`.
3. Summarize affected features by hazard `LEVEL` without calling the result damage.
4. Identify facilities by `FAC_TYPE`, `CAPACITY`, and `STATUS`.
5. Treat road access as a network or field-validation question, not simple straight-line distance.
6. Join population only through verified `BRGY_CODE` values.
7. Record missing travel time, road condition, occupancy, structural condition, hazard depth, and policy threshold data.

## Verification

Every operation must name its input, output, and check. The next step must consume an earlier output. Thresholds require an identified policy source. Expected-output images may guide discussion but are not substitutes for a participant plan.

## Common mistakes

Choosing one kilometre because AI suggested it; using buffer distance as travel time; treating polygon intersection as impact severity; adding population, exposure, and capacity into an arbitrary score; ignoring duplicate join keys.

## Human validation

DRRM confirms hazard interpretation. Planning confirms decision criteria. Engineering or transport staff confirm accessibility assumptions. Facility owners confirm condition and usable capacity.

## Acceptable alternatives

Participants may propose a staged screen followed by field validation, or network analysis after acquiring routable roads. They may omit a priority score when policy weights are unavailable.

## Discussion questions

Which step requires an official threshold? Which map result is only a screening result? What new data would change the plan most?

## Evidence of understanding

The group rejects at least one plausible AI suggestion and documents why the available data cannot answer an operational question.
