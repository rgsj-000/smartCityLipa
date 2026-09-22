# ACT01 Comprehensive Datasets

## Purpose

These datasets support **ACT01 Understanding Data**, where participants inspect unfamiliar LGU-style data, draft field descriptions and data-quality questions with AI assistance, and validate those suggestions before producing a data dictionary.

The package is intentionally broader than the six-barangay synthetic QGIS project used elsewhere in the workshop. ACT01 is designed for exploration, profiling, QA, joins, and discussion before participants move into more advanced GIS analysis.

## Dataset package

| File | Records | Main use |
|---|---:|---|
| `data/raw/ACT01_barangay_profile_RAW.csv` | 72 barangays | Primary participant dataset with controlled data-quality issues |
| `data/reference/ACT01_barangay_profile_REFERENCE_CLEAN.csv` | 72 barangays | Facilitator/reference version with normalized training values |
| `data/raw/ACT01_facilities_SYNTHETIC.csv` | 192 facilities | Point-data exploration, categories, filtering, joins, and coordinate import |
| `data/raw/ACT01_service_requests_SYNTHETIC.csv` | 600 requests | Tabular exploration, dates, categories, service status, response time, and citizen feedback |
| `data/reference/ACT01_data_dictionary.csv` | 56 field definitions | Field meaning, type, unit/format, domain, and source-status reference |
| `facilitator/ACT01_facilitator_issue_key.csv` | 13 seeded QA issues | Facilitator-only checking guide for the RAW barangay profile |

## Source and data status

The following fields in the barangay profile are based on the Philippine Statistics Authority PSGC City of Lipa listing and its 2024 POPCEN values:

`psgc_10_digit`

`correspondence_code`

`barangay_name`

`urban_rural`

`population_2024`

PSA reference: https://psa.gov.ph/classification/psgc/barangays/0401014000

All fields ending in `_synth` are synthetic training values. The facility records, facility coordinates, and service-request records are also synthetic and are not authoritative LGU records. They must not be used for operational planning or official decisions.

## Suggested participant flow

1. Load `ACT01_barangay_profile_RAW.csv` and determine what one row represents.
2. Classify fields as identifiers, categories, counts, percentages, dates, measurements, or derived values.
3. Identify missing values, inconsistent categories, impossible values, suspicious values, formatting issues, and fields that need controlled vocabularies.
4. Ask AI to propose field definitions and QA questions using only the supplied field names and sample values.
5. Verify AI suggestions against the actual dataset, the reference dictionary, and local/domain knowledge.
6. Load `ACT01_facilities_SYNTHETIC.csv` as delimited text using longitude and latitude with **EPSG:4326 / WGS 84**.
7. Explore filters, sorting, categories, summaries, and possible barangay-name joins.
8. Use `ACT01_service_requests_SYNTHETIC.csv` to explore service categories, channels, priorities, status, response time, and temporal patterns.
9. Produce a participant data dictionary and short QA findings sheet.

## Controlled QA issues

The RAW barangay profile deliberately includes a small number of training errors and suspicious values. Participants should discover and describe them instead of being told the answers in advance. The facilitator key is stored separately in `facilitator/ACT01_facilitator_issue_key.csv`.

Do not automatically repair a suspicious value merely because AI recommends a correction. The intended workflow is:

**Problem → Data → AI Assistance → Verification → Human Interpretation → Decision**
