---
name: text-splitter
description: >-
  Split text into specified-sized chunks while maintaining semantic integrity. Suitable for long text batch processing, dividing text into processable segments
license: MIT
---

# Text Splitter Tool

## Functionality

Split text into specified-sized chunks while maintaining semantic integrity, facilitating subsequent batch processing and analysis.

## Usage Scenarios

- Process extra-long text by splitting it into agent-processable segments
- Perform text preprocessing to provide standardized input for subsequent content analysis, summarization, or evaluation tasks
- Optimize text processing workflows to ensure each processing unit is controllable in size and semantically complete

## Core Capabilities

- **Semantic Integrity Priority**: When splitting, avoid truncating sentences or paragraphs; prioritize splitting at natural boundaries (periods, line breaks) to ensure semantic integrity of each chunk
- **Preserve Original Format**: During splitting, preserve the original format and structure of text, such as Markdown, HTML tags, etc.
- **Precise Chunk Size Control**: Strictly split according to specified size limits, ensuring each text chunk does not exceed the preset maximum length
- **Multiple Splitting Strategies**: Support various splitting strategies based on character count, token count, paragraph count, or specific delimiters

## Input Requirements

- **Text Content**: Original text to be split
- **Chunk Size Limit**: Maximum length of each text chunk (recommend providing character count or token count)
- **Splitting Strategy** (optional): Specify preferred splitting strategy, such as split by sentence, split by paragraph, split by specific delimiter, etc.

## Output Format

```
[Text Splitting Report]

- Original text length: [integer] words/tokens
- Target chunk size: [integer] words/tokens
- Actual number of chunks: [integer] chunks

### Splitting Results
- Chunk 1 (length: [integer] words/tokens): "[content preview...]"
- Chunk 2 (length: [integer] words/tokens): "[content preview...]"
- Chunk 3 (length: [integer] words/tokens): "[content preview...]"
...
```

## Constraints

- Splitting results must strictly comply with specified chunk size limits
- Ensure maximum preservation of text semantic integrity during splitting
- Output format must be structured, clearly displaying content and length of each text chunk
- Avoid introducing any extra information or explanations in output; only provide splitting results

## Resources

- [examples.md](references/examples.md)
