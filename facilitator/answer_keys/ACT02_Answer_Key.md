# ACT02 Answer Key: QGIS Assistant

## Expected procedure

Participants prompt for a QGIS 3.34 Field Calculator expression using `POP_TOTAL`, create or update text field `POP_CLASS`, run the expression, inspect representative records, then explain the conditions.

## Correct expression

```qgis
CASE
  WHEN "POP_TOTAL" IS NULL THEN 'Unknown'
  WHEN "POP_TOTAL" < 5000 THEN 'Low'
  WHEN "POP_TOTAL" <= 10000 THEN 'Medium'
  ELSE 'High'
END
```

## Expected result

Amihan is Low. Banaba, Ilang-Ilang, and Maligaya are Medium. Duhat and Sampaguita are High. A test null is Unknown.

## Verification

Use the QGIS expression preview and temporarily replace every `POP_TOTAL` reference with 4,999, 5,000, 10,000, 10,001, and `NULL`, one at a time. Read the preview result and do not save the literal tests. Then run the final field-based expression on the layer, confirm that the output field is text, and ask a participant to explain why the condition sequence matters.

## Common mistakes

The known bad expression uses `<= 5000` for Low and lacks null handling. Other errors include misspelling `POP_TOTAL`, using curly quotation marks, creating a numeric output field, or assuming an expression is correct because QGIS accepts the syntax.

## Human validation

The GIS analyst validates the implementation. The responsible planning office supplies any real classification rule.

## Acceptable alternatives

Nested `if` is acceptable if the boundaries and null case match. A rule-based renderer can provide the same visible result, but the activity requires a saved or documented expression.

## Discussion questions

What test value exposes the boundary error? What happens if population is null? Why should a planning threshold have a documented basis?

## Evidence of understanding

The participant can predict the result before running QGIS, detect the flawed boundary, and explain why null requires an explicit branch.
