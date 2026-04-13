# Contributing

[English](./CONTRIBUTING.md) | [简体中文](./CONTRIBUTING.zh-CN.md)

Welcome to contribute new skills or improve existing ones in `TopPerson`.

This repository accepts structured, AI-usable person-methodology skills rather than ordinary articles.

We care most about:

- source quality
- method extraction
- structural consistency
- modern translation and safety

## Quick Path To Propose A New Skill

If you want to propose a new skill, keep it simple:

1. Pick a person with real source material.
2. Say what problem this skill should solve.
3. Explain why ordinary people can use the method.
4. List the main sources.
5. Open an issue or PR.

## What Fits This Repository

Good submissions:

- a historical figure skill
- a modern person’s decision-making style skill
- source improvements or structural fixes for an existing skill
- clearer reference organization

Not a fit:

- plain biography
- biography summary without method extraction
- unsourced quote collection
- pseudoscience, manipulation, or unlawful guidance

## Minimum Skill Structure

Each skill should usually live under:

```text
.agents/skills/<skill-name>/
```

Minimum required files:

```text
.agents/skills/<skill-name>/SKILL.md
.agents/skills/<skill-name>/agents/openai.yaml
.agents/skills/<skill-name>/references/source-map.md
.agents/skills/<skill-name>/references/principles.md
```

Optional human-facing guide files:

```text
.agents/skills/<skill-name>/references/overview.en.md
.agents/skills/<skill-name>/references/overview.zh-CN.md
.agents/skills/<skill-name>/references/demo.en.md
.agents/skills/<skill-name>/references/demo.zh-CN.md
.agents/skills/<skill-name>/references/research.en.md
.agents/skills/<skill-name>/references/research.zh-CN.md
```

File roles:

- `SKILL.md`
  Main skill file describing purpose, triggers, and output style. Prefer sections such as `Invocation Parameters`, `Response Modes`, `Core Models`, `Voice And Delivery`, and `Honest Boundary`.
  Stronger skills should also include `Expression DNA` and `Values And Anti-Patterns`.
- `references/source-map.md`
  Source hierarchy: primary, secondary, and low-confidence materials.
- `references/principles.md`
  Distilled principles translated into modern actionable guidance.
- `references/overview.en.md`
  Optional English guide for repository visitors.
- `references/overview.zh-CN.md`
  Optional Simplified Chinese guide for repository visitors.
- `references/demo.en.md`
  Optional English example prompts and output-shape guide.
- `references/demo.zh-CN.md`
  Optional Chinese example prompts and output-shape guide.
- `references/research.en.md`
  Optional English research brief for deeper source guidance and next research questions.
- `references/research.zh-CN.md`
  Optional Chinese research brief for deeper source guidance and next research questions.
- `agents/openai.yaml`
  UI-facing and invocation metadata.

## Naming Rules

- Use lowercase hyphenated folder names such as `zeng-guofan-skill`
- The `name` field in `SKILL.md` frontmatter must match the folder name
- Names should be short, stable, and predictable

## Content Rules

### 1. Prefer Primary Sources

Prefer:

- books by the person
- letters
- diaries
- speeches
- papers
- interviews
- verified public materials

If primary sources are limited, high-quality secondary research is acceptable, but explain that clearly in `source-map.md`.

### 2. Separate Source Confidence

At minimum, use three layers:

- high-confidence sources
- interpretive supporting sources
- low-confidence or disputed sources

### 3. Do Not Build Quote Dumps

We want:

- reusable judgment frameworks
- actionable guidance
- clear boundaries

Not:

- motivational quote piles
- fake archaic slogans
- turning a person into a mythic guru

### 4. Must Translate To Modern Contexts

Historical skills cannot import their original era literally.

They must be translated into modern, lawful, ethically acceptable guidance.

Examples:

- do not encourage violence
- do not encourage manipulation or humiliation
- do not encourage discrimination or oppression
- do not center physiognomy, class bias, or power games

### 5. Provide A Clear Output Shape

Each skill should suggest a stable default output structure, such as:

- core judgment
- first moves
- avoid
- short- and mid-term plan
- communication advice
- reflection question

### 6. Support Parameterized Invocation

Prefer these four task modes by default:

- `quick-judgment`
- `action-plan`
- `conversation-draft`
- `30-day-plan`

Also make the `SKILL.md` clear about these prompt parameters:

- `problem-area`
- `task-mode`
- `constraints`
- `voice-mode`

## Recommended Workflow

1. Gather real sources
2. Build source hierarchy in `source-map.md`
3. Distill principles in `principles.md`
4. Write triggers, usage, output, and boundaries in `SKILL.md`
5. Optionally add `overview.en.md` and/or `overview.zh-CN.md`
6. Optionally add `demo.en.md` and/or `demo.zh-CN.md`
7. Optionally add `research.en.md` and/or `research.zh-CN.md`
8. Run local validation
9. Open a PR

## Pre-Submission Checklist

- `python3 scripts/validate_skills.py` passes successfully
- `SKILL.md` frontmatter is complete
- required files exist
- `references/source-map.md` makes source hierarchy explicit
- `references/principles.md` is distilled, not copied
- `python3 scripts/validate_skill_content.py` passes for deeper skill content
- there are no obvious fake sources, fake quotations, or pseudoscience
- there is no unlawful, deceptive, manipulative, or harmful guidance

## What A PR Should Include

A PR description should at least include:

- who the skill is about
- main sources used
- what kinds of problems it helps solve
- how disputed or low-confidence material was handled

Use the repository PR template.

## Review Standard

Maintainers review along these dimensions:

1. source quality
2. structural completeness
3. quality of method extraction
4. modern translation and safety boundaries
5. readability and AI usability

For a more detailed checklist, see:

- [`docs/review-checklist.md`](./docs/review-checklist.md)
- [`docs/review-checklist.zh-CN.md`](./docs/review-checklist.zh-CN.md)

## Suggestions

- write less, but write accurately
- use fewer quotes and explain the method clearly
- say when confidence is limited
- make the skill a reliable thinking framework, not a flashy roleplay persona
