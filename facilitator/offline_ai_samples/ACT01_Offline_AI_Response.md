# ACT01 Offline AI Response

## User prompt

Review fields BRGY_CODE, BRGY_NAME, POP_TOTAL, HH_COUNT, AREA_KM2, POP_DENS, and POP_CLASS. Draft meanings, types, units, and quality questions. Mark uncertainty and do not invent official definitions.

## AI response

| Field | Possible meaning | Type | Unit | Quality question | Confidence |
|---|---|---|---|---|---|
| BRGY_CODE | Barangay identifier | Text | None | Unique and complete? | High |
| BRGY_NAME | Barangay name | Text | None | Standard spelling? | High |
| POP_TOTAL | Total population | Integer | Persons | Which reference date? | Medium |
| HH_COUNT | Household count | Integer | Households | Same reference date as population? | Medium |
| AREA_KM2 | Polygon area | Decimal | km² | Calculated in a projected CRS? | Medium |
| POP_DENS | Population density | Decimal | Persons per km² | Equal to POP_TOTAL / AREA_KM2? | Medium |
| POP_CLASS | Population category | Text | None | What thresholds and authority define it? | Low |

## What is correct

The likely data types and quality questions are reasonable. The response correctly asks for source dates, CRS, and classification basis.

## What needs verification

The exact official meanings, population reference date, allowed values, and responsible office remain unconfirmed.

## Potential errors

High confidence still does not make the definition official. `BRGY_CODE` may use another coding standard in real data.

## Facilitator explanation

Ask participants to compare every row with the supplied dictionary and label its status. Emphasize that AI inferred structure from names but did not supply provenance.

## Improved prompt

Add sample values and ask AI to separate “inferred from field name” from “confirmed by supplied documentation.”
