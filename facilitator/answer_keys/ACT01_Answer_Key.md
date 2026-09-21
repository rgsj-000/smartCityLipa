# ACT01 Answer Key: Understanding Data

## Expected procedure

Participants inspect the CSV before prompting. A strong prompt names the fields, provides sample values, requests confidence and quality questions, and prohibits invented official definitions. Participants compare the AI draft with `data_dictionary.csv` and mark every row.

## Expected result

`BRGY_CODE` remains Text because it identifies a location. `POP_TOTAL` and `HH_COUNT` are whole-number counts. `AREA_KM2` is decimal area in square kilometres. `POP_DENS` is decimal persons per square kilometre. `POP_CLASS` is a controlled text result created from a training rule.

## Verification

Ask participants to show the source that confirms each definition. A correct answer may use different wording, but it must preserve data type, unit, allowed values, and uncertainty. Definitions based only on field-name inference remain Needs Revision or Unknown.

## Common mistakes

Calling `BRGY_CODE` an integer; claiming the population year is 2025 when no year field exists; stating that the field list is official; omitting the denominator unit for density; copying AI text without status marks.

## Human validation

The data owner determines the official definition, source, update cycle, and valid-value rules. The participant must be able to name what AI could not verify.

## Acceptable alternatives

Participants may add columns for nullable, uniqueness, domain owner, or update frequency. They may use Confirmed, Revise, and Unknown or equivalent labels.

## Discussion questions

Which field sounded obvious but still required confirmation? What harm could follow from misreading an identifier or unit? Which quality check should happen before a join?

## Evidence of understanding

The participant challenges at least one AI inference, preserves codes as text, states units, and records a concrete validation question.
