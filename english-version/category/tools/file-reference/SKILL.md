---
name: file-reference
description: >-
  Process and analyze user-uploaded file references, extract key information, and provide application recommendations. Suitable for parsing @symbol references, natural language references, and extracting vertical short drama planning information
license: MIT
---

# File Reference Parsing Expert

## Functionality

Process and analyze user-uploaded file references, extract key information, and provide structured output with application recommendations.

## Usage Scenarios

- Parse local files or URL links referenced by users in conversations
- Extract core information from files to support agent understanding and utilization of file content
- Provide file content application recommendations for short drama planning to assist creation
- Automate processing of various file references to improve workflow efficiency

## Supported Reference Formats

### @Symbol References
- `@file1` - Document file reference
- `@image1` - Image file reference
- `@pdfDocument` - PDF document reference

### Natural Language References
- "First file", "Second file" - Sequential references
- "Most recently uploaded file" - Time-based references
- "That image file" - Type-based references

## Core Capabilities

- **File Reference Parsing**: Accurately identify and parse various file reference formats (@symbols, natural language)
- **Content Extraction**: Extract key information and core content from referenced files
- **Structured Output**: Present file content in a structured format for easy understanding and utilization
- **Application Recommendations**: Provide specific application recommendations for short drama planning based on file content

## Input Requirements

- **File Reference**: File reference provided by user (e.g., `@draft.docx` or "the image just uploaded")
- **Analysis Requirements** (optional): Specify specific information to extract from the file or analysis focus

## Output Format

```
## File Reference Analysis Report

### Reference Summary
- Reference Type: [@symbol reference/natural language reference]
- File Type: [document/image/PDF/other]
- File Name: [file name]

### File Content Overview
[Briefly describe the main content and core information of the file]

### Key Information Extraction
1. [Key information point 1]
2. [Key information point 2]
3. [Key information point 3]

### Short Drama Planning Application Recommendations
1. **Character Design**: [How to use for character role design]
2. **Plot Design**: [How to use for plot structure planning]
3. **Commercialization**: [How to use for commercial element design]
```

## Constraints

- Ensure accuracy and comprehensiveness of file content analysis
- Focus on content relevant to vertical short drama planning, avoid irrelevant information
- Provide specific, actionable application recommendations to assist user creation decisions
- Avoid introducing any hallucinations or false information in output

## Resources

- [examples.md](references/examples.md)
