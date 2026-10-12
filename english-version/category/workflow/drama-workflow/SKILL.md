---
name: drama-workflow
description: >-
  Orchestrate long-form plot-point and dramatic-function analysis: preprocess,
  segment analysis, merge. Use for novels/scripts needing a structured drama report.
license: MIT
---

# Drama Analysis Workflow

## Call chain (in order)

| Step | Skill | Role |
|------|-------|------|
| 1 | `text-truncator` | Semantic truncation |
| 2 | `text-splitter` | Segment by chapter/scene |
| 3 | `drama-analyzer` | Plot points + dramatic function (parallel OK) |
| 4 | `result-integrator` | Dedupe, timeline align, final report |

If sub-skills cannot be invoked, simulate each role with its constraints and label step outputs.

## Rules

- Isolate segment context; do not leak unproven facts across segments
- Inherit `drama-analyzer` limits: ≤100 words/point, ≥5 points, no Arabic numbering, no fabrication
- On failure: degrade with completed segments, never fake completeness

## Resources

- [examples.md](references/examples.md)
