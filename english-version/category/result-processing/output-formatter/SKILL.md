---
name: output-formatter
description: >-
  Integrate agent output results into structured final output, support multiple formats. Suitable for integrating analysis reports, generating structured reports
license: MIT
---

# Output Formatting Expert

## Functionality

Integrate output results from various agents into structured final output, supporting multiple output formats.

## Use Cases

- Integrate analysis results from multiple agents, generate unified structured reports.
- Convert complex data into multiple easy-to-read formats such as Markdown, JSON, HTML, plain text.
- Batch process large numbers of agent outputs, ensure format consistency and readability.
- Automate report generation process, improve work efficiency.

## Core Capabilities

- **Result Integration**: Efficiently integrate all agent output results, ensure data integrity.
- **Multi-Format Output**: Support multiple common formats such as Markdown, JSON, HTML, plain text, meeting different needs.
- **Structured Display**: Provide clear hierarchy and unified format style, improve readability.
- **Batch Processing Support**: Capable of batch processing multiple agent results, achieving automated formatting.
- **Error Handling**: Properly handle input data anomalies, ensure output stability and reliability.

## Core Steps

```
Receive agent output results
    ↓
Format according to specified output format
    ↓
Integrate all result data
    ↓
Generate structured final output
    ↓
Return formatted results
```

## Input Requirements

- **Agent Output Results**: Output data from various agents to be integrated (JSON, Markdown, Text, etc.).
- **Target Output Format** (optional): Specify final output format (such as Markdown, JSON, HTML, Text). Default is Markdown.
- **Structuring Requirements** (optional): Specific output structure templates or field definitions.

## Output Format

Provide structured final results according to specified output format. For example, in Markdown format, may contain the following content:

```
# Comprehensive Report Title

## Story Outline
[Complete story outline content]

## Major Plot Points
- Plot point 1: [Description]
- Plot point 2: [Description]

## Mind Map
![Mind Map](Image URL)
[Mind map edit link]

## Detailed Plot Points
### Plot Point 1
[Detailed description]

## Metadata Information
- Creation Date: [Date]
- Report Version: [Version number]
```

## Constraints

- Input data must be in parseable format to correctly extract information.
- Strictly follow specified output format requirements to ensure result standardization.
- Avoid introducing irrelevant information or hallucinations in output.

## Resources

- [examples.md](references/examples.md)
