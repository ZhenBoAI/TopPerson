[English](./person-catalog.md) | [简体中文](./person-catalog.zh-CN.md)

# TopPerson Person Catalog

This is the structured 100+ person dataset for future skill distillation.

It is different from the backlog:

- `docs/person-backlog.*` is the current planning shortlist
- `data/person-catalog.json` is the broader structured data pool

## Data Files

- JSON dataset: [`data/person-catalog.json`](../data/person-catalog.json)

## Current Counts

- Total people: `110`
- Reference skill: `1`
- Draft skills already created: `44`
- New candidates without a skill directory yet: `65`

## Main Fields

- `slug`
  Stable repository-friendly id
- `name_zh` / `name_en`
  Chinese and English names
- `fit_buckets`
  Main usage buckets: `life`, `study`, `work`, `life-guidance`
- `status`
  `reference_skill`, `draft_skill`, or `candidate`
- `distillation_priority`
  Current refinement or candidate priority
- `primary_use_case`
  What real problems this person is most useful for
- `ordinary_people_value`
  Why the method can transfer to ordinary users
- `source_readiness`
  `strong` or `medium`
- `risk_note`
  Main caution when turning this person into a skill
- `recommended_skill_angle`
  Best first skill angle
- `source_hints`
  Starting points for source collection

## Suggested Next Distillation Picks

If you want to keep expanding beyond the current 45 skill directories, these are strong next candidates:

- Confucius
- Hu Shi
- Tao Xingzhi
- Qian Xuesen
- Yuan Longping
- Tu Youyou
- Pony Ma
- Zhang Ruimin
- Viktor Frankl
- Taiichi Ohno
- Soichiro Honda
- Satya Nadella
- John Wooden
- Daniel Kahneman

## How To Use This Dataset

Common ways to use it:

- Filter by `fit_buckets` to find life / study / work / life-guidance skills
- Filter by `status` to separate existing skills from future candidates
- Filter by `source_readiness` if you want easier distillation first
- Filter by `distillation_priority` if you want a next batch

## Note

This catalog is for distillation planning, not final historiography.
Every candidate still needs source review before becoming a production-quality skill.
