# ACT04 Workflow: GIS QA and Documentation

**Official slot:** Day 2, 4:00 PM to 4:45 PM

**Required output:** Metadata and QA sheet

## Objective

Use AI to organize processing notes without allowing it to invent provenance, dates, responsibility, accuracy, or limitations.

## Scenario

A colleague must reproduce the flood-exposure map six months later. The current analyst has only rough processing notes.

## Required files

The QGIS project, `data/reference/data_dictionary.csv`, and a participant-created processing history.

## Timed procedure

1. **Trust question, 5 minutes:** Ask whether another employee can reproduce the map.
2. **Documentation demo, 8 minutes:** Give AI rough notes and require Unknown for missing facts.
3. **Participant documentation, 15 minutes:** Draft metadata, processing history, QA questions, and limitations.
4. **Source audit, 10 minutes:** Check CRS, source, date, layer names, field names, and output location.
5. **Debrief, 7 minutes:** Identify one fact AI could not know.

## Expected result

A Metadata and QA sheet with dataset title, coverage, CRS, source, source date, processing steps, validation checks, limitations, responsible person, update requirement, and status.

## Verification

Compare every metadata entry with the project, source file, or responsible person. Re-run one processing step or inspect one intermediate result to test reproducibility.

## Common mistakes

Letting AI invent a data source or collection date; omitting field calculations; failing to record the CRS; using “accurate” without a test; forgetting what the output should not support.

## Human validation

The analyst signs the processing record. The data owner confirms provenance and update responsibilities.
