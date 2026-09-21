# ACT01 Workflow: Understanding Data

**Official slot:** Day 1, 11:15 AM to 12:00 NN

**Required output:** Validated data dictionary

## Objective

Use AI to draft possible field descriptions and data-quality questions, then distinguish inference from confirmed LGU meaning.

## Scenario

Another office shared a GIS dataset with short field names but incomplete documentation. Before analysis, the receiving team must establish what each field means, which values are valid, and what remains unknown.

## Required files

`data/raw/population.csv` and `data/reference/data_dictionary.csv`

## Timed procedure

1. **Problem setup, 5 minutes:** Inspect the CSV headers and sample rows. List unclear fields.
2. **AI demonstration, 8 minutes:** Use the ACT01 prompt from the prompt library.
3. **Participant drafting, 12 minutes:** Produce possible meaning, type, unit, valid values, quality question, and confidence.
4. **Human validation, 12 minutes:** Compare the draft with the reference dictionary. Mark Confirmed, Needs Revision, or Unknown.
5. **Debrief and save, 8 minutes:** Record one field where AI inferred too much.

## Expected result

A Validated data dictionary that keeps `BRGY_CODE` as text, identifies units, records data-quality questions, and clearly separates confirmed definitions from AI guesses.

## Verification

Check each definition against `data_dictionary.csv`. Confirm that identifiers remain text, numeric units are stated, possible values match the source, and unsupported provenance remains Unknown.

## Common mistakes

Accepting a plausible field meaning without confirmation; converting a geographic code to a number; inventing a source year; treating a sample value list as a complete official code list.

## Human validation

The data owner approves official field meanings and allowed values. The participant remains responsible for documenting uncertainty.
