# ACT02 Workflow: QGIS Assistant

**Official slot:** Day 1, 4:30 PM to 5:00 PM

**Required output:** Working verified expression or workflow

## Objective

Use AI to draft and explain a QGIS expression, then verify its syntax, boundary behavior, null handling, and meaning in QGIS.

## Scenario

The planning team needs a repeatable population classification for the initial thematic map.

## Required files

`qgis/Lipa_AI_GIS_Training.qgz`, layer `barangays`, and `workflows/qgis_expressions.md`

## Timed procedure

1. **Prompt structure, 4 minutes:** State Task, Data, Rule, Output, and Environment.
2. **Live demonstration, 6 minutes:** Ask AI for `POP_CLASS` and inspect the explanation.
3. **Participant task, 14 minutes:** Create or update the text field in Field Calculator.
4. **Boundary challenge, 3 minutes:** In the QGIS expression preview, temporarily replace every `POP_TOTAL` reference with `4999`, `5000`, `10000`, `10001`, and `NULL`, one test at a time. Read the preview result and do not save the literal tests.
5. **Verification and debrief, 3 minutes:** Run the final field-based expression on the layer, compare the result with the expected map, and record the verification decision.

## Expected result

A Working verified expression or workflow that returns Low below 5,000, Medium from 5,000 through 10,000, High above 10,000, and Unknown for null.

## Verification

Run the final expression on the layer. Use the non-destructive expression-preview method above to prove all four boundaries and null behavior even though the six supplied records do not contain every test value. Explain every condition in plain language.

## Common mistakes

Using `<= 5000` for Low; omitting null handling; using a nonexistent field; saving the result as a number instead of text; accepting an expression only because it runs.

## Human validation

The analyst confirms that the classification rule has an approved planning basis before reusing it beyond training.
