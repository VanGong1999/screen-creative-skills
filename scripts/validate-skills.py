#!/usr/bin/env python3
"""Structural validation for all SKILL.md files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASES = [ROOT / "category", ROOT / "english-version" / "category"]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return ["missing frontmatter"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return ["unclosed frontmatter"]
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except Exception as e:  # noqa: BLE001
        return [f"invalid yaml: {e}"]

    name = meta.get("name")
    desc = meta.get("description")
    folder = path.parent.name
    if not name:
        errors.append("missing name")
    elif name != folder:
        errors.append(f"name '{name}' != folder '{folder}'")
    if not desc or not str(desc).strip():
        errors.append("missing description")
    elif len(str(desc)) > 1024:
        errors.append(f"description too long: {len(str(desc))}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", str(name or "")):
        errors.append("invalid name format")

    forbidden = ("changelog", "allowed-tools", "model", "compatibility", "version")
    for key in forbidden:
        if key in meta:
            errors.append(f"unexpected frontmatter key: {key}")

    body = text[end + 5 :]
    if "## 版本历史" in body or "## Version History" in body:
        errors.append("version history section still present")
    if "{baseDir}" in body:
        errors.append("legacy {baseDir} path still present")

    # referenced local markdown must exist
    for m in re.finditer(r"\[[^\]]+\]\((references/[^)]+)\)", body):
        rel = m.group(1).split("#", 1)[0]
        if not (path.parent / rel).exists():
            errors.append(f"broken link: {rel}")

    lines = body.count("\n") + 1
    if lines > 500:
        errors.append(f"SKILL.md too long: {lines} lines")

    return errors


def main() -> int:
    failed = 0
    total = 0
    for base in BASES:
        for path in sorted(base.rglob("SKILL.md")):
            total += 1
            errs = validate(path)
            if errs:
                failed += 1
                print(f"FAIL {path.relative_to(ROOT)}")
                for e in errs:
                    print(f"  - {e}")
    print(f"\n{total - failed}/{total} skills passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
