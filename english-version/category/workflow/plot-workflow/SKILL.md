---
name: plot-workflow
description: >-
  Orchestrate major plot points plus detailed beats: preprocess, extract, expand,
  format. Use when a full plot skeleton and beat sheet are needed.
license: MIT
---

# Plot Workflow Orchestrator

## Call chain (in order)

| Step | Skill | Role |
|------|-------|------|
| 1 | `text-truncator` / `text-splitter` | Preprocess as needed |
| 2 | `plot-keypoints` | Major plot points |
| 3 | `detailed-plot-analyzer` | Expand into detailed beats |
| 4 | `output-formatter` | Normalize final output |

Skeleton before detail. Detailed beats must attach to a major point.

## Resources

- [examples.md](references/examples.md)
