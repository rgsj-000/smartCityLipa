# ACT02 Workflow: QGIS Assistant

**Official slot:** Day 1, 4:30 PM to 5:00 PM

**Required output:** Working verified expression or workflow

## Objective

Continue from the ACT01 barangay profile. Use AI to draft and explain a QGIS expression, then verify the exact field name, syntax, thresholds, null handling, and meaning in QGIS.

## Scenario

Use `population_2024`, already examined in ACT01, to create a training field named `population_band_synth`.

The Low, Medium, and High bands are exercise rules only and are not an official LGU classification.

## Required files

`data/raw/ACT01_barangay_profile_RAW.csv`

Editable QGIS working copy of the ACT01 barangay profile

`workflows/qgis_expressions.md`

If the imported CSV is read only, save or export it as an editable working layer first. Do not overwrite the raw CSV.

## Timed procedure

1. **Prompt structure, 4 minutes:** State the task, source field, rule, output field, QGIS environment, and verification tests.
2. **Live demonstration, 6 minutes:** Ask AI for `population_band_synth` from `population_2024` and inspect the explanation.
3. **Participant task, 14 minutes:** Create or update the text field `population_band_synth` and run the Field Calculator expression.
4. **Boundary challenge, 3 minutes:** In the QGIS expression preview, temporarily replace every `population_2024` reference with `4999`, `5000`, `10000`, `10001`, and `NULL`, one at a time. Read the preview result and do not save the literal tests.
5. **Verification and debrief, 3 minutes:** Inspect actual ACT01 records, record any correction, and save the working expression or documented workflow.

## Expected result

Low below 5,000, Medium from 5,000 through 10,000, High above 10,000, and Unknown for null.

Representative checks are Adya at 2,144 as Low, Anilao at 5,019 as Medium, Latag at 9,230 as Medium, and Balintawak at 19,063 as High.

## Verification

Confirm that `population_2024` exists, that `population_band_synth` is text, and that all boundary and null tests pass. Inspect representative ACT01 records and explain every branch.

## Common mistakes

Using the old `POP_TOTAL` or `POP_CLASS` fields, using `<= 5000` for Low, omitting null handling, creating a numeric output field, editing the raw CSV, or treating the exercise thresholds as an official standard.

## Human validation

The GIS analyst validates the implementation. A real planning classification requires a documented basis and approval from the responsible office.
