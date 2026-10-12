---
name: novel-truncator
description: >-
  Intelligently truncate text while preserving content integrity. Suitable for novel text preprocessing, ensuring text does not exceed specified length limits
license: MIT
---

# Text Truncator Tool (Novel Edition)

## Functionality

Receive text content and maximum length limit, intelligently truncate text while preserving content integrity.

## Usage Scenarios

- Preprocess long novel text to meet length limits
- Extract text segments without compromising semantic integrity
- Ensure text input to other agents does not exceed their processing capacity

## Truncation Principles

1. **Prioritize Sentence Endings**: Break at periods, question marks, exclamation points
2. **Next Paragraph Endings**: Break at spaces, line breaks
3. **Finally Specified Length**: Ensure not exceeding set maximum length limit

## Input Requirements

- **Text Content**: Original text to be truncated (string)
- **Maximum Length Limit**: Target maximum character count for text (integer)
- **Truncation Marker** (optional): String to identify text truncation location, such as "[...]"

## Output Format

```
[Text Truncation Report]

Original Length: [character count]
Truncated Length: [character count]
Truncation Position: [position description, such as: at period in sentence X]

Truncated Text:
[text content]
```

## Constraints

- Truncation process should maximally preserve original text's semantic and contextual integrity
- Strictly adhere to maximum length limit
- Avoid truncating in the middle of words

## Resources

- [examples.md](references/examples.md)
