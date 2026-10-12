---
name: novel-evaluator
description: >-
  Score a story from the provided text only (market potential, originality, highlights).
  Use for manuscript first-pass screening without web research. For hotness, author
  track record, or rights diligence, use ip-evaluator instead.
license: MIT
---

# Novel Text Evaluator (First Pass)

Score using **only the user-provided text**. No web search. No external sales/hotness claims.

## vs ip-evaluator

| | novel-evaluator | ip-evaluator |
|--|--|--|
| Sources | Given text only | Text + public web info |
| Use | Anonymous sample screening | Rights / greenlight diligence |

## Scoring bands

- 8.5+: excellent (rare; justify strictly)
- 8.0–8.4: strong, needs polish
- 7.5–7.9: average
- ≤7.4: weak

Scores to one decimal place. End with an information-boundary note.

## Resources

- [guide.md](references/guide.md)
- [examples.md](references/examples.md)
