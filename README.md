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

- [`zeng-guofan-skill`](./.agents/skills/zeng-guofan-skill/SKILL.md): Qing statesman and military leader known for self-discipline, team building, and long-horizon order.

### Other Available Skills

- [`andy-grove-skill`](./.agents/skills/andy-grove-skill/SKILL.md): Former Intel CEO known for paranoid management and execution systems.
- [`benjamin-franklin-skill`](./.agents/skills/benjamin-franklin-skill/SKILL.md): Statesman, inventor, and writer known for habits, self-improvement, and pragmatism.
- [`cao-cao-skill`](./.agents/skills/cao-cao-skill/SKILL.md): Three Kingdoms statesman, warlord, and poet known for strategy and talent use.
- [`cao-dewang-skill`](./.agents/skills/cao-dewang-skill/SKILL.md): Founder of Fuyao Glass known for industrial discipline, cost awareness, and pragmatic execution.
- [`charlie-munger-skill`](./.agents/skills/charlie-munger-skill/SKILL.md): Investor and Buffett's longtime partner known for mental models and avoiding stupidity.
- [`duan-yongping-skill`](./.agents/skills/duan-yongping-skill/SKILL.md): Chinese entrepreneur and investor known for long-termism, selective focus, and business judgment.
- [`elon-musk-skill`](./.agents/skills/elon-musk-skill/SKILL.md): Entrepreneur known for first-principles thinking, technical boldness, and hard trade-offs.
- [`haruki-murakami-skill`](./.agents/skills/haruki-murakami-skill/SKILL.md): Japanese novelist known for routine, endurance, and long solitary creative work.
- [`hayao-miyazaki-skill`](./.agents/skills/hayao-miyazaki-skill/SKILL.md): Japanese animator and director known for craft discipline and creative standards.
- [`jack-ma-skill`](./.agents/skills/jack-ma-skill/SKILL.md): Entrepreneur and communicator known for market education and organizational energy.
- [`jeff-bezos-skill`](./.agents/skills/jeff-bezos-skill/SKILL.md): Amazon founder known for customer obsession, flywheel thinking, and long-term building.
- [`jensen-huang-skill`](./.agents/skills/jensen-huang-skill/SKILL.md): NVIDIA founder known for long-term R&D, technical strategy, and founder leadership.
- [`kazuo-inamori-skill`](./.agents/skills/kazuo-inamori-skill/SKILL.md): Kyocera founder known for management discipline, altruism, and long-term organization building.
- [`kobe-bryant-skill`](./.agents/skills/kobe-bryant-skill/SKILL.md): Basketball icon known for discipline, deliberate practice, and competitive standards.
- [`konosuke-matsushita-skill`](./.agents/skills/konosuke-matsushita-skill/SKILL.md): Panasonic founder known for management philosophy, people development, and enterprise building.
- [`lee-kuan-yew-skill`](./.agents/skills/lee-kuan-yew-skill/SKILL.md): Founding Prime Minister of Singapore known for institutional design and pragmatic trade-offs.
- [`lei-jun-skill`](./.agents/skills/lei-jun-skill/SKILL.md): Entrepreneur and product-minded founder known for product judgment, efficiency, and sincere communication.
- [`luo-xiang-skill`](./.agents/skills/luo-xiang-skill/SKILL.md): Law professor and public educator known for principled reasoning and clear explanation.
- [`marcus-aurelius-skill`](./.agents/skills/marcus-aurelius-skill/SKILL.md): Roman emperor and Stoic thinker known for self-command, emotional steadiness, and duty.
- [`napoleon-skill`](./.agents/skills/napoleon-skill/SKILL.md): Military and political leader known for strategy, timing, and concentration of effort.
- [`peter-drucker-skill`](./.agents/skills/peter-drucker-skill/SKILL.md): Foundational management thinker known for objectives and knowledge work effectiveness.
- [`rafael-nadal-skill`](./.agents/skills/rafael-nadal-skill/SKILL.md): Tennis champion known for resilience, consistency, and low-error execution.
- [`ray-dalio-skill`](./.agents/skills/ray-dalio-skill/SKILL.md): Bridgewater founder known for principles, systemized decisions, and feedback loops.
- [`ren-zhengfei-skill`](./.agents/skills/ren-zhengfei-skill/SKILL.md): Huawei founder known for crisis awareness, survival thinking, and organizational discipline.
- [`richard-feynman-skill`](./.agents/skills/richard-feynman-skill/SKILL.md): Physicist and explainer known for understanding, explanation, and curiosity.
- [`steve-jobs-skill`](./.agents/skills/steve-jobs-skill/SKILL.md): Apple co-founder known for product taste, focus, and high standards.
- [`su-shi-skill`](./.agents/skills/su-shi-skill/SKILL.md): Song dynasty writer and statesman known for resilience, emotional balance, and life order under adversity.
- [`wang-xing-skill`](./.agents/skills/wang-xing-skill/SKILL.md): Founder of Meituan known for competitive judgment, strategic focus, and organizational scaling.
- [`wang-yangming-skill`](./.agents/skills/wang-yangming-skill/SKILL.md): Ming dynasty thinker and general known for unity of knowledge and action.
- [`warren-buffett-skill`](./.agents/skills/warren-buffett-skill/SKILL.md): Long-term investing icon known for circle of competence, patience, and durable decisions.
- [`zhang-yiming-skill`](./.agents/skills/zhang-yiming-skill/SKILL.md): ByteDance founder known for rational decision-making, information processing, and mechanism design.
- [`zhuge-liang-skill`](./.agents/skills/zhuge-liang-skill/SKILL.md): Three Kingdoms strategist and statesman known for planning discipline, diligence, and conscientious execution.

### Newly Added Draft Skills

- [`confucius-skill`](./.agents/skills/confucius-skill/SKILL.md): Classical Chinese teacher and thinker known for conduct, learning, role responsibility, and everyday order.
- [`hu-shi-skill`](./.agents/skills/hu-shi-skill/SKILL.md): Modern Chinese writer and thinker known for evidence, skepticism, and plain expression.
- [`tao-xingzhi-skill`](./.agents/skills/tao-xingzhi-skill/SKILL.md): Educator known for learning by doing and practical education.
- [`qian-xuesen-skill`](./.agents/skills/qian-xuesen-skill/SKILL.md): Scientist and engineer known for systems thinking and complex-project synthesis.
- [`yuan-longping-skill`](./.agents/skills/yuan-longping-skill/SKILL.md): Agricultural scientist known for field-tested persistence and practical science.
- [`tu-youyou-skill`](./.agents/skills/tu-youyou-skill/SKILL.md): Scientist known for evidence extraction, quiet rigor, and patient validation.
- [`ma-huateng-skill`](./.agents/skills/ma-huateng-skill/SKILL.md): Founder of Tencent known for product restraint, pacing, and platform judgment.
- [`zhang-ruimin-skill`](./.agents/skills/zhang-ruimin-skill/SKILL.md): Haier leader known for accountability, self-disruption, and user-facing organizational change.
- [`viktor-frankl-skill`](./.agents/skills/viktor-frankl-skill/SKILL.md): Psychiatrist and thinker known for meaning, agency, and response under suffering.
- [`taiichi-ohno-skill`](./.agents/skills/taiichi-ohno-skill/SKILL.md): Toyota production pioneer known for waste reduction, process discipline, and go-to-gemba observation.
- [`satya-nadella-skill`](./.agents/skills/satya-nadella-skill/SKILL.md): Microsoft CEO known for empathy, learning culture, and strategic renewal.
- [`daniel-kahneman-skill`](./.agents/skills/daniel-kahneman-skill/SKILL.md): Psychologist known for bias reduction, decision hygiene, and noise control.

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
Use $zeng-guofan-skill to analyze this situation and give me actionable advice.
```

### 3. Ask by scenario

Example prompts:

```text
Use $wang-yangming-skill to help me stop overthinking and start acting.
Use $richard-feynman-skill to help me learn this topic clearly.
Use $lei-jun-skill to help me judge this product direction.
Use $duan-yongping-skill to help me decide whether this opportunity is worth doing.
```

### 4. Pick a task mode

Most person skills now support four common modes:

- `quick-judgment`
- `action-plan`
- `conversation-draft`
- `30-day-plan`

Examples:

```text
Use $zeng-guofan-skill to give me a quick judgment on this team problem.
Use $confucius-skill to draft what I should say in this conflict.
Use $richard-feynman-skill to make me a 30-day learning plan for this topic.
```

### 5. Read the built-in examples

Many skills now include extra reference files such as:

- `references/demo.en.md`
- `references/demo.zh-CN.md`
- `references/research.en.md`
- `references/research.zh-CN.md`

Use them to see how to ask better questions and what a stronger output shape looks like.

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
python3 scripts/validate_skill_content.py
```

## License

This repository is released under the [`MIT License`](./LICENSE).
