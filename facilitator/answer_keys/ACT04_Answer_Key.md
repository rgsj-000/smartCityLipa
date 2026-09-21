# ACT04 Answer Key: GIS QA and Documentation

## Expected procedure

Participants write rough processing notes first, then ask AI to organize them. They compare the draft with the QGIS project and source files, replace invented details with Unknown, and assign responsibility.

## Expected result

The sheet records a clear title, synthetic Lipa-style training coverage, EPSG:32651, actual filenames, processing steps, validation questions, limitations, author or responsible person, update requirement, and Draft or Verified status.

## Verification

Open layer properties to confirm CRS and source. Compare layer and field names with the project. Re-run one calculation or inspect one intermediate table. Confirm the source date only if the source provides it.

## Common mistakes

Accepting an invented government office, collection method, accuracy statement, or update cycle; omitting joins and field calculations; using “validated” without recording the check; documenting only the final map rather than the processing chain.

## Human validation

The analyst signs the process record. The data owner confirms source, date, limitations, and update responsibility.

## Acceptable alternatives

A processing model log, QGIS history export, structured spreadsheet, or metadata form is acceptable if it captures the same information and links to source files.

## Discussion questions

Which metadata fields can AI organize but never confirm? What would prevent a colleague from reproducing this result? When should the output return to Draft status?

## Evidence of understanding

The participant finds and removes at least one unsupported detail, records a limitation, and names a reproducibility check.
