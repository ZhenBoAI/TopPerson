[English](./README.md) | [简体中文](./README.zh-CN.md)

# 顶尖人 TopPerson

`TopPerson` 是一个开源的「人物方法论 skill 仓库」。

它不做名人语录收集，也不做人设崇拜，而是把人物的生平、原始著作、可信研究，整理成可以被 AI 调用的结构化 skill。

它想回答的问题是：

`如果按这个人的做事方式处理现实问题，会怎么判断、怎么取舍、怎么行动？`

## 目录

- [为什么做这个仓库](#为什么做这个仓库)
- [核心原则](#核心原则)
- [参考示例 Skill](#参考示例-skill)
- [人物 Skill 目录](#人物-skill-目录)
- [人物 Backlog](#人物-backlog)
- [快速开始](#快速开始)
- [贡献方式](#贡献方式)
- [仓库结构](#仓库结构)
- [自动校验](#自动校验)
- [License](#license)

## 为什么做这个仓库

很多人物内容在互联网上会被压缩成：

- 鸡汤金句
- 断章取义的“成功秘诀”
- 神秘化、戏剧化的人设标签

`TopPerson` 反过来做四件事：

- 回到来源
- 提炼方法
- 建立边界
- 变成可执行的 skill

## 核心原则

- `来源优先`
  一手资料优先，二手研究辅助，流行金句降权。
- `方法优先`
  不做人物简介，要做可复用的判断框架。
- `现代转译`
  历史人物的方法必须翻译到现代、合法、非伤害性的语境。
- `结构统一`
  让不同 skill 都能稳定被 AI 调用和复用。

## 参考示例 Skill

| Skill | 人物 | 作用 |
| --- | --- | --- |
| `zeng-guofan` | 曾国藩 | 用曾国藩的修身、识人、处事、带队框架分析现实问题 |

技能目录：

- [`zeng-guofan/SKILL.md`](./.agents/skills/zeng-guofan/SKILL.md)
- [`zeng-guofan/references/source-map.md`](./.agents/skills/zeng-guofan/references/source-map.md)
- [`zeng-guofan/references/principles.md`](./.agents/skills/zeng-guofan/references/principles.md)
- 可选说明：[`zeng-guofan/references/overview.zh-CN.md`](./.agents/skills/zeng-guofan/references/overview.zh-CN.md)
- 可选说明：[`zeng-guofan/references/overview.en.md`](./.agents/skills/zeng-guofan/references/overview.en.md)

`zeng-guofan` 仍然是当前最完整、最成熟的示例 skill。
人物 backlog 中列出的其他人物，现在也都已经在 [`.agents/skills`](./.agents/skills) 下生成了初版 skill。

## 人物 Skill 目录

当前仓库状态： [`.agents/skills`](./.agents/skills) 下已有 `33` 个 skill 目录。

### 成熟示例

`zeng-guofan`（曾国藩）

### 初版 Skill：P0 打磨优先级

`wang-yangming`（王阳明）、`su-shi`（苏轼）、`lei-jun`（雷军）、`duan-yongping`（段永平）、`ren-zhengfei`（任正非）、`cao-dewang`（曹德旺）、`kazuo-inamori`（稻盛和夫）、`warren-buffett`（巴菲特）、`charlie-munger`（查理·芒格）、`andy-grove`（安迪·格鲁夫）、`benjamin-franklin`（本杰明·富兰克林）、`richard-feynman`（理查德·费曼）

### 初版 Skill：P1 打磨优先级

`zhang-yiming`（张一鸣）、`jensen-huang`（黄仁勋）、`wang-xing`（王兴）、`luo-xiang`（罗翔）、`hayao-miyazaki`（宫崎骏）、`haruki-murakami`（村上春树）、`steve-jobs`（乔布斯）、`jeff-bezos`（贝索斯）、`konosuke-matsushita`（松下幸之助）、`peter-drucker`（彼得·德鲁克）、`rafael-nadal`（纳达尔）、`kobe-bryant`（科比）

### 初版 Skill：P2 打磨优先级

`elon-musk`（马斯克）、`jack-ma`（马云）、`cao-cao`（曹操）、`zhuge-liang`（诸葛亮）、`napoleon`（拿破仑）、`lee-kuan-yew`（李光耀）、`ray-dalio`（Ray Dalio）、`marcus-aurelius`（马可·奥勒留）

## 人物 Backlog

用于规划后续人物 skill 的仓库级文档：

- 英文版：[`docs/person-backlog.md`](./docs/person-backlog.md)
- 中文版：[`docs/person-backlog.zh-CN.md`](./docs/person-backlog.zh-CN.md)

这些 backlog 文档里的 `P0 / P1 / P2` 现在表示“后续打磨优先级”，而不是是否已经存在 skill 目录。

## 快速开始

### 1. 浏览技能

进入 [`.agents/skills`](./.agents/skills) 或先看上面的“人物 Skill 目录”查看已收录人物。

### 2. 调用技能

在支持 skill 的环境里，可以直接这样调用：

```text
Use $zeng-guofan to analyze this situation in 曾国藩式做事风格，并给出可执行建议。
```

### 3. 查看单个 skill 说明

skill 说明文档是可选的，可以放在 skill 自己的目录中。

推荐命名：

- `references/overview.zh-CN.md`
- `references/overview.en.md`

### 4. 本地校验

提交前运行：

```bash
python3 scripts/validate_skills.py
```

### 5. 从模板开始

新增人物 skill 时，直接参考：

- [`templates/person-skill/SKILL.md`](./templates/person-skill/SKILL.md)
- [`templates/person-skill/references/source-map.md`](./templates/person-skill/references/source-map.md)
- [`templates/person-skill/references/principles.md`](./templates/person-skill/references/principles.md)
- 可选说明：[`templates/person-skill/references/overview.zh-CN.md`](./templates/person-skill/references/overview.zh-CN.md)
- 可选说明：[`templates/person-skill/references/overview.en.md`](./templates/person-skill/references/overview.en.md)
- [`templates/person-skill/agents/openai.yaml`](./templates/person-skill/agents/openai.yaml)

## 贡献方式

欢迎大家提交更多人物 skill，例如历史人物、企业家、投资人、学者、管理者、或某个领域的顶尖实践者。

但请不要把仓库做成：

- 语录大全
- 神化人物的宣传材料
- 没有来源的“成功学”
- 鼓吹操控、压迫、洗脑、伪科学的方法库

开始贡献前，请先看：

- 中文指南：[`CONTRIBUTING.zh-CN.md`](./CONTRIBUTING.zh-CN.md)
- English guide: [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- 中文审查清单：[`docs/review-checklist.zh-CN.md`](./docs/review-checklist.zh-CN.md)
- English checklist: [`docs/review-checklist.md`](./docs/review-checklist.md)
- 中文 PR 模板：[`PULL_REQUEST_TEMPLATE.zh-CN.md`](./.github/PULL_REQUEST_TEMPLATE.zh-CN.md)
- English PR 模板：[`PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md)

## 仓库结构

```text
.agents/skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/
      source-map.md
      principles.md
      overview.zh-CN.md     # 可选
      overview.en.md        # 可选

docs/
  person-backlog.md
  person-backlog.zh-CN.md
  review-checklist.md
  review-checklist.zh-CN.md

scripts/
  validate_skills.py

templates/
  person-skill/
    SKILL.md
    agents/openai.yaml
    references/
      source-map.md
      principles.md
      overview.zh-CN.md     # 可选
      overview.en.md        # 可选
```

## 自动校验

仓库包含一个本地校验脚本和 GitHub Action：

- 本地运行：`python3 scripts/validate_skills.py`
- PR 自动运行：`.github/workflows/validate-skills.yml`

它会检查：

- skill 目录命名
- `SKILL.md` frontmatter
- 必需文件是否存在
- `openai.yaml` 的关键字段是否存在

可选的 `overview` 说明文件不会被强制要求。

## License

本仓库采用 [`MIT License`](./LICENSE)。

这意味着：

- 代码、脚本、结构和仓库组织方式可以自由复用
- 提交内容前请确认你有权贡献
- 不要直接搬运受版权保护的长篇原文
