---
name: character-profile
description: >-
  Analyze story text and generate detailed character profiles. Use when building
  cast bibles, actor references, or character sheets; triggers: character profile,
  character bible, persona analysis.
license: MIT
---

# Character Profile Expert

Extract character information from story text and produce structured profiles. Invent nothing that is not supported by the text.

## Steps

1. Read the text and mark all characters with actions, dialogue, and relationships
2. Select protagonists and important supporting characters
3. Extract basics, personality, background, relationships, narrative function
4. Write profiles; mark gaps as "not stated in text"

## Hard constraints

- Usually at least 8 important characters (or all available, with explanation)
- 300–500 words per profile
- Stick to the source text; no fabrication
- Third-person objective voice even if the source is first-person

## Output format

```
【Character Profile: Name】

1. Basics — name / age / role / appearance
2. Personality — traits / behavior / speech
3. Background — family / growth / key events
4. Relationships — with major characters
5. Narrative role — function / plot drive / theme / desire & obstacle
```

## Resources

- [guide.md](references/guide.md)
- [examples.md](references/examples.md)
