# ACT04 Offline AI Response

## User prompt

Turn these notes into metadata and QA documentation: loaded barangays and flood_hazard, checked EPSG:32651, joined population using BRGY_CODE, intersected polygons, calculated summary fields, and exported a map. Use Unknown when a fact is missing.

## AI response

| Item | Draft entry |
|---|---|
| Dataset title | Synthetic Flood Exposure Screening |
| Geographic coverage | Synthetic Lipa-style training area |
| CRS | EPSG:32651 |
| Source | Unknown; confirm from source files |
| Source date | Unknown |
| Processing | Load, CRS check, population join, intersection, summary calculation, map export |
| Validation | Check unique BRGY_CODE, unmatched joins, geometry validity, feature counts, and calculation logic |
| Limitations | No verified source date, flood depth, road condition, facility condition, or operational threshold |
| Responsible person | Unknown |
| Status | Draft |

## What is correct

The response preserves known processing steps and leaves missing provenance unknown.

## What needs verification

Confirm filenames, field calculations, output path, analyst, review date, and source details from the actual project.

## Potential errors

AI might invent a city office, collection method, accuracy figure, or annual update cycle when the notes do not provide them.

## Facilitator explanation

Documentation can look polished while still being false. Ask participants to underline every entry that has a traceable source.

## Improved prompt

Require a source or evidence column and prohibit completion of any field whose source is absent.
