#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
SKIP_PARTS = {".git", ".omx", ".workbuddy", "slides", "__pycache__"}
TEXT_SUFFIXES = {".md", ".yaml", ".json", ".py", ".txt"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def build_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(SKILLS_ROOT.iterdir()):
        if not path.is_dir():
            continue
        if path.name.endswith("-skill"):
            continue
        mapping[path.name] = f"{path.name}-skill"
    return mapping


def rename_directories(mapping: dict[str, str]) -> None:
    for old, new in mapping.items():
        src = SKILLS_ROOT / old
        dst = SKILLS_ROOT / new
        if src.exists() and not dst.exists():
            src.rename(dst)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        files.append(path)
    return files


def replace_general(text: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        text = text.replace(f".agents/skills/{old}/", f".agents/skills/{new}/")
        text = text.replace(f"${old}", f"${new}")
        text = re.sub(rf"^name:\s*{re.escape(old)}\s*$", f"name: {new}", text, flags=re.MULTILINE)
    return text


def replace_readme_labels(text: str) -> str:
    text = re.sub(
        r"(\[`)([a-z0-9-]+)(`\]\(\./\.agents/skills/)([a-z0-9-]+-skill)(/SKILL\.md\))",
        lambda m: f"{m.group(1)}{m.group(4)}{m.group(3)}{m.group(4)}{m.group(5)}",
        text,
    )
    text = re.sub(
        r"(\[`[^`\n]* / )([a-z0-9-]+)(`\]\(\./\.agents/skills/)([a-z0-9-]+-skill)(/SKILL\.md\))",
        lambda m: f"{m.group(1)}{m.group(4)}{m.group(3)}{m.group(4)}{m.group(5)}",
        text,
    )
    return text


def replace_contributing_examples(text: str) -> str:
    text = text.replace("such as `zeng-guofan`", "such as `zeng-guofan-skill`")
    text = text.replace("例如 `zeng-guofan`", "例如 `zeng-guofan-skill`")
    return text


def replace_count_typos(text: str) -> str:
    text = text.replace("current 33 skill directories", "current 45 skill directories")
    text = text.replace("现有 33 个 skill 之外", "现有 45 个 skill 之外")
    return text


def main() -> None:
    mapping = build_mapping()
    if not mapping:
        return

    rename_directories(mapping)

    for path in iter_text_files():
        original = read_text(path)
        updated = replace_general(original, mapping)

        if path.name in {"README.md", "README.zh-CN.md"}:
            updated = replace_readme_labels(updated)
        if path.name in {"CONTRIBUTING.md", "CONTRIBUTING.zh-CN.md"}:
            updated = replace_contributing_examples(updated)
        if path.name in {"person-catalog.md", "person-catalog.zh-CN.md"}:
            updated = replace_count_typos(updated)

        if updated != original:
            write_text(path, updated)


if __name__ == "__main__":
    main()
