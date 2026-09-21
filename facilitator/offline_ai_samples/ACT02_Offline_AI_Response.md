# ACT02 Offline AI Response

## User prompt

Create a QGIS 3.34 expression for POP_CLASS from POP_TOTAL. Low is below 5,000, Medium is 5,000 through 10,000, High is above 10,000, and null is Unknown.

## AI response

```qgis
CASE
  WHEN "POP_TOTAL" IS NULL THEN 'Unknown'
  WHEN "POP_TOTAL" < 5000 THEN 'Low'
  WHEN "POP_TOTAL" <= 10000 THEN 'Medium'
  ELSE 'High'
END
```

Test 4,999, 5,000, 10,000, 10,001, and null through the QGIS expression preview. Temporarily substitute each literal for every `POP_TOTAL` reference, read the preview result, and do not save the literal tests.

## What is correct

The expression uses the existing field, matches the stated boundaries, returns text, and handles null explicitly.

## What needs verification

Run it in QGIS and inspect records. Confirm that the real planning office approves any classification used beyond training.

## Potential errors

An AI response using `<= 5000` for Low would misclassify the boundary. Curly quotes copied from formatted text can also cause syntax errors.

## Facilitator explanation

Show the known bad expression first. Ask participants to predict the result for 5,000 and null before revealing the correction.

## Improved prompt

Require QGIS version, exact field name, output type, boundary tests, null behavior, and a line-by-line explanation.
