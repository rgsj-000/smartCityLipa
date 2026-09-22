# ACT02 Answer Key: QGIS Assistant

## Expected procedure

Participants continue from the ACT01 barangay profile. They use `population_2024`, create a text field named `population_band_synth`, run the expression on an editable QGIS working layer, inspect records, test boundaries and nulls, and explain the conditions.

If the ACT01 CSV is read only, save or export it as an editable working layer first. Keep the raw CSV unchanged.

## Correct expression

```qgis
CASE
  WHEN "population_2024" IS NULL THEN 'Unknown'
  WHEN "population_2024" < 5000 THEN 'Low'
  WHEN "population_2024" <= 10000 THEN 'Medium'
  ELSE 'High'
END
```

## Expected result

Adya at 2,144 is Low. Anilao at 5,019 is Medium. Latag at 9,230 is Medium. Balintawak at 19,063 is High. A test null is Unknown.

The bands are training rules only.

## Verification

In the QGIS expression preview, temporarily replace every `population_2024` reference with 4,999, 5,000, 10,000, 10,001, and `NULL`, one at a time. Read each preview result and do not save the literal tests. Then run the field based expression on the editable ACT01 working layer and confirm that `population_band_synth` is text.

## Common mistakes

Using `<= 5000` for Low, omitting null handling, using the old `POP_TOTAL` or `POP_CLASS` names, misspelling `population_2024`, creating a numeric output field, changing the raw CSV, or accepting an expression only because it runs.

## Human validation

The analyst validates the implementation. Any real classification used outside the exercise needs a documented basis from the appropriate office.

## Acceptable alternatives

Nested `if` is acceptable if the boundaries and null case match. A rule based renderer can provide the same visible grouping, but the activity requires a saved or documented expression or workflow.

## Discussion questions

What test value exposes the boundary error? What happens when `population_2024` is null? Why should a threshold have a documented basis?

## Evidence of understanding

The participant can predict the result before running QGIS, detect the flawed boundary, and explain why null requires an explicit branch.
