---
name: mind-map-generator
description: >-
  Call the generateTreeMind tool to create visual mind maps, returning image URL and edit link. Suitable for story structure visualization, plot relationship graph display
license: MIT
---

# Mind Map Generator Expert

## Functionality

Call the `generateTreeMind` tool to create visual mind maps and provide image URLs and edit links.

## Usage Scenarios

- **Story Structure Visualization**: Convert complex story outlines, plot points, or character relationships into intuitive mind maps to help users quickly understand and organize
- **Plot Relationship Graph Display**: Show character relationships and event development patterns graphically for analysis and design
- **Creative Idea Organization**: Assist creators in organizing and diverging ideas, organizing scattered thoughts into structured mind maps
- **Team Collaboration and Sharing**: Generate editable mind map links for convenient team collaboration and iteration

## Core Capabilities

- **Mind Map Generation**: Call `generateTreeMind` API to convert text content (outlines, lists, free text) into structured mind maps
- **Visual Display**: Provide generated mind map image URLs supporting online preview, download, and embedding
- **Edit Link Provision**: Provide online edit links for generated mind maps, allowing users to make secondary modifications and customizations
- **API Call Management**: Effectively manage `generateTreeMind` API requests and responses, ensuring stability and fault tolerance

## Input Requirements

- **Content to Convert**: Text content for mind map generation (story outlines, character lists, script segments)
- **Mind Map Structure** (optional): Specify hierarchical relationships or specific node connection methods for the mind map
- **Style Settings** (optional): Define visual styles such as colors, fonts, and layout for the mind map

## Output Format

```json
{
  "pic": "[mind map image URL]",
  "jump_link": "[mind map edit link]",
  "data": "[original data, typically JSON format mind map data]",
  "log_id": "[log ID]"
}
```

## Constraints

- Ensure stability and success rate of `generateTreeMind` API calls
- Handle various states in API responses, including success, failure, or error messages
- Mind map generation content must accurately reflect the structure and semantics of input text
- Returned image URLs and edit links must be valid and accessible
- Do not introduce any information unrelated to mind map generation in output

## Resources

- [examples.md](references/examples.md)
