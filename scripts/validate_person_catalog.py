#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "person-catalog.json"
SKILLS_ROOT = ROOT / ".agents" / "skills"

REQUIRED_KEYS = {
    "slug",
    "name_zh",
    "name_en",
    "region",
    "fit_buckets",
    "domain",
    "status",
    "distillation_priority",
    "skill_path",
    "primary_use_case",
    "ordinary_people_value",
    "source_readiness",
    "risk_note",
    "recommended_skill_angle",
    "source_hints",
}

VALID_STATUS = {"reference_skill", "draft_skill", "candidate"}
VALID_SOURCE_READINESS = {"strong", "medium"}


def main() -> int:
    if not CATALOG_PATH.exists():
        print(f"Missing catalog: {CATALOG_PATH.relative_to(ROOT)}")
        return 1

    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    people = data.get("people", [])
    errors: list[str] = []

    if not isinstance(people, list):
        print("`people` must be a list")
        return 1

    if len(people) < 70:
        errors.append(f"Catalog must contain at least 70 people, found {len(people)}")

    if data.get("total_people") != len(people):
        errors.append(
            f"`total_people` is {data.get('total_people')}, but actual count is {len(people)}"
        )

    seen_slugs: set[str] = set()
    for index, item in enumerate(people, start=1):
        missing = REQUIRED_KEYS - set(item.keys())
        if missing:
            errors.append(f"Entry {index} is missing keys: {sorted(missing)}")
            continue

        slug = item["slug"]
        if slug in seen_slugs:
            errors.append(f"Duplicate slug: {slug}")
        seen_slugs.add(slug)

        if item["status"] not in VALID_STATUS:
            errors.append(f"{slug}: invalid status `{item['status']}`")

        if item["source_readiness"] not in VALID_SOURCE_READINESS:
            errors.append(f"{slug}: invalid source_readiness `{item['source_readiness']}`")

        if not isinstance(item["fit_buckets"], list) or not item["fit_buckets"]:
            errors.append(f"{slug}: fit_buckets must be a non-empty list")

        if not isinstance(item["source_hints"], list) or not item["source_hints"]:
            errors.append(f"{slug}: source_hints must be a non-empty list")

        skill_path = item["skill_path"]
        if item["status"] in {"reference_skill", "draft_skill"}:
            if not skill_path:
                errors.append(f"{slug}: skill_path is required for existing skills")
            elif not (ROOT / skill_path).exists():
                errors.append(f"{slug}: skill_path does not exist: {skill_path}")
        elif item["status"] == "candidate" and skill_path is not None:
            errors.append(f"{slug}: candidate entries must use null skill_path")

    if errors:
        print("Person catalog validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validated person catalog successfully: "
        f"{len(people)} people, {sum(1 for p in people if p['status'] != 'candidate')} existing skill entries."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
