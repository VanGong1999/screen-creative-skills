---
name: result-integrator
description: >-
  Integrate multiple plot point analysis results into comprehensive reports, generating high-quality analysis through deduplication, classification, sorting, and summarization. Suitable for integrating multiple analysis sources, generating unified reports
license: MIT
---

# Result Integration Tool

## Functionality

Integrate multiple plot point analysis results into comprehensive reports, generating high-quality comprehensive analysis through deduplication, classification, sorting, and summarization.

## Use Cases

- Integrate plot point results from multiple analysis sources, generate unified comprehensive reports.
- Remove duplicate and redundant information, ensure report conciseness and accuracy.
- Provide structured plot point analysis summary for quick understanding of story core.
- Optimize report logical coherence, improve readability and professionalism.

## Integration Principles

1. **Deduplication**: Remove duplicate or similar plot points, ensure each plot point is unique.
2. **Classification**: Classify plot points by dramatic function, provide clear structured view.
3. **Sorting**: Arrange plot points in order of appearance in story, ensure timeline coherence.
4. **Summarization**: Provide overall dramatic structure analysis, give professional insights and recommendations.

## Core Steps

```
Receive multiple analysis results
    ↓
Identify and remove duplicate content
    ↓
Classify by dramatic function
    ↓
Sort by story order
    ↓
Generate overall analysis summary
    ↓
Output final comprehensive report
```

## Input Requirements

- **Plot Point Analysis Results**: Multiple plot point analysis reports or data from different agents.
- **Analysis Source Weights** (optional): Specify priority or weights of different analysis source results.

## Output Format

```
[Plot Point Integration Analysis Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Overall Analysis Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Overall dramatic structure analysis and professional insights]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Plot Point Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Plot Point]: [Description]
[Dramatic Function]: [Analysis]
- [Specifically describe function and impact of this plot point]

[Plot Point]: [Description]
[Dramatic Function]: [Analysis]
- [Specifically describe function and impact of this plot point]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Dramatic Structure Evaluation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Professional evaluation and improvement recommendations for integrated dramatic structure]
```

## Constraints

- Ensure all input plot point information is complete and parseable.
- Integration process must maintain objectivity, not introduce new subjective judgments.
- Report content must be logically coherent, easy to read and understand.
- Ensure final output report format is standardized and meets expected requirements.

## Resources

- [examples.md](references/examples.md)
