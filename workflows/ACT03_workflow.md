# ACT03 Workflow: Analysis Assistant

**Official slot:** Day 2, 2:00 PM to 2:45 PM

**Required output:** GIS analysis plan

## Objective

Translate an LGU decision question into a defensible sequence of data requirements, GIS operations, intermediate outputs, checks, assumptions, and limitations.

## Scenario

The team asks which synthetic training barangays may require priority evacuation planning based on flood exposure, population, and access to evacuation facilities.

## Required files

All layers in `qgis/Lipa_AI_GIS_Training.qgz` and the ACT03 prompt.

## Timed procedure

1. **Decision question, 7 minutes:** Define what the analysis can and cannot answer.
2. **AI plan demonstration, 8 minutes:** Ask AI for a workflow without supplying a distance threshold.
3. **Group plan, 15 minutes:** Complete data, field, operation, output, validation, and limitation columns.
4. **Critique, 10 minutes:** Reject invented thresholds, straight-line access assumptions, or unsupported priority scores.
5. **Consolidation, 5 minutes:** Save the plan and identify the required policy decision.

## Expected result

A GIS analysis plan that begins with source and CRS checks, uses spatial intersection for exposure, identifies relevant facilities, treats road accessibility as a separate question, and records missing information.

## Verification

Confirm that every proposed operation has an available input and produces an output used by the next step. Check that the plan distinguishes exposure, accessibility, capacity, and operational readiness.

## Common mistakes

Choosing a one-kilometre buffer without a basis; treating intersection as proof of damage; assuming all roads are passable; using capacity without occupancy or condition data; combining unlike indicators without an approved weighting method.

## Human validation

DRRM, planning, engineering, facility managers, and other responsible offices supply policy thresholds and interpret operational meaning.
