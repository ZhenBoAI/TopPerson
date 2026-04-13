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


def parse_openai_yaml(path: Path) -> tuple[str, str]:
    text = read_text(path)
    display = re.search(r'display_name:\s*"([^"]+)"', text)
    short = re.search(r'short_description:\s*"([^"]+)"', text)
    return (
        display.group(1) if display else path.parents[1].name,
        short.group(1) if short else "",
    )


def english_name_from_skill(skill_name: str) -> str:
    base = skill_name.removesuffix("-skill")
    return " ".join(part.capitalize() for part in base.split("-"))


def split_frontmatter(text: str) -> tuple[str, str]:
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter")
    return parts[1], parts[2]


def get_description(frontmatter: str) -> str:
    match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_english_summary(description: str, fallback: str) -> str:
    match = re.search(r"Use when Codex needs (.+?)(?: Also use when|$)", description)
    if match:
        return match.group(1).strip().rstrip(".")
    return to_english_text(fallback)


def parse_principles(path: Path) -> list[str]:
    text = read_text(path)
    return re.findall(r"^##\s+\d+\.\s+(.+)$", text, flags=re.MULTILINE)


def parse_section_bullets(text: str, title: str) -> list[str]:
    pattern = re.compile(rf"##\s+{re.escape(title)}\n\n(.*?)(?=\n## |\Z)", re.DOTALL)
    match = pattern.search(text)
    if not match:
        return []
    section = match.group(1)
    bullets = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
    return bullets


def infer_profile(skill_name: str, text: str) -> str:
    if skill_name in PROFILE_OVERRIDES:
        return PROFILE_OVERRIDES[skill_name]
    lowered = text.lower()
    if any(token in lowered for token in ["product", "用户", "platform", "产品", "market", "customer", "飞轮", "机制设计", "效率"]):
        return "product"
    if any(token in lowered for token in ["management", "组织", "leadership", "带队", "execution", "manager", "culture", "管理"]):
        return "management"
    if any(token in lowered for token in ["learning", "study", "explanation", "理解", "学习", "teaching", "curiosity", "教育", "写作"]):
        return "learning"
    if any(token in lowered for token in ["systems", "science", "evidence", "验证", "工程", "research", "field", "实验"]):
        return "science"
    if any(token in lowered for token in ["meaning", "adversity", "emotion", "resilience", "逆境", "情绪", "韧性", "主体性"]):
        return "resilience"
    if any(token in lowered for token in ["strategy", "war", "时机", "战略", "talent use", "灰度", "竞争", "取舍"]):
        return "strategy"
    if any(token in lowered for token in ["judgment", "decision", "noise", "bias", "投资", "能力圈", "降噪", "长期决策"]):
        return "judgment"
    return "conduct"


def profile_pack(profile: str) -> dict[str, list[str] | str]:
    packs = {
        "conduct": {
            "modern_zh": "现代转译时，重点保留角色责任、分寸、节律和自我修正，去掉权威崇拜与过度道德化。",
            "modern_en": "In modern translation, keep role responsibility, proportion, rhythm, and self-correction; drop authority worship and moral grandstanding.",
            "questions_zh": [
                "哪些判断其实来自角色混乱，而不是立场对立？",
                "哪些原则可以从修身语言翻译成现代日常规则？",
                "哪些说法属于后世道德化包装，而不是稳定原典？",
            ],
            "questions_en": [
                "Which judgments are really about role confusion rather than value conflict?",
                "Which principles can be translated from cultivation language into modern daily rules?",
                "Which claims are later moral packaging rather than stable primary-corpus patterns?",
            ],
            "misread_zh": [
                "把人物误学成只会讲道理，却不肯把责任和边界写清楚。",
                "把修身误读成压抑或服从，而不是更稳定的自我约束。",
            ],
            "misread_en": [
                "Reducing the person to moral talk while refusing to clarify roles and boundaries in real life.",
                "Misreading self-cultivation as suppression or obedience instead of steadier self-command.",
            ],
        },
        "learning": {
            "modern_zh": "现代转译时，重点保留解释力、练习、反馈和好问题，去掉神秘化天才叙事。",
            "modern_en": "In modern translation, keep explanation, practice, feedback, and good questions; drop the mystique of genius.",
            "questions_zh": [
                "哪些具体行为最能体现‘真懂’而不是‘看起来懂’？",
                "人物在教学、写作、对话里有哪些重复表达方式？",
                "哪些名言流传很广，但并不能代表其核心学习方法？",
            ],
            "questions_en": [
                "Which concrete behaviors best show real understanding rather than the appearance of understanding?",
                "What repeated patterns appear in this person's teaching, writing, and dialogue?",
                "Which famous quotes travel widely but do not actually represent the core learning method?",
            ],
            "misread_zh": [
                "把人物误读成只靠灵感或聪明，而忽略练习和解释的硬功夫。",
                "把白话表达误解成浅薄，而不是理解到位后的简洁。",
            ],
            "misread_en": [
                "Treating the person as if they relied on inspiration or raw brilliance while ignoring practice and explanation.",
                "Mistaking plain language for shallowness instead of clarity earned through understanding.",
            ],
        },
        "management": {
            "modern_zh": "现代转译时，重点保留 owner、节奏、反馈和系统思维，去掉羞辱式管理和个人崇拜。",
            "modern_en": "In modern translation, keep ownership, cadence, feedback, and systems thinking; drop humiliation-based management and personality cults.",
            "questions_zh": [
                "这个人物在哪些组织时刻最能体现其管理方法？",
                "哪些动作是机制建设，哪些只是强人格施压？",
                "成熟期与高压期的管理方式有什么不同？",
            ],
            "questions_en": [
                "Which organizational moments best reveal this person's management method?",
                "Which moves are system-building and which are just pressure from strong personality?",
                "How does the mature-period method differ from the crisis-period method?",
            ],
            "misread_zh": [
                "把高压误学成高标准，把苛刻误学成有效管理。",
                "只学人物的态度和金句，不学机制、节奏和复盘。",
            ],
            "misread_en": [
                "Mistaking pressure for standards and harshness for effective management.",
                "Copying attitude and slogans while ignoring mechanisms, cadence, and review loops.",
            ],
        },
        "product": {
            "modern_zh": "现代转译时，重点保留用户动作、关键路径、节奏与取舍，避免把人物神化成‘天生会判断’。",
            "modern_en": "In modern translation, keep user actions, critical paths, timing, and trade-offs; avoid turning the person into a myth of natural product intuition.",
            "questions_zh": [
                "哪些公开案例最能说明他如何做取舍？",
                "产品判断背后依赖了什么数据、观察或长期结构？",
                "哪些结论其实只适合平台型公司，不适合普通个人？",
            ],
            "questions_en": [
                "Which public cases best show how this person made trade-offs?",
                "What data, observation, or long-cycle structure sat behind the product judgment?",
                "Which conclusions only fit platform-scale companies and do not transfer cleanly to ordinary users?",
            ],
            "misread_zh": [
                "只学愿景表达，不学阶段判断和砍功能的勇气。",
                "把节奏感误学成保守，或把激进误学成产品判断。",
            ],
            "misread_en": [
                "Copying vision talk while ignoring stage judgment and the courage to cut scope.",
                "Mistaking pacing for timidity or aggression for product judgment.",
            ],
        },
        "science": {
            "modern_zh": "现代转译时，重点保留证据、变量、验证和现场反馈，去掉结果论英雄的叙事捷径。",
            "modern_en": "In modern translation, keep evidence, variables, verification, and field feedback; drop success-only storytelling shortcuts.",
            "questions_zh": [
                "哪些材料最能证明这个人物如何做验证，而不是如何讲故事？",
                "人物在失败、反复试验和修正中留下了什么痕迹？",
                "哪些广为流传的成功叙事压平了真实研究过程？",
            ],
            "questions_en": [
                "Which materials best show how this person verified rather than narrated?",
                "What traces did failure, repeated experiments, and correction leave behind?",
                "Which popular success stories flatten the real research process?",
            ],
            "misread_zh": [
                "只学最后成功的结果，不学长期试验和反复验证。",
                "把科学人物误读成‘靠直觉猜对’，忽略证据处理过程。",
            ],
            "misread_en": [
                "Learning only from the final success instead of long experimentation and repeated verification.",
                "Misreading scientific figures as people who guessed right by intuition while ignoring evidence work.",
            ],
        },
        "resilience": {
            "modern_zh": "现代转译时，重点保留主体性、节律、意义和长期耐力，避免把苦难本身神圣化。",
            "modern_en": "In modern translation, keep agency, rhythm, meaning, and long endurance; avoid sanctifying suffering itself.",
            "questions_zh": [
                "人物在困境里具体保住了什么秩序、训练或意义线？",
                "哪些表达是在承认痛苦，哪些表达是在重新夺回主动性？",
                "哪些外界叙事把人物简化成励志模板？",
            ],
            "questions_en": [
                "What order, training line, or meaning line did the person actually preserve inside hardship?",
                "Which expressions admit pain and which expressions reclaim agency?",
                "Which outside narratives reduce the person to a motivational template?",
            ],
            "misread_zh": [
                "把人物误学成纯鸡汤，不谈代价、边界和现实条件。",
                "把强撑、麻木或逞强错当成真正的韧性。",
            ],
            "misread_en": [
                "Turning the person into pure inspiration while avoiding cost, boundaries, and reality conditions.",
                "Mistaking strain, numbness, or performative toughness for actual resilience.",
            ],
        },
        "strategy": {
            "modern_zh": "现代转译时，重点保留位置判断、主次取舍、成本意识和集中力量，去掉权谋美化。",
            "modern_en": "In modern translation, keep position judgment, prioritization, cost awareness, and concentration of force; remove romance around power games.",
            "questions_zh": [
                "这个人物在哪些关键局面里最能体现主次判断？",
                "哪些看似强硬的动作，本质上依赖更深的现实判断？",
                "哪些流行印象把人物简化成‘狠’而不是‘会算账’？",
            ],
            "questions_en": [
                "Which key situations best reveal the person's sense of priority?",
                "Which apparently hard-line moves actually depended on deeper realism?",
                "Which popular impressions reduce the person to toughness instead of calculation?",
            ],
            "misread_zh": [
                "只学强硬口气，不学位置、代价和时机判断。",
                "把战略人物浪漫化成权谋导师，而不是现实取舍者。",
            ],
            "misread_en": [
                "Copying the hard tone while ignoring position, cost, and timing judgment.",
                "Romanticizing strategic figures into power-game mentors instead of real trade-off thinkers.",
            ],
        },
        "judgment": {
            "modern_zh": "现代转译时，重点保留边界、反偏差、长期赔率和避免大错，避免把人物写成万能导师。",
            "modern_en": "In modern translation, keep boundaries, debiasing, long-run odds, and mistake avoidance; avoid writing the person as an all-purpose guru.",
            "questions_zh": [
                "哪些材料最能体现其如何处理不确定性与边界？",
                "人物在面对反例和失败判断时是如何修正的？",
                "哪些流行总结过度简化了其判断框架？",
            ],
            "questions_en": [
                "Which materials best show how this person handled uncertainty and boundaries?",
                "How did the person correct course in the face of counterexamples and failed judgment?",
                "Which popular summaries oversimplify the judgment framework?",
            ],
            "misread_zh": [
                "把人物误读成永远正确，而不是擅长少犯大错。",
                "只学结论，不学能力圈、概率和等待机制。",
            ],
            "misread_en": [
                "Treating the person as always right instead of someone skilled at avoiding large mistakes.",
                "Copying conclusions while ignoring circle-of-competence, probability, and waiting mechanisms.",
            ],
        },
    }
    return packs[profile]


def to_english_text(text: str) -> str:
    replacements = [
        ("《", "\""),
        ("》", "\""),
        ("：", ": "),
        ("；", "; "),
        ("、", ", "),
        ("。", "."),
        ("相关公开演讲与文章", "related public talks and articles"),
        ("公开演讲与文章", "public talks and articles"),
        ("管理研究、企业案例、传记", "management studies, company cases, and biographies"),
        ("管理研究, 企业案例, 传记", "management studies, company cases, and biographies"),
        ("企业案例研究、媒体长访谈", "business case studies and long-form media interviews"),
        ("传记、投资与决策研究", "biographies and studies on investing and judgment"),
        ("传记, 投资与决策研究", "biographies and studies on investing and judgment"),
        ("三国史研究、人物传记、制度背景研究", "Three Kingdoms studies, biographies, and institutional background research"),
        ("儒家思想史研究与学术导读", "histories of Confucian thought and academic guides"),
        ("孔子传记、先秦思想研究和可靠注释本", "biographies of Confucius, studies of early Chinese thought, and reliable annotated editions"),
        ("孔子传记, 先秦思想研究和可靠注释本", "biographies of Confucius, studies of early Chinese thought, and reliable annotated editions"),
        ("自传与公开口述材料", "autobiographies and public oral-history material"),
        ("采访、演讲与企业公开表达", "interviews, speeches, and public company materials"),
        ("制造业经营相关公开案例", "public cases on industrial operations"),
        ("先秦相关史料与注疏传统", "early Chinese historical materials and commentary traditions"),
        ("用于补充秩序、修身和礼的语境", "used to supplement the context of order, self-cultivation, and ritual propriety"),
        ("用于补充秩序, 修身和礼的语境", "used to supplement the context of order, self-cultivation, and ritual propriety"),
        ("用于识别哪些理解更稳妥", "used to identify more stable interpretations"),
        ("了解孔子关于修身、学习、待人和角色责任的最核心材料", "the core material for understanding Confucius on self-cultivation, learning, conduct toward others, and role responsibility"),
        ("了解孔子关于修身, 学习, 待人和角色责任的最核心材料", "the core material for understanding Confucius on self-cultivation, learning, conduct toward others, and role responsibility"),
        ("后世过度道德化、口号化的“圣人语录”需要降权", "later moralized slogan-like 'sage quotes' should be downgraded"),
        ("后世过度道德化, 口号化的\"圣人语录\"需要降权", "later moralized slogan-like 'sage quotes' should be downgraded"),
        ("把孔子简单讲成服从权威或空泛说教，通常不可靠", "simple readings of Confucius as obedience to authority or empty preaching are usually unreliable"),
        ("不要把高压风格当成普适文化", "do not treat high-pressure style as universal culture"),
        ("要把偏执转成预警机制而不是焦虑", "turn paranoia into an early-warning mechanism rather than anxiety"),
        ("related整理本与研究文字", "related edited collections and studies"),
        ("related studies such as传记与分析", "related studies such as biographies and analysis"),
        ("Other modern研究、家书导读、年谱、学术论文", "other modern studies, reading guides, chronologies, and scholarly papers"),
        ("Other modern研究, 家书导读, 年谱, 学术论文", "other modern studies, reading guides, chronologies, and scholarly papers"),
        ("用曾国藩的修身、识人、处事框架分析问题并给出行动建议", "Zeng Guofan style advice for self-discipline, judging people, handling affairs, and actionable execution"),
        ("用曾国藩的修身, 识人, 处事框架分析问题并给出行动建议", "Zeng Guofan style advice for self-discipline, judging people, handling affairs, and actionable execution"),
        ("按Andy Grove的方法论分析问题并给出可执行建议", "Andy Grove style advice for management, paranoia, crisis awareness, and execution systems"),
        ("按孔子的修身、学习与角色责任方法分析问题并给出建议", "Confucius style advice for self-cultivation, learning, and role responsibility"),
        ("按孔子的修身, 学习与角色责任方法分析问题并给出建议", "Confucius style advice for self-cultivation, learning, and role responsibility"),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    result = re.sub(r"\s+", " ", result).strip()
    result = result.replace(" .", ".").replace(" ,", ",")
    return result


def build_zh(
    display_name: str,
    short_description: str,
    profile: str,
    primary: list[str],
    related: list[str],
    caution: list[str],
    principles: list[str],
) -> str:
    pack = profile_pack(profile)
    recurring = principles[:5] or [short_description]
    primary_lines = "\n".join(f"- {item}" for item in primary[:6]) or "- 当前以 source-map 里的 primary corpus 为准。"
    related_lines = "\n".join(f"- {item}" for item in related[:5]) or "- 当前以可靠传记、研究和长访谈做解释层补充。"
    caution_lines = "\n".join(f"- {item}" for item in caution[:5]) or "\n".join(f"- {item}" for item in pack["misread_zh"])
    recurring_lines = "\n".join(f"- `{item}`" for item in recurring)
    question_lines = "\n".join(f"- {item}" for item in pack["questions_zh"])
    return f"""# {display_name} 研究简报

## 当前蒸馏焦点

- {short_description}
- 这份简报的作用不是重复 `SKILL.md`，而是说明这个人物的高置信来源、反复出现的主题，以及下一轮补资料该往哪里继续挖。

## 高置信来源优先读什么

{primary_lines}

## 解释层材料可以补什么

{related_lines}

## 当前最反复出现的主题

{recurring_lines}

## 最容易被误学或误讲的地方

{caution_lines}

## 现代转译提醒

- {pack["modern_zh"]}

## 下一轮研究建议

{question_lines}
"""


def build_en(
    display_name: str,
    english_name: str,
    english_summary: str,
    profile: str,
    primary: list[str],
    related: list[str],
    caution: list[str],
    principles: list[str],
) -> str:
    pack = profile_pack(profile)
    recurring = principles[:5] or [english_summary]
    primary_lines = "\n".join(f"- {to_english_text(item)}" for item in primary[:6]) or "- Follow the primary corpus listed in `source-map.md` first."
    related_lines = "\n".join(f"- {to_english_text(item)}" for item in related[:5]) or "- Use biographies, long interviews, and credible studies as the interpretation layer."
    caution_lines = "\n".join(f"- {to_english_text(item)}" for item in caution[:5]) or "\n".join(f"- {item}" for item in pack["misread_en"])
    recurring_lines = "\n".join(f"- `{item}`" for item in recurring)
    question_lines = "\n".join(f"- {item}" for item in pack["questions_en"])
    return f"""# {display_name} Research Brief

## Current Distillation Focus

- {english_summary}
- This brief does not repeat `SKILL.md`. It shows the highest-confidence source base, recurring themes, and the next useful directions for deeper research.

## Primary Sources To Read First

{primary_lines}

## Interpretation Layer To Add

{related_lines}

## Themes That Keep Reappearing

{recurring_lines}

## Most Common Misreadings

{caution_lines}

## Modern Translation Note

- {pack["modern_en"]}

## Next Research Questions

{question_lines}
"""


def append_overview(path: Path, line: str) -> None:
    text = read_text(path)
    if line not in text:
        text = text.rstrip() + "\n" + line + "\n"
        write_text(path, text)


def main() -> None:
    for skill_dir in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() and path.name.endswith("-skill")):
        skill_md = skill_dir / "SKILL.md"
        source_map = skill_dir / "references" / "source-map.md"
        principles = skill_dir / "references" / "principles.md"
        overview_zh = skill_dir / "references" / "overview.zh-CN.md"
        overview_en = skill_dir / "references" / "overview.en.md"
        research_zh = skill_dir / "references" / "research.zh-CN.md"
        research_en = skill_dir / "references" / "research.en.md"
        openai_yaml = skill_dir / "agents" / "openai.yaml"

        display_name, short_description = parse_openai_yaml(openai_yaml)
        frontmatter, body = split_frontmatter(read_text(skill_md))
        description = get_description(frontmatter)
        english_name = english_name_from_skill(skill_dir.name)
        english_summary = extract_english_summary(description, short_description)
        profile = infer_profile(skill_dir.name, "\n".join([display_name, short_description, description, body]))

        source_text = read_text(source_map)
        primary = parse_section_bullets(source_text, "1. Primary Corpus")
        related = parse_section_bullets(source_text, "3. Related Works")
        caution = parse_section_bullets(source_text, "4. Popular Attributions And Caution")
        principle_names = parse_principles(principles)

        write_text(research_zh, build_zh(display_name, short_description, profile, primary, related, caution, principle_names))
        write_text(research_en, build_en(english_name, english_name, english_summary, profile, primary, related, caution, principle_names))

        if overview_zh.exists():
            append_overview(overview_zh, "- `references/research.zh-CN.md`")
        if overview_en.exists():
            append_overview(overview_en, "- `references/research.en.md`")


if __name__ == "__main__":
    main()
