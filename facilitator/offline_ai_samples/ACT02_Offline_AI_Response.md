# ACT02 Offline AI Response

## User prompt

Create a QGIS 3.34 Field Calculator expression for a text field named `population_band_synth` using only `population_2024`. For this training exercise, Low is below 5,000, Medium is 5,000 through 10,000, High is above 10,000, and null is Unknown. Include boundary tests and do not present the bands as an official classification.

## AI response

```qgis
CASE
  WHEN "population_2024" IS NULL THEN 'Unknown'
  WHEN "population_2024" < 5000 THEN 'Low'
  WHEN "population_2024" <= 10000 THEN 'Medium'
  ELSE 'High'
END
```

Test 4,999, 5,000, 10,000, 10,001, and null through the QGIS expression preview. Temporarily substitute each literal for every `population_2024` reference, read the preview result, and do not save the literal tests.

## What is correct

The expression uses the ACT01 population field, matches the stated boundaries, returns text, and handles null explicitly.

## What needs verification

Run it in QGIS on an editable working copy of the ACT01 barangay profile. Inspect representative records and confirm the output field is text. Keep the raw CSV unchanged.

## Potential errors

An AI response using `<= 5000` for Low would misclassify the boundary. Using the old field name `POP_TOTAL`, curly quotation marks, or a numeric output field would also be incorrect for this activity.

## Facilitator explanation

Show the known bad expression first. Ask participants to predict the result for 5,000 and null before revealing the correction. Reinforce that the population bands are training rules only.

## Improved prompt

Require the exact ACT01 field name, output field, QGIS version, output type, boundary tests, null behavior, and a line by line explanation. State that the threshold bands are exercise rules rather than official classifications.
