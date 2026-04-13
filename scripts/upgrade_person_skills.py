#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"

TRIGGER_APPEND = (
    " Also use when the user asks what this person would do, asks to switch into this "
    "person's perspective, or wants this person's method applied to life, study, work, "
    "or life-guidance problems."
)

ZH_OVERVIEW = """# {display_name} skill 说明

## 这个 skill 主要解决什么

这个 skill 不是语录堆砌，也不是夸张扮演，而是把 {display_name} 反复出现的方法论整理成可调用的认知操作系统。

核心方向：

- {short_description}

更适合放到这四类问题里使用：

- `生活`：习惯、情绪、关系、秩序、长期方向
- `学习`：理解、练习、解释、节奏、复盘
- `工作`：判断、执行、沟通、带人、取舍
- `人生指导`：转折期、重大选择、失误修正、下一步怎么走

## 怎么调用

建议在提问时补足这几个参数：

- `问题类型`：生活 / 学习 / 工作 / 人生指导
- `任务模式`：快速判断 / 行动方案 / 沟通草稿 / 30天计划
- `约束条件`：时间、资源、关系人、风险、不能碰的边界
- `语气要求`：默认分析模式；如果你明确要求，也可以带一点 {display_name} 的风格

直接调用示例：

```text
Use ${skill_name} to analyze this situation with the method of {display_name} and give me a practical plan.
```

## 使用提醒

- 默认优先现代、清晰、可执行，不做夸张角色扮演
- 如果问题超出 {display_name} 的高置信范围，skill 应该明确说明不确定
- 更好的效果来自“方法迁移”，不是“口气模仿”

## 建议先看

- `SKILL.md`
- `references/source-map.md`
- `references/principles.md`
"""

EN_OVERVIEW = """# {display_name} Skill Overview

## What This Skill Is For

This skill is not a quote dump or exaggerated roleplay. It turns {display_name}'s recurring method into a reusable cognitive operating system.

Core direction:

- {core_direction_en}

Best fit across four problem areas:

- `Life`: habits, emotions, relationships, order, long-term direction
- `Study`: understanding, practice, explanation, pace, review
- `Work`: judgment, execution, communication, leadership, trade-offs
- `Life guidance`: transitions, major choices, course correction, what to do next

## How To Invoke It

It works better when the prompt includes these parameters:

- `problem-area`: life / study / work / life-guidance
- `task-mode`: quick-judgment / action-plan / conversation-draft / 30-day-plan
- `constraints`: time, resources, stakeholders, risks, and non-negotiables
- `voice-mode`: default is analysis; add light {display_name} tone only if explicitly requested

Direct example:

```text
Use ${skill_name} to analyze this situation with the method of {display_name} and give me a practical plan.
```

## Usage Notes

- Default to modern, clear, practical analysis instead of heavy roleplay
- If the request goes beyond {display_name}'s strongest documented range, the skill should say so
- Better results come from method transfer, not surface imitation

## Read First

- `SKILL.md`
- `references/source-map.md`
- `references/principles.md`
"""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def split_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Incomplete frontmatter")
    return parts[0], parts[1], parts[2]


def get_frontmatter_value(frontmatter: str, key: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+)$", re.MULTILINE)
    match = pattern.search(frontmatter)
    return match.group(1).strip() if match else ""


def set_frontmatter_value(frontmatter: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:\s*.+$", re.MULTILINE)
    replacement = f"{key}: {value}"
    if pattern.search(frontmatter):
        return pattern.sub(replacement, frontmatter, count=1)
    return frontmatter.rstrip() + "\n" + replacement + "\n"


def parse_openai_yaml(path: Path) -> tuple[str, str, str]:
    text = read_text(path)
    display = re.search(r'display_name:\s*"([^"]+)"', text)
    short = re.search(r'short_description:\s*"([^"]+)"', text)
    prompt = re.search(r'default_prompt:\s*"([^"]+)"', text)
    return (
        display.group(1) if display else path.parents[1].name,
        short.group(1) if short else "",
        prompt.group(1) if prompt else "",
    )


def update_openai_yaml(path: Path, skill_name: str, display_name: str) -> None:
    text = read_text(path)
    prompt_line = (
        f'  default_prompt: "Use ${skill_name} to analyze this situation with the method of {display_name} '
        'and return a quick judgment, action plan, conversation draft, or 30-day plan."'
    )
    text = re.sub(
        r'^\s*default_prompt:\s*".*"$',
        prompt_line,
        text,
        flags=re.MULTILINE,
    )
    write_text(path, text)


def title_from_body(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def insert_once(body: str, marker: str, addition: str) -> str:
    if addition.strip() in body:
        return body
    return body.replace(marker, addition + marker, 1)


def update_skill_md(path: Path, display_name: str) -> None:
    text = read_text(path)
    _prefix, frontmatter, body = split_frontmatter(text)
    skill_name = path.parent.name
    title = title_from_body(body, display_name)

    frontmatter = set_frontmatter_value(frontmatter, "name", skill_name)

    description = get_frontmatter_value(frontmatter, "description")
    if description and TRIGGER_APPEND not in description:
        frontmatter = set_frontmatter_value(frontmatter, "description", description + TRIGGER_APPEND)

    if "## Invocation Parameters" not in body:
        invocation = f"""## Invocation Parameters

Before answering, quickly lock these parameters:

1. `problem-area`
   Choose the closest fit: `life`, `study`, `work`, `life-guidance`.
2. `task-mode`
   Choose one: `quick-judgment`, `action-plan`, `conversation-draft`, `30-day-plan`.
3. `constraints`
   Capture time, resources, people, risk, and non-negotiables.
4. `voice-mode`
   Default to `analysis`. Use `voice` only if the user explicitly asks for {title}'s tone.

## Response Modes

- `quick-judgment`: give one diagnosis, the first move, and the main thing to avoid.
- `action-plan`: give priorities, sequencing, and a 7-day plan.
- `conversation-draft`: give the user's position, the boundary, and a usable draft message.
- `30-day-plan`: give weekly checkpoints, review points, and a realistic rhythm.

"""
        body = insert_once(body, "## Core Lens", invocation)

    body = body.replace("## Core Lens", "## Core Models", 1)
    body = body.replace("## Scenario Guidance", "## Decision Heuristics", 1)

    voice = f"""## Voice And Delivery

- Default to modern, plain, and practical language.
- If the user explicitly asks for {title}'s tone, you may switch to a light first-person voice for the current response.
- Keep the method stronger than the performance; do not turn the answer into parody or cosplay.
- Do not invent quotations, obscure jargon, or historical dialogue.

"""
    if "## Voice And Delivery" not in body:
        body = insert_once(body, "## Output Format", voice)
    else:
        body = re.sub(
            r"## Voice And Delivery\n\n.*?\n(?=## Output Format)",
            voice,
            body,
            flags=re.DOTALL,
        )

    if "default to `action-plan`" not in body:
        body = body.replace(
            "When answering with this skill, prefer this structure:\n",
            "When answering with this skill, prefer this structure:\n\n"
            "If the user does not specify a mode, default to `action-plan`. Compress or expand the sections below to fit the chosen response mode.\n",
            1,
        )
        body = body.replace(
            "When using this skill, prefer this structure:\n",
            "When using this skill, prefer this structure:\n\n"
            "If the user does not specify a mode, default to `action-plan`. Compress or expand the sections below to fit the chosen response mode.\n",
            1,
        )

    boundary = f"""## Honest Boundary

- Base the answer on recurring source-backed patterns, not on one-off anecdotes.
- If the source support is indirect or low-confidence, say so briefly.
- If the request falls outside {title}'s strongest documented domain, give the nearest applicable method and label it as an inference.

"""
    if "## Honest Boundary" not in body:
        body = insert_once(body, "## Guardrails", boundary)
    else:
        body = re.sub(
            r"## Honest Boundary\n\n.*?\n(?=## Guardrails)",
            boundary,
            body,
            flags=re.DOTALL,
        )

    if "Examples Of Good Triggers" in body:
        trigger_line = f'- "切换到{title}，帮我先做一个快速判断。"\n'
        body = re.sub(
            r'## Examples Of Good Triggers\n(?:\n- "切换到.*?"\n)?',
            f"## Examples Of Good Triggers\n\n{trigger_line}",
            body,
            count=1,
        )
        body = re.sub(
            r'(## Examples Of Good Triggers\n\n- ".*?"\n)\n(- )',
            r"\1\2",
            body,
            count=1,
        )

    body = re.sub(r"([^\n])\n(## )", r"\1\n\n\2", body)
    body = re.sub(r"\n{3,}", "\n\n", body)

    updated = f"---\n{frontmatter}---\n{body}"
    write_text(path, updated)


def extract_english_summary(description: str, fallback: str) -> str:
    match = re.search(r"Use when Codex needs (.+?)(?: Also use when|$)", description)
    if match:
        return match.group(1).strip().rstrip(".")
    if "。" in fallback and "." not in fallback:
        return fallback.replace("。", ". ").replace("，", ", ").strip()
    return fallback.strip()


def write_overviews(skill_dir: Path, display_name: str, short_description: str) -> None:
    skill_text = read_text(skill_dir / "SKILL.md")
    _prefix, frontmatter, _body = split_frontmatter(skill_text)
    description = get_frontmatter_value(frontmatter, "description")
    core_direction_en = extract_english_summary(description, short_description)
    zh_path = skill_dir / "references" / "overview.zh-CN.md"
    en_path = skill_dir / "references" / "overview.en.md"

    write_text(
        zh_path,
        ZH_OVERVIEW.format(
            display_name=display_name,
            short_description=short_description,
            skill_name=skill_dir.name,
        ),
    )
    write_text(
        en_path,
        EN_OVERVIEW.format(
            display_name=display_name,
            core_direction_en=core_direction_en,
            skill_name=skill_dir.name,
        ),
    )


def main() -> None:
    for skill_dir in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir()):
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        skill_md = skill_dir / "SKILL.md"

        display_name, short_description, _prompt = parse_openai_yaml(openai_yaml)
        update_openai_yaml(openai_yaml, skill_dir.name, display_name)
        update_skill_md(skill_md, display_name)
        write_overviews(skill_dir, display_name, short_description)


if __name__ == "__main__":
    main()
