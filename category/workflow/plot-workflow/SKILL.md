---
name: plot-workflow
description: >-
  编排大情节点与详细情节点一键生成：预处理、提取、细化、格式化。
  适用于需要完整情节骨架与逐点展开时；提到情节工作流、情节点流水线时使用。
license: MIT
---

# 情节工作流编排器

按固定调用链生成「大情节点 + 详细情节点」并格式化输出。

## 调用链（必须按序）

| 步骤 | Skill | 作用 |
|------|-------|------|
| 1 | `text-truncator` / `text-splitter` | 长文本预处理（按需） |
| 2 | `plot-keypoints` | 提取大情节点（阶段骨架） |
| 3 | `detailed-plot-analyzer` | 将大情节点展开为详细情节点 |
| 4 | `output-formatter` | 统一格式、编号与可读性 |

若无法真正调用子 skill：在同一次回复中依次遵循各 skill 的硬约束完成，并标注步骤。

## 编排规则

- 先骨架后细节：未完成 `plot-keypoints` 不得跳进详细展开
- 详细情节点必须挂在对应大情节点下，禁止悬空
- 情节点表述忠实原文；大情节点单条通常 ≤150 字（遵循 `plot-keypoints`）
- 异常时返回已完成层级 + 失败原因，提供降级结果

## 输入

- 故事文本或故事大纲
- 可选：目标集数/篇幅、关注的主线

## 输出格式

```
【工作流执行报告】

一、执行状态
- 步骤完成情况（1–4）/ 失败点（如有）

二、大情节点
[plot-keypoints 产出]

三、详细情节点
[按大情节点分组的 detailed-plot-analyzer 产出]

四、格式化终稿
[output-formatter 产出]
```

## 参考资料

- [examples.md](references/examples.md)
