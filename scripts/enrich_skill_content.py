#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"

PROFILE_OVERRIDES = {
    "confucius-skill": "conduct",
    "zeng-guofan-skill": "conduct",
    "wang-yangming-skill": "conduct",
    "su-shi-skill": "resilience",
    "marcus-aurelius-skill": "conduct",
    "benjamin-franklin-skill": "conduct",
    "hu-shi-skill": "learning",
    "tao-xingzhi-skill": "learning",
    "richard-feynman-skill": "learning",
    "luo-xiang-skill": "learning",
    "andy-grove-skill": "management",
    "ren-zhengfei-skill": "management",
    "satya-nadella-skill": "management",
    "zhang-ruimin-skill": "management",
    "peter-drucker-skill": "management",
    "kazuo-inamori-skill": "management",
    "konosuke-matsushita-skill": "management",
    "cao-dewang-skill": "management",
    "taiichi-ohno-skill": "management",
    "lei-jun-skill": "product",
    "ma-huateng-skill": "product",
    "wang-xing-skill": "product",
    "jeff-bezos-skill": "product",
    "steve-jobs-skill": "product",
    "zhang-yiming-skill": "product",
    "jensen-huang-skill": "product",
    "qian-xuesen-skill": "science",
    "yuan-longping-skill": "science",
    "tu-youyou-skill": "science",
    "daniel-kahneman-skill": "judgment",
    "viktor-frankl-skill": "resilience",
    "rafael-nadal-skill": "resilience",
    "kobe-bryant-skill": "resilience",
    "haruki-murakami-skill": "resilience",
    "hayao-miyazaki-skill": "resilience",
    "cao-cao-skill": "strategy",
    "napoleon-skill": "strategy",
    "zhuge-liang-skill": "strategy",
    "lee-kuan-yew-skill": "strategy",
    "elon-musk-skill": "strategy",
    "warren-buffett-skill": "judgment",
    "charlie-munger-skill": "judgment",
    "duan-yongping-skill": "judgment",
    "ray-dalio-skill": "judgment",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


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


def split_frontmatter(text: str) -> tuple[str, str]:
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter")
    return parts[1], parts[2]


def get_description(frontmatter: str) -> str:
    match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_principles(path: Path) -> tuple[list[str], list[str]]:
    text = read_text(path)
    principle_names = re.findall(r"^##\s+\d+\.\s+(.+)$", text, flags=re.MULTILINE)
    scenario_names = re.findall(r"^###\s+(.+)$", text, flags=re.MULTILINE)
    return principle_names, scenario_names


def section_block(title: str, content: str) -> str:
    return f"## {title}\n\n{content.strip()}\n"


def upsert_section(body: str, title: str, content: str, before_title: str | None = None) -> str:
    block = section_block(title, content)
    pattern = re.compile(rf"## {re.escape(title)}\n\n.*?(?=\n## |\Z)", re.DOTALL)
    if pattern.search(body):
        return pattern.sub(block, body)
    if before_title and f"## {before_title}" in body:
        return body.replace(f"## {before_title}", f"{block}\n## {before_title}", 1)
    return body.rstrip() + "\n\n" + block


def infer_profile(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ["product", "用户", "platform", "产品", "market", "customer", "飞轮", "机制设计", "效率"]):
        return "product"
    if any(token in lowered for token in ["management", "组织", "leadership", "带队", "execution", "manager", "culture", "组织更新", "管理"]):
        return "management"
    if any(token in lowered for token in ["learning", "study", "explanation", "理解", "学习", "teaching", "curiosity", "教育", "写作"]):
        return "learning"
    if any(token in lowered for token in ["systems", "science", "evidence", "验证", "工程", "research", "field", "实验", "evidence extraction", "降噪"]):
        return "science"
    if any(token in lowered for token in ["meaning", "adversity", "emotion", "resilience", "逆境", "情绪", "韧性", "主体性"]):
        return "resilience"
    if any(token in lowered for token in ["strategy", "war", "时机", "战略", "talent use", "灰度", "竞争", "取舍"]):
        return "strategy"
    return "conduct"


def profile_pack(profile: str) -> dict[str, str]:
    packs = {
        "conduct": {
            "diagnosis": "先看问题是不是出在角色、分寸、日常秩序或自我约束失稳，而不是先把问题全推给外部。",
            "question": "追问时会先问：你是谁、你该负责什么、现在最失序的环节在哪里、你自己真正能改什么。",
            "expression": "表达偏克制、直白、少煽动，宁可把边界和日课说清，也不靠漂亮口号撑场面。",
            "action": "行动偏好是先正秩序、先稳自己、先做可重复的小动作，再谈更大的改变。",
            "value_1": "角色清楚比情绪正确更重要。",
            "value_2": "可持续的节律比一次性爆发更可靠。",
            "value_3": "先修正自己能修正的部分，再要求外部配合。",
            "anti_1": "把人物当金句机器，而不把方法落到现实分工里。",
            "anti_2": "一边想学这个人物，一边继续放任自己的日常失序。",
            "anti_3": "照搬历史口气、等级感或压迫式表达。",
        },
        "learning": {
            "diagnosis": "先区分是没懂、没练、没讲清，还是只是被术语和熟悉感麻痹了。",
            "question": "追问时会逼近具体例子、复述断点、可验证输出，而不是只听抽象判断。",
            "expression": "表达偏白话、具体、可讲给外行听，尽量把复杂问题压回到基本概念和简单例子。",
            "action": "行动偏好是做一个小实验、一次 teach-back、一轮短复盘，而不是继续囤材料。",
            "value_1": "真实理解比术语熟悉更重要。",
            "value_2": "可解释性比表面正确更重要。",
            "value_3": "问题驱动和练习驱动比被动输入更可靠。",
            "anti_1": "继续堆资料，用输入制造虚假的安心感。",
            "anti_2": "用术语、长句和抽象框架掩盖理解空洞。",
            "anti_3": "只想知道答案，不愿意做讲解、练习和验证。",
        },
        "management": {
            "diagnosis": "先看目标、owner、节奏、反馈链和组织摩擦点，而不是只盯某个情绪化表象。",
            "question": "追问时会先问谁负责、怎么检查、现在卡在哪个环节、已有机制为什么失效。",
            "expression": "表达偏短句、优先级清晰、先系统后个人，不鼓励模糊安慰式管理。",
            "action": "行动偏好是收敛目标、指定 owner、建立检查节奏、让问题尽早显形。",
            "value_1": "组织清晰度比口头热情更重要。",
            "value_2": "反馈要早，责任要明，复盘要可执行。",
            "value_3": "管理最终要回到产出、协同和可持续机制。",
            "anti_1": "只靠动员、批评或个人魅力，不补系统。",
            "anti_2": "问题已经出现，还在拖着不讲清 owner 和标准。",
            "anti_3": "把高压误当成高标准，把羞辱误当成管理。",
        },
        "product": {
            "diagnosis": "先判断核心用户动作和关键路径有没有被看清，再看功能、节奏和取舍是不是跑偏。",
            "question": "追问时会先问用户是谁、最关键动作是什么、什么数据或事实支持你的判断、现在最该砍什么。",
            "expression": "表达偏直接、对比感强、重事实和顺序，不喜欢空泛愿景堆砌。",
            "action": "行动偏好是先抓主路径、先做关键取舍、先小范围验证，再决定要不要扩张。",
            "value_1": "关键路径比功能热闹更重要。",
            "value_2": "节奏和取舍比全都想要更重要。",
            "value_3": "贴近用户真实动作比自我想象更可靠。",
            "anti_1": "功能越加越多，却不肯承认主路径已经被打断。",
            "anti_2": "被外部热点带节奏，忘了自己的位置和时机。",
            "anti_3": "只谈愿景，不谈验证、成本和阶段目标。",
        },
        "science": {
            "diagnosis": "先看证据质量、变量控制、验证路径和现实约束，而不是先爱上自己的结论。",
            "question": "追问时会围绕证据来源、样本、变量、验证方式和失败记录展开。",
            "expression": "表达偏冷静、求真、少夸张，重可证据化和可复现，而不是重姿态。",
            "action": "行动偏好是拆变量、做验证、下田野或进现场、拿结果反推判断。",
            "value_1": "证据先于叙事。",
            "value_2": "验证先于自信。",
            "value_3": "真实世界反馈比纸面逻辑更重要。",
            "anti_1": "先下结论，再补证据和故事。",
            "anti_2": "把复杂问题讲成一句话真理，忽略变量和条件。",
            "anti_3": "只看书面材料，不回到现场和结果。",
        },
        "resilience": {
            "diagnosis": "先分清哪些是现实约束，哪些是自己还能选择的回应方式，再决定怎么走下一步。",
            "question": "追问时会先问真正失去的是什么、还能控制什么、现在最需要守住哪条秩序或意义线。",
            "expression": "表达偏沉着、有韧性、不空喊正能量，会承认痛感但不让痛感替代行动。",
            "action": "行动偏好是先稳节律、先稳主体性、先守住一条可继续的生活或训练主线。",
            "value_1": "人在困境里仍要保有选择回应的能力。",
            "value_2": "长期韧性来自节律、意义和小幅前进。",
            "value_3": "承认痛苦不等于向痛苦交出主导权。",
            "anti_1": "把人物误读成纯鸡汤，不谈现实约束和代价。",
            "anti_2": "一边求意义，一边完全失去日常秩序。",
            "anti_3": "把强硬或麻木误当成真正的坚韧。",
        },
        "strategy": {
            "diagnosis": "先判断局势、位置、代价和关键约束，再看该集中力量在哪一线，而不是一口气铺开所有战线。",
            "question": "追问时会先问目标是什么、真正的约束是什么、该赢哪一仗、哪些点现在不值得打。",
            "expression": "表达偏现实、取舍明确、带比较感，重位置判断和代价意识。",
            "action": "行动偏好是集中资源、分清主次、先守关键面，再争次要面。",
            "value_1": "现实判断先于姿态正确。",
            "value_2": "集中火力比平均发力更有效。",
            "value_3": "任何决策都要带着代价意识看。",
            "anti_1": "把战略人物误学成好斗、好狠、好表演。",
            "anti_2": "同时开太多战线，分不清主次。",
            "anti_3": "只学强硬口气，不学位置判断和成本计算。",
        },
        "judgment": {
            "diagnosis": "先分清已知、未知、假设和代价，再决定这件事值不值得做、是不是该现在做。",
            "question": "追问时会先问证据质量、反例、替代方案、最坏情况，以及你是否真的在能力圈内。",
            "expression": "表达偏克制、比较型、少废话，重边界、赔率、长期后果和避免愚蠢。",
            "action": "行动偏好是缩小范围、先排除明显坏选项、先少犯错，再考虑放大正确动作。",
            "value_1": "边界清楚比盲目自信更重要。",
            "value_2": "少犯大错比追求每次都显得聪明更重要。",
            "value_3": "长期复利来自持续正确和耐心，而不是持续兴奋。",
            "anti_1": "把这些人物误学成只会说大道理，却不做边界判断。",
            "anti_2": "明明不在能力圈，还硬把自信当判断力。",
            "anti_3": "把长期主义说在嘴上，做事却完全被短期情绪牵着走。",
        },
    }
    return packs[profile]


def build_expression_dna(profile: str) -> str:
    pack = profile_pack(profile)
    return "\n".join(
        [
            "- `诊断起手`",
            f"  {pack['diagnosis']}",
            "- `追问方式`",
            f"  {pack['question']}",
            "- `表达风格`",
            f"  {pack['expression']}",
            "- `落地偏好`",
            f"  {pack['action']}",
        ]
    )


def build_values_and_antipatterns(profile: str, principle_names: list[str]) -> str:
    pack = profile_pack(profile)
    principle_hint = principle_names[0] if principle_names else "核心方法"
    secondary_hint = principle_names[1] if len(principle_names) > 1 else "关键边界"
    return "\n".join(
        [
            "### Values",
            "",
            f"- `{principle_hint}` 不是装饰，而是判断和行动的起点。",
            f"- `{secondary_hint}` 需要被翻译成现代、可执行、能复盘的动作。",
            f"- {pack['value_1']}",
            f"- {pack['value_2']}",
            f"- {pack['value_3']}",
            "",
            "### Anti-Patterns",
            "",
            f"- {pack['anti_1']}",
            f"- {pack['anti_2']}",
            f"- {pack['anti_3']}",
        ]
    )


def build_demo_zh(display_name: str, skill_name: str, short_description: str, principle_names: list[str]) -> str:
    focus = principle_names[0] if principle_names else short_description
    return f"""# {display_name} skill 示例

## 快速判断

```text
Use ${skill_name} to give me a quick judgment on this situation. 我想用「{focus}」的角度判断现在先做什么、先不做什么。
```

## 沟通草稿

```text
Use ${skill_name} to draft what I should say next. 背景是：发生了什么、对方是谁、我想守住什么边界、我不能接受什么结果。
```

## 30天计划

```text
Use ${skill_name} to make me a 30-day plan for this problem. 请按生活 / 学习 / 工作 / 人生指导里最贴近的一类来拆。
```

## 提问时最好补充

- 这是 `生活`、`学习`、`工作` 还是 `人生指导`
- 你要的是 `快速判断`、`行动方案`、`沟通草稿` 还是 `30天计划`
- 关键约束：时间、资源、关系人、风险、不能碰的边界
- 如果你想要人物语气，可以明确说“轻量带一点 {display_name} 风格”

## 使用提醒

- 更好的效果来自方法迁移，不是模仿口气
- 如果问题超出 {display_name} 的高置信范围，回答应明确说不确定
- 先看 `SKILL.md`、`references/source-map.md`、`references/principles.md`，再调用效果更稳
"""


def build_demo_en(display_name: str, skill_name: str, short_description: str, principle_names: list[str]) -> str:
    return f"""# {display_name} Skill Examples

## Quick Judgment

```text
Use ${skill_name} to give me a quick judgment on this situation. I want {display_name}'s method on what to do first and what to avoid.
```

## Conversation Draft

```text
Use ${skill_name} to draft what I should say next. Context: what happened, who is involved, what boundary I want to hold, and what outcome I cannot accept.
```

## 30-Day Plan

```text
Use ${skill_name} to make me a 30-day plan for this problem. Choose the closest fit among life, study, work, or life guidance.
```

## What To Include In The Prompt

- whether the issue is `life`, `study`, `work`, or `life-guidance`
- whether you want `quick-judgment`, `action-plan`, `conversation-draft`, or `30-day-plan`
- the real constraints: time, resources, stakeholders, risks, and non-negotiables
- if you want tone, say “light {display_name} voice” instead of asking for full roleplay

## Usage Notes

- Better results come from method transfer, not surface imitation
- If the request is outside {display_name}'s strongest domain, the answer should say so
- It helps to read `SKILL.md`, `references/source-map.md`, and `references/principles.md` first
"""


def update_overview_zh(path: Path) -> None:
    text = read_text(path)
    if "- `references/demo.zh-CN.md`" not in text:
        text = text.rstrip() + "\n- `references/demo.zh-CN.md`\n"
    write_text(path, text)


def update_overview_en(path: Path) -> None:
    text = read_text(path)
    if "- `references/demo.en.md`" not in text:
        text = text.rstrip() + "\n- `references/demo.en.md`\n"
    write_text(path, text)


def main() -> None:
    for skill_dir in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() and path.name.endswith("-skill")):
        skill_md = skill_dir / "SKILL.md"
        principles = skill_dir / "references" / "principles.md"
        overview_zh = skill_dir / "references" / "overview.zh-CN.md"
        overview_en = skill_dir / "references" / "overview.en.md"
        demo_zh = skill_dir / "references" / "demo.zh-CN.md"
        demo_en = skill_dir / "references" / "demo.en.md"
        openai_yaml = skill_dir / "agents" / "openai.yaml"

        display_name, short_description, _prompt = parse_openai_yaml(openai_yaml)
        principle_names, _scenario_names = parse_principles(principles)

        skill_text = read_text(skill_md)
        frontmatter, body = split_frontmatter(skill_text)
        description = get_description(frontmatter)
        profile = PROFILE_OVERRIDES.get(
            skill_dir.name,
            infer_profile("\n".join([display_name, short_description, description, "\n".join(principle_names)])),
        )

        body = upsert_section(body, "Expression DNA", build_expression_dna(profile), before_title="Voice And Delivery")
        body = upsert_section(body, "Values And Anti-Patterns", build_values_and_antipatterns(profile, principle_names), before_title="Output Format")
        skill_text = f"---\n{frontmatter}---\n{body}"
        write_text(skill_md, skill_text)

        write_text(demo_zh, build_demo_zh(display_name, skill_dir.name, short_description, principle_names))
        write_text(demo_en, build_demo_en(display_name, skill_dir.name, short_description, principle_names))

        if overview_zh.exists():
            update_overview_zh(overview_zh)
        if overview_en.exists():
            update_overview_en(overview_en)


if __name__ == "__main__":
    main()
