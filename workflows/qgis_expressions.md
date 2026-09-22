# Reusable QGIS Expressions

These expressions use the canonical training fields for their respective activities. Run them in QGIS, inspect sample records, and explain the result before saving an output.

## ACT02 population band with null handling

ACT02 continues from `data/raw/ACT01_barangay_profile_RAW.csv`. Work on an editable QGIS copy of the ACT01 profile and keep the raw CSV unchanged.

Create a text field named `population_band_synth`.

```qgis
CASE
  WHEN "population_2024" IS NULL THEN 'Unknown'
  WHEN "population_2024" < 5000 THEN 'Low'
  WHEN "population_2024" <= 10000 THEN 'Medium'
  ELSE 'High'
END
```

Boundary checks: 4,999 is Low; 5,000 and 10,000 are Medium; 10,001 is High; null is Unknown.

Non-destructive QGIS test: paste the expression into the expression preview, temporarily replace every `"population_2024"` reference with `4999`, `5000`, `10000`, `10001`, or `NULL`, and read the preview result for each test. Do not save the literal test expressions to the layer.

These thresholds are training rules only and are not an official planning classification.

## Population density

The following expression belongs to the reusable synthetic QGIS project used by later activities. Create a decimal field named `POP_DENS`.

```qgis
CASE
  WHEN coalesce("AREA_KM2", 0) <= 0 THEN NULL
  ELSE round("POP_TOTAL" / "AREA_KM2", 1)
END
```

The guard prevents division by zero. Confirm that `AREA_KM2` uses square kilometres.

## Standardized facility status

```qgis
CASE
  WHEN trim(coalesce("STATUS", '')) = '' THEN 'Unknown'
  WHEN lower(trim("STATUS")) = 'operational' THEN 'Operational'
  WHEN lower(trim("STATUS")) = 'needs inspection' THEN 'Needs Inspection'
  ELSE 'Review'
END
```

Do not add a new status category without the data owner's approval.

## Join key check

```qgis
regexp_match("BRGY_CODE", '^SYN[0-9]{3}$')
```

This checks the synthetic format only. Real LGU codes require the official coding standard.

## Label with population

```qgis
"BRGY_NAME" || '\nPopulation: ' || format_number("POP_TOTAL", 0)
```

## Select facilities needing review

```qgis
"STATUS" = 'Needs Inspection'
```

## ACT02 known bad expression

```qgis
if("population_2024" <= 5000, 'Low', if("population_2024" <= 10000, 'Medium', 'High'))
```

This expression classifies 5,000 as Low, which conflicts with the ACT02 exercise rule. It also classifies null as High. The corrected `CASE` expression above resolves both problems.
