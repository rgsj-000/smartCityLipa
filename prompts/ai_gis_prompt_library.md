# AI + GIS Prompt Library

Use the structure below whenever AI assists a GIS task.

## Prompt structure

**Role:** The perspective AI should use

**Objective:** The decision or GIS task

**Data:** Exact layer names, fields, CRS, sample values, and known sources

**Constraints:** Rules, unavailable data, prohibited assumptions, and software version

**Expected output:** The format you need

**Verification:** What the participant must check in QGIS or with the data owner

## ACT01: Data dictionary draft

> Act as a GIS data steward. Review only the supplied fields and sample rows from `ACT01_barangay_profile_RAW.csv`. The profile includes official PSA reference fields such as `psgc_10_digit`, `correspondence_code`, `barangay_name`, `urban_rural`, and `population_2024`, plus fields ending in `_synth` for training. Draft a table with field name, possible meaning, likely data type, unit or allowed values, data-quality question, and confidence. Mark every claim that is not confirmed by the supplied reference dictionary as Needs confirmation. Do not invent a source, date, definition, or official status.

Verification questions:

1. Did AI invent an official source or definition?
2. Are identifier fields such as `psgc_10_digit` and `correspondence_code` preserved correctly?
3. Which `_synth` fields or meanings still need confirmation from the supplied documentation?

## ACT02: QGIS expression

> Act as a QGIS 3.34 assistant. Continue from the ACT01 barangay profile. In Field Calculator, create the text field `population_band_synth` using only integer field `population_2024`. For this training exercise, return Low below 5,000, Medium from 5,000 through 10,000, High above 10,000, and Unknown for null. Provide one QGIS expression, explain each condition, and list the boundary tests 4,999, 5,000, 10,000, 10,001, and null. Do not present these bands as an official LGU classification.

## ACT02: Troubleshooting

> In QGIS 3.34, my editable working copy of `ACT01_barangay_profile_RAW.csv` uses field `population_2024`. The Field Calculator expression runs but 5,000 is classified as Low. Review this expression and explain the exact boundary error: `if("population_2024" <= 5000, 'Low', if("population_2024" <= 10000, 'Medium', 'High'))`. Provide a corrected expression that also handles null and writes a text result for `population_band_synth`. Keep the raw CSV unchanged.

## ACT03: Analysis plan

> Act as a GIS analysis planner. We need to identify synthetic training barangays that may require priority evacuation planning based on mapped flood exposure, population, and access to evacuation facilities. Available layers are barangays, facilities, roads, and flood_hazard in EPSG:32651. Propose a sequence with required fields, QGIS operation, purpose, intermediate output, validation, and limitation for each step. Do not choose distance or priority thresholds unless a policy basis is provided. Do not invent road condition, travel time, flood depth, or facility structural condition.

## ACT04: Metadata and QA

> Act as a GIS documentation assistant. Turn the processing notes below into a draft metadata and QA record with dataset title, geographic coverage, CRS, source, source date, processing steps, validation questions, limitations, update requirement, responsible person, and status. Leave an explicit blank or Unknown where the notes do not provide a fact. Do not invent provenance.

## ACT05: Decision-support report

> Prepare a concise LGU GIS decision-support report using only the verified facts supplied. Separate Observation, Interpretation, Limitation, and Possible Action. Preserve every number exactly. Do not add locations, causes, policy thresholds, forecasts, or conclusions. Phrase actions as matters for validation or consideration by the responsible LGU office.

## Known bad response

> The city must immediately evacuate all residents within one kilometre of every flood polygon because the map proves these areas will flood tomorrow.

Problems: the dataset contains no forecast, no one-kilometre policy, no resident locations, and no evacuation order. The statement turns a synthetic overlay into an official decision.

## Corrected response

> The synthetic overlay identifies mapped barangays and facilities that intersect the training flood-hazard polygons. The result supports a review of exposure and facility readiness. It does not establish forecast timing, flood depth, structural safety, road accessibility, or the need for an evacuation order. The responsible offices should validate the source data and current field conditions before using a similar workflow for planning.
