#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"

REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/source-map.md",
    "references/principles.md",
    "references/demo.en.md",
    "references/demo.zh-CN.md",
    "references/research.en.md",
    "references/research.zh-CN.md",
]

REQUIRED_SECTIONS = [
    "## Invocation Parameters",
    "## Response Modes",
    "## Core Models",
    "## Expression DNA",
    "## Values And Anti-Patterns",
    "## Voice And Delivery",
    "## Honest Boundary",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    if not SKILLS_ROOT.exists():
        print(f"Missing skills root: {SKILLS_ROOT}")
        return 1

    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() and path.name.endswith("-skill"))

    if not skill_dirs:
        print("No *-skill directories found.")
        return 1

    for skill_dir in skill_dirs:
        for relative in REQUIRED_FILES:
            full = skill_dir / relative
            if not full.exists():
                errors.append(f"{skill_dir.name}: missing {relative}")

        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            text = read_text(skill_md)
            for section in REQUIRED_SECTIONS:
                if section not in text:
                    errors.append(f"{skill_dir.name}: missing section `{section}`")

        overview_en = skill_dir / "references" / "overview.en.md"
        overview_zh = skill_dir / "references" / "overview.zh-CN.md"
        if overview_en.exists():
            text = read_text(overview_en)
            for marker in ["references/demo.en.md", "references/research.en.md"]:
                if marker not in text:
                    errors.append(f"{skill_dir.name}: overview.en.md missing `{marker}`")
        if overview_zh.exists():
            text = read_text(overview_zh)
            for marker in ["references/demo.zh-CN.md", "references/research.zh-CN.md"]:
                if marker not in text:
                    errors.append(f"{skill_dir.name}: overview.zh-CN.md missing `{marker}`")

    if errors:
        print("Skill content validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validated skill content successfully: "
        f"{len(skill_dirs)} skill(s), deep content files and sections present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
