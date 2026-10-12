#!/usr/bin/env python3
"""Batch-clean SKILL.md files for cross-platform Agent Skills usability."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL_GLOBS = [
    ROOT / "category",
    ROOT / "english-version" / "category",
]

KEEP_FRONTMATTER = ("name", "description", "license")

VERSION_HEADERS = (
    "## 版本历史",
    "## Version History",
)


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unclosed frontmatter")
    meta = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5 :]
    return meta, body


def slim_frontmatter(meta: dict) -> dict:
    out = {}
    for key in KEEP_FRONTMATTER:
        if key in meta and meta[key] not in (None, "", []):
            out[key] = meta[key]
    if "license" not in out:
        out["license"] = "MIT"
    return out


def strip_version_history(body: str) -> str:
    for header in VERSION_HEADERS:
        idx = body.find(header)
        if idx != -1:
            body = body[:idx].rstrip() + "\n"
    return body


def fix_basedir_links(body: str) -> str:
    # `{baseDir}/references/foo.md` -> [foo.md](references/foo.md)
    body = re.sub(
        r"`?\{baseDir\}/references/([^`\s]+)`?",
        r"[\1](references/\1)",
        body,
    )
    body = re.sub(
        r"`?\{baseDir\}/([^`\s]+)`?",
        r"[\1](\1)",
        body,
    )
    return body


def normalize_resources(body: str, skill_dir: Path) -> str:
    """Collapse redundant 详细文档 / Detailed Documentation into Resources."""
    refs = skill_dir / "references"
    if not refs.is_dir():
        return body

    files = sorted(p.name for p in refs.glob("*.md"))
    if not files:
        return body

    is_en = "english-version" in str(skill_dir)
    header = "## Resources" if is_en else "## 参考资料"
    bullets = "\n".join(f"- [{name}](references/{name})" for name in files)
    block = f"{header}\n\n{bullets}\n"

    # Remove old resource-like sections (keep content before them)
    for h in (
        "## 详细文档",
        "## Detailed Documentation",
        "## 参考资料",
        "## Resources",
        "## 示例",
        "## Examples",
    ):
        # Only strip the purely pointer-style sections later; rebuild clean Resources at end
        pass

    # Drop trailing pointer sections that only point at references
    patterns = [
        r"\n## 详细文档\n[\s\S]*?(?=\n## |\Z)",
        r"\n## Detailed Documentation\n[\s\S]*?(?=\n## |\Z)",
        r"\n## 参考资料\n[\s\S]*?(?=\n## |\Z)",
        r"\n## Resources\n[\s\S]*?(?=\n## |\Z)",
    ]
    cleaned = body
    for pat in patterns:
        cleaned = re.sub(pat, "\n", cleaned)

    # If 示例/Examples only points to references without inline example, replace with Resources
    for h, label in (("## 示例", "示例"), ("## Examples", "Examples")):
        m = re.search(rf"\n{re.escape(h)}\n([\s\S]*?)(?=\n## |\Z)", cleaned)
        if not m:
            continue
        section = m.group(1).strip()
        if (
            "references/" in section
            or "{baseDir}" in section
            or re.search(r"请参见|See |see ", section)
        ) and "```" not in section:
            cleaned = cleaned[: m.start()] + cleaned[m.end() :]

    cleaned = cleaned.rstrip() + "\n\n" + block
    return cleaned


def dump_frontmatter(meta: dict) -> str:
    # Stable, readable YAML without sorting keys oddly
    lines = ["---"]
    for key in KEEP_FRONTMATTER:
        if key not in meta:
            continue
        val = meta[key]
        if key == "description" and isinstance(val, str) and (
            "\n" in val or len(val) > 100
        ):
            # fold long descriptions
            lines.append(f"{key}: >-")
            # keep as single folded paragraph
            wrapped = " ".join(val.split())
            lines.append(f"  {wrapped}")
        else:
            dumped = yaml.safe_dump(
                {key: val}, allow_unicode=True, default_flow_style=False
            ).strip()
            lines.append(dumped)
    lines.append("---")
    return "\n".join(lines) + "\n"


def process_skill(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(original)
    meta = slim_frontmatter(meta)
    body = strip_version_history(body)
    body = fix_basedir_links(body)
    body = normalize_resources(body, path.parent)
    # tidy excess blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    new_text = dump_frontmatter(meta) + "\n" + body
    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    total = 0
    for base in SKILL_GLOBS:
        for path in sorted(base.rglob("SKILL.md")):
            total += 1
            if process_skill(path):
                changed += 1
                print(f"updated: {path.relative_to(ROOT)}")
    print(f"done: {changed}/{total} skills updated")


if __name__ == "__main__":
    main()
