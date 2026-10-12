---
name: score-analyzer
description: >-
  Analyze multi-round evaluation result scoring data, calculate various metrics, calculate rating grades. Suitable for analyzing scoring trends, calculating S/A/B ratings
license: MIT
---

# Score Analysis Agent

## Functionality

Analyze scoring data from multiple evaluation rounds, calculate various scoring metrics, and calculate rating grades (S Strong Focus/A Suggested Focus/B Ordinary).

## Usage Scenarios

- Quickly grasp overall performance and trends of multi-round evaluation results
- Provide decision support for project approval and IP adaptation based on quantitative data
- Identify high-potential works for S/A/B grading
- Assist evaluators in analyzing scoring deviations to optimize evaluation processes

## Rating Grade Definitions

- **S Grade (Strong Focus)**: At least one 8.5 score or at least eight 8.0 scores accumulated
- **A Grade (Suggested Focus)**: At least five 8.0 scores accumulated
- **B Grade (Ordinary)**: Does not meet A Grade standards

## Statistical Metrics

- **Evaluation Count**: Total evaluation rounds
- **Valid Score Count**: Evaluation rounds with valid scoring data
- **First Score**: Record first evaluation score
- **Highest Score**: Record highest score among all evaluations
- **Lowest Score**: Record lowest score among all evaluations
- **Average Score**: Calculate average score of all evaluations
- **Trimmed Mean Score**: Average score after removing highest and lowest scores
- **High Score Statistics**: Count occurrences in each score range (8.5 and above, 8.0-8.4, etc.)

## Core Steps

```
Receive multi-round evaluation results
    ↓
Extract all scoring data
    ↓
Calculate various scoring metrics
    ↓
Calculate rating grades
    ↓
Generate comprehensive evaluation report
    ↓
Output structured results
```

## Input Requirements

- **Evaluation Results**: Structured text containing multi-round evaluation scoring data (recommend at least 10 evaluation results)
- **Scoring Dimensions**: Clear dimensions and standards for scoring
- **Special Requirements** (optional): Any specific statistical or analysis requirements

## Output Format

```
[Score Analysis Report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I. Evaluation Overview
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Evaluation Count: [count]
- Valid Scores: [count]
- Rating Grade: [S/A/B]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
II. Score Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- First Score: [score]
- Highest Score: [score]
- Lowest Score: [score]
- Average Score: [score]
- Trimmed Mean: [score]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
III. Score Sequence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [score]
2. [score]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IV. High Score Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 8.5 and above: [count]
- 8.0-8.4: [count]
- 7.5-7.9: [count]
- 7.4 and below: [count]
```

## Constraints

- Input evaluation data must contain clear scores for statistical analysis
- Report content must be objective and fair, based on data generation without subjective judgment
- Ensure calculation results are accurate

## Resources

- [examples.md](references/examples.md)
