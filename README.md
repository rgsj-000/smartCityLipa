# Lipa City AI + GIS Training Package

This repository supports the five AI-assigned slots in the official GIS Application for Smart Cities training. It is a practical companion to the main QGIS sessions. It does not replace the trainers' lessons on GIS fundamentals, CRS, cleaning, digitizing, map design, spatial analysis, raster analysis, mobile GIS, governance, or the capstone.

> **AI assists. QGIS verifies. People decide.**

## Companion training materials

The master presentation, five participant worksheets, prompt cards, verification checklist, Smart City Canvas, facilitator guide, PDFs, and expected-output resources are available in the [Google Drive training folder](https://drive.google.com/drive/folders/1h8H1GGmUsXGz59zbLgb9nzG1d8mDTq7g).

## Five-session learning journey

| Activity | Official slot | Duration | Participant output |
|---|---|---:|---|
| ACT01 Understanding Data | Day 1, 11:15 AM | 45 min | Validated data dictionary |
| ACT02 QGIS Assistant | Day 1, 4:30 PM | 30 min | Working verified expression or workflow |
| ACT03 Analysis Assistant | Day 2, 2:00 PM | 45 min | GIS analysis plan |
| ACT04 GIS QA and Documentation | Day 2, 4:00 PM | 45 min | Metadata and QA sheet |
| ACT05 GIS Decision Support | Day 3, 10:15 AM | 60 min | AI-assisted GIS report |

## Requirements

Use QGIS 3.34 LTR or a later QGIS 3 release. No plugin is required. An AI service is optional because the facilitator kit includes offline response samples.

Recommended setup:

1. A computer with QGIS installed
2. A spreadsheet or document editor
3. Internet access for the live AI demonstration, when available
4. A projector for the facilitator

## Training data

All supplied data are synthetic. The six training barangays, facilities, roads, hazard polygons, values, and outputs do not represent official Lipa City records. Do not use them for operational decisions.

The project uses EPSG:32651, WGS 84 / UTM zone 51N. The layers are stored in `data/processed/lipa_training.gpkg`:

| Layer | Features | Purpose |
|---|---:|---|
| barangays | 6 | Population attributes and classification |
| facilities | 10 | Facility location and status examples |
| roads | 5 | Accessibility discussion |
| flood_hazard | 2 | Moderate and high synthetic hazard areas |

## Start the workshop

1. Download or clone the repository.
2. Keep the folder structure unchanged.
3. Open `qgis/Lipa_AI_GIS_Training.qgz`.
4. Confirm that four layers appear and the project CRS is EPSG:32651.
5. Apply the matching `.qml` file from `qgis/styles` if a layer style does not load.
6. Open the workflow for the current activity.

## Folder structure

```text
repository root/
  data/raw/                 CSV source used in the joining example
  data/processed/           GeoPackage used by the QGIS project
  data/reference/           Data dictionary and GeoJSON copy
  qgis/                     QGIS project and reusable styles
  outputs/screenshots/      Expected map outputs
  outputs/expected_results.json  Machine-readable ACT02 and ACT05 checks
  scripts/                  Expected-output regeneration script
  workflows/                Five time-boxed activity workflows and expressions
  prompts/                  GIS prompt library
  facilitator/answer_keys/  Teaching keys for all five activities
  facilitator/offline_ai_samples/  Pre-generated responses for offline delivery
  docs/                     Package documentation
```

## Activity sequence

ACT01 starts with fields and sample values. Participants use AI to draft possible meanings and data-quality questions, then validate the draft against the supplied dictionary.

ACT02 uses AI to explain and improve a QGIS Field Calculator expression. Participants test boundary and null cases before accepting the expression.

ACT03 starts with an LGU decision question. Participants evaluate an AI-proposed analysis plan and reject unsupported thresholds or spatial assumptions.

ACT04 converts rough processing notes into metadata and QA documentation. Participants must supply real provenance and must reject invented source details.

ACT05 uses verified QGIS facts to draft a short decision-support report. Participants separate observation, interpretation, limitation, and possible action.

## Reproduce expected results

Run `python scripts/generate_expected_outputs.py` from the repository root to rebuild `outputs/expected_results.json` and `outputs/screenshots/ACT05_01_Decision_Support_Map.png` from the supplied GeoPackage. The ACT05 map reports direct flood-hazard intersections only. It does not assign priority, risk, damage, urgency, or an operational action.

## Offline delivery

If internet access fails, open the matching file in `facilitator/offline_ai_samples`. Read the user prompt first, let participants predict the answer, then reveal the saved response. Participants still complete the QGIS verification and written output. Do not skip verification because the response is pre-generated.

## Common setup problems

### Layers show a red exclamation mark

Keep the QGIS project and `data` folder in their original relative positions. If needed, right-click the broken layer, choose Change Data Source, and select the matching table in `data/processed/lipa_training.gpkg`.

### Text fields become numbers

Import `BRGY_CODE` as text. A geographic identifier is not a quantity and should not be calculated as a number.

### Areas or distances look wrong

Confirm that the project and layer CRS are EPSG:32651 before calculating metric distance or area.

### AI gives a different expression

Different syntax may be acceptable if it uses existing fields, handles nulls, produces the required categories, and passes test records. The participant must explain the expression.

## Maintenance

Update `VERSION` and `training_manifest.json` together. When a canonical field or filename changes, update the QGIS project, workflow, worksheet, answer key, prompt sample, screenshot, and facilitator guide in the same release. Record the change in the repository history.

## License and attribution

Training materials use CC BY 4.0. The synthetic dataset has no external data source. Cite the training package when adapting the materials and replace synthetic values with approved sources before real use.
