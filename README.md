[English](./README.md) | [简体中文](./README.zh-CN.md)

# TopPerson

`TopPerson` is an open-source repository of person-based AI skills.

It helps AI answer a practical question:

`How would a top person judge, decide, and act in this situation?`

## Contents

- [What It Does](#what-it-does)
- [Main Use Cases](#main-use-cases)
- [Current Skills](#current-skills)
- [Distillation Dataset](#distillation-dataset)
- [Distillation Roadmap](#distillation-roadmap)
- [How To Use](#how-to-use)
- [How To Propose A New Skill](#how-to-propose-a-new-skill)
- [Contribution Rules](#contribution-rules)
- [Validation](#validation)
- [License](#license)

## What It Does

TopPerson turns biographies, primary works, letters, speeches, interviews, and credible research into reusable skills.

This repository is for:

- practical judgment
- action planning
- modern translation of historical or modern methods

This repository is not for:

- quote collections
- fandom
- empty motivation
- harmful or manipulative guidance

## Main Use Cases

You can use TopPerson skills to think through:

- `Life`: self-discipline, habits, emotional stability, long-term direction
- `Study`: learning methods, focus, explanation, practice, curiosity
- `Work`: execution, management, communication, product judgment, decision-making
- `Life guidance`: major choices, setbacks, transitions, values, how to act next

## Current Skills

Current repository status: `45` skill directories in [`.agents/skills`](./.agents/skills).

### Reference Skill

- [`zeng-guofan`](./.agents/skills/zeng-guofan/SKILL.md): Qing statesman and military leader known for self-discipline, team building, and long-horizon order.

### Other Available Skills

- [`andy-grove`](./.agents/skills/andy-grove/SKILL.md): Former Intel CEO known for paranoid management and execution systems.
- [`benjamin-franklin`](./.agents/skills/benjamin-franklin/SKILL.md): Statesman, inventor, and writer known for habits, self-improvement, and pragmatism.
- [`cao-cao`](./.agents/skills/cao-cao/SKILL.md): Three Kingdoms statesman, warlord, and poet known for strategy and talent use.
- [`cao-dewang`](./.agents/skills/cao-dewang/SKILL.md): Founder of Fuyao Glass known for industrial discipline, cost awareness, and pragmatic execution.
- [`charlie-munger`](./.agents/skills/charlie-munger/SKILL.md): Investor and Buffett's longtime partner known for mental models and avoiding stupidity.
- [`duan-yongping`](./.agents/skills/duan-yongping/SKILL.md): Chinese entrepreneur and investor known for long-termism, selective focus, and business judgment.
- [`elon-musk`](./.agents/skills/elon-musk/SKILL.md): Entrepreneur known for first-principles thinking, technical boldness, and hard trade-offs.
- [`haruki-murakami`](./.agents/skills/haruki-murakami/SKILL.md): Japanese novelist known for routine, endurance, and long solitary creative work.
- [`hayao-miyazaki`](./.agents/skills/hayao-miyazaki/SKILL.md): Japanese animator and director known for craft discipline and creative standards.
- [`jack-ma`](./.agents/skills/jack-ma/SKILL.md): Entrepreneur and communicator known for market education and organizational energy.
- [`jeff-bezos`](./.agents/skills/jeff-bezos/SKILL.md): Amazon founder known for customer obsession, flywheel thinking, and long-term building.
- [`jensen-huang`](./.agents/skills/jensen-huang/SKILL.md): NVIDIA founder known for long-term R&D, technical strategy, and founder leadership.
- [`kazuo-inamori`](./.agents/skills/kazuo-inamori/SKILL.md): Kyocera founder known for management discipline, altruism, and long-term organization building.
- [`kobe-bryant`](./.agents/skills/kobe-bryant/SKILL.md): Basketball icon known for discipline, deliberate practice, and competitive standards.
- [`konosuke-matsushita`](./.agents/skills/konosuke-matsushita/SKILL.md): Panasonic founder known for management philosophy, people development, and enterprise building.
- [`lee-kuan-yew`](./.agents/skills/lee-kuan-yew/SKILL.md): Founding Prime Minister of Singapore known for institutional design and pragmatic trade-offs.
- [`lei-jun`](./.agents/skills/lei-jun/SKILL.md): Entrepreneur and product-minded founder known for product judgment, efficiency, and sincere communication.
- [`luo-xiang`](./.agents/skills/luo-xiang/SKILL.md): Law professor and public educator known for principled reasoning and clear explanation.
- [`marcus-aurelius`](./.agents/skills/marcus-aurelius/SKILL.md): Roman emperor and Stoic thinker known for self-command, emotional steadiness, and duty.
- [`napoleon`](./.agents/skills/napoleon/SKILL.md): Military and political leader known for strategy, timing, and concentration of effort.
- [`peter-drucker`](./.agents/skills/peter-drucker/SKILL.md): Foundational management thinker known for objectives and knowledge work effectiveness.
- [`rafael-nadal`](./.agents/skills/rafael-nadal/SKILL.md): Tennis champion known for resilience, consistency, and low-error execution.
- [`ray-dalio`](./.agents/skills/ray-dalio/SKILL.md): Bridgewater founder known for principles, systemized decisions, and feedback loops.
- [`ren-zhengfei`](./.agents/skills/ren-zhengfei/SKILL.md): Huawei founder known for crisis awareness, survival thinking, and organizational discipline.
- [`richard-feynman`](./.agents/skills/richard-feynman/SKILL.md): Physicist and explainer known for understanding, explanation, and curiosity.
- [`steve-jobs`](./.agents/skills/steve-jobs/SKILL.md): Apple co-founder known for product taste, focus, and high standards.
- [`su-shi`](./.agents/skills/su-shi/SKILL.md): Song dynasty writer and statesman known for resilience, emotional balance, and life order under adversity.
- [`wang-xing`](./.agents/skills/wang-xing/SKILL.md): Founder of Meituan known for competitive judgment, strategic focus, and organizational scaling.
- [`wang-yangming`](./.agents/skills/wang-yangming/SKILL.md): Ming dynasty thinker and general known for unity of knowledge and action.
- [`warren-buffett`](./.agents/skills/warren-buffett/SKILL.md): Long-term investing icon known for circle of competence, patience, and durable decisions.
- [`zhang-yiming`](./.agents/skills/zhang-yiming/SKILL.md): ByteDance founder known for rational decision-making, information processing, and mechanism design.
- [`zhuge-liang`](./.agents/skills/zhuge-liang/SKILL.md): Three Kingdoms strategist and statesman known for planning discipline, diligence, and conscientious execution.

### Newly Added Draft Skills

- [`confucius`](./.agents/skills/confucius/SKILL.md): Classical Chinese teacher and thinker known for conduct, learning, role responsibility, and everyday order.
- [`hu-shi`](./.agents/skills/hu-shi/SKILL.md): Modern Chinese writer and thinker known for evidence, skepticism, and plain expression.
- [`tao-xingzhi`](./.agents/skills/tao-xingzhi/SKILL.md): Educator known for learning by doing and practical education.
- [`qian-xuesen`](./.agents/skills/qian-xuesen/SKILL.md): Scientist and engineer known for systems thinking and complex-project synthesis.
- [`yuan-longping`](./.agents/skills/yuan-longping/SKILL.md): Agricultural scientist known for field-tested persistence and practical science.
- [`tu-youyou`](./.agents/skills/tu-youyou/SKILL.md): Scientist known for evidence extraction, quiet rigor, and patient validation.
- [`ma-huateng`](./.agents/skills/ma-huateng/SKILL.md): Founder of Tencent known for product restraint, pacing, and platform judgment.
- [`zhang-ruimin`](./.agents/skills/zhang-ruimin/SKILL.md): Haier leader known for accountability, self-disruption, and user-facing organizational change.
- [`viktor-frankl`](./.agents/skills/viktor-frankl/SKILL.md): Psychiatrist and thinker known for meaning, agency, and response under suffering.
- [`taiichi-ohno`](./.agents/skills/taiichi-ohno/SKILL.md): Toyota production pioneer known for waste reduction, process discipline, and go-to-gemba observation.
- [`satya-nadella`](./.agents/skills/satya-nadella/SKILL.md): Microsoft CEO known for empathy, learning culture, and strategic renewal.
- [`daniel-kahneman`](./.agents/skills/daniel-kahneman/SKILL.md): Psychologist known for bias reduction, decision hygiene, and noise control.

See also:

- English backlog: [`docs/person-backlog.md`](./docs/person-backlog.md)
- Chinese backlog: [`docs/person-backlog.zh-CN.md`](./docs/person-backlog.zh-CN.md)

## Distillation Dataset

For broader person collection beyond the current skill directories:

- English guide: [`docs/person-catalog.md`](./docs/person-catalog.md)
- Chinese guide: [`docs/person-catalog.zh-CN.md`](./docs/person-catalog.zh-CN.md)
- JSON data: [`data/person-catalog.json`](./data/person-catalog.json)

## Distillation Roadmap

If you want the next recommended batches instead of the full raw catalog:

- English roadmap: [`docs/person-roadmap.md`](./docs/person-roadmap.md)
- Chinese roadmap: [`docs/person-roadmap.zh-CN.md`](./docs/person-roadmap.zh-CN.md)

## How To Use

### 1. Browse skills

Open [`.agents/skills`](./.agents/skills) and choose a person.

### 2. Invoke a skill

Example:

```text
Use $zeng-guofan to analyze this situation and give me actionable advice.
```

### 3. Ask by scenario

Example prompts:

```text
Use $wang-yangming to help me stop overthinking and start acting.
Use $richard-feynman to help me learn this topic clearly.
Use $lei-jun to help me judge this product direction.
Use $duan-yongping to help me decide whether this opportunity is worth doing.
```

## How To Propose A New Skill

If you want to add a new person skill, use this simple path:

1. Pick a person with real source material.
2. Explain why ordinary people can use the method.
3. State the main use case.
4. List primary and secondary sources.
5. Open an issue or PR.

Start here:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`CONTRIBUTING.zh-CN.md`](./CONTRIBUTING.zh-CN.md)
- [`docs/review-checklist.md`](./docs/review-checklist.md)
- [`docs/review-checklist.zh-CN.md`](./docs/review-checklist.zh-CN.md)

Recommended template files:

- [`templates/person-skill/SKILL.md`](./templates/person-skill/SKILL.md)
- [`templates/person-skill/references/source-map.md`](./templates/person-skill/references/source-map.md)
- [`templates/person-skill/references/principles.md`](./templates/person-skill/references/principles.md)
- [`templates/person-skill/agents/openai.yaml`](./templates/person-skill/agents/openai.yaml)

## Contribution Rules

Good contributions should be:

- source-based
- method-first
- modern and safe
- usable by AI

Please avoid:

- quote dumps
- myth-making
- fake sources
- unlawful, deceptive, or harmful advice

## Validation

Run this before opening a PR:

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_person_catalog.py
```

## License

This repository is released under the [`MIT License`](./LICENSE).
