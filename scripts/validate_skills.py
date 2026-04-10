#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
SKILL_NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md frontmatter is incomplete")

    body = parts[1]
    data: dict[str, str] = {}
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def require(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def validate_openai_yaml(path: Path, errors: list[str]) -> None:
    require(path, errors)
    if not path.exists():
        return

    text = read_text(path)
    required_strings = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
    ]
    for item in required_strings:
        if item not in text:
            errors.append(f"{path.relative_to(ROOT)} is missing `{item}`")


def validate_skill_dir(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_name = skill_dir.name

    if not SKILL_NAME_RE.fullmatch(skill_name):
        errors.append(
            f"Invalid skill directory name `{skill_name}`. Use lowercase letters, digits, and hyphens only."
        )

    skill_md = skill_dir / "SKILL.md"
    source_map = skill_dir / "references" / "source-map.md"
    principles = skill_dir / "references" / "principles.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    require(skill_md, errors)
    require(source_map, errors)
    require(principles, errors)
    validate_openai_yaml(openai_yaml, errors)

    if skill_md.exists():
        try:
            frontmatter = parse_frontmatter(skill_md)
        except ValueError as exc:
            errors.append(f"{skill_md.relative_to(ROOT)}: {exc}")
        else:
            name = frontmatter.get("name", "")
            description = frontmatter.get("description", "")
            if not name:
                errors.append(f"{skill_md.relative_to(ROOT)} is missing `name` in frontmatter")
            elif name != skill_name:
                errors.append(
                    f"{skill_md.relative_to(ROOT)} has name `{name}`, but directory name is `{skill_name}`"
                )

            if not description:
                errors.append(f"{skill_md.relative_to(ROOT)} is missing `description` in frontmatter")

    return errors


def main() -> int:
    if not SKILLS_ROOT.exists():
        print(f"No skills directory found at {SKILLS_ROOT.relative_to(ROOT)}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"No skills found under {SKILLS_ROOT.relative_to(ROOT)}")
        return 1

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill_dir(skill_dir))

    if all_errors:
        print("Skill validation failed:\n")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s) successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
