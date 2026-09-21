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

> Act as a GIS data steward. Review the following fields and sample values from a synthetic training dataset: BRGY_CODE, BRGY_NAME, POP_TOTAL, HH_COUNT, AREA_KM2, POP_DENS, and POP_CLASS. Draft a table with possible meaning, likely data type, unit, possible values, data-quality questions, and confidence. Mark any meaning that cannot be confirmed from the names and samples alone. Do not present inferred meanings as official definitions.

Verification questions:

1. Did AI invent an official source or definition?
2. Do the proposed types preserve identifiers such as BRGY_CODE as text?
3. Which meanings need confirmation from the data owner?

## ACT02: QGIS expression

> Act as a QGIS 3.34 assistant. In Field Calculator, create the text field POP_CLASS from integer field POP_TOTAL. Return Low below 5,000, Medium from 5,000 through 10,000, High above 10,000, and Unknown for null. Provide one QGIS expression, explain each condition, and list boundary test values. Use only the stated fields.

## ACT02: Troubleshooting

> In QGIS 3.34, my population layer uses EPSG:32651 and field POP_TOTAL. The Field Calculator expression runs but 5,000 is classified as Low. Review this expression and explain the exact boundary error: `if("POP_TOTAL" <= 5000, 'Low', if("POP_TOTAL" <= 10000, 'Medium', 'High'))`. Provide a corrected expression that also handles null.

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
