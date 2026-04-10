# 顶尖人 TopPerson

`TopPerson` 是一个开源的「人物方法论 skill 仓库」。

它不做名人语录收集，也不做人物崇拜，而是把人物的生平、原始著作、可信研究，整理成可以被 AI 调用的结构化 skill，用来回答一个更实用的问题：

`如果按这个人的做事方式处理现实问题，会怎么判断、怎么取舍、怎么行动？`

## 为什么做这个仓库

很多人物内容在互联网上会被压缩成三种东西：

- 鸡汤金句
- 断章取义的“成功秘诀”
- 神秘化、人格化、戏剧化的标签

`TopPerson` 想做的是反过来的事情：

- 回到来源
- 提炼方法
- 建立边界
- 变成能真正帮助现实决策的 skill

## 仓库目标

- 沉淀可复用的 `topperson skills`
- 优先基于一手资料，而不是短视频式金句
- 把历史人物或现实人物的方法，翻译成现代、合法、可执行的行动建议
- 允许社区提交，但坚持统一的来源标准、结构标准、审查标准

## 核心原则

- `来源优先`
  一手资料优先，二手研究辅助，流行金句降权。
- `方法优先`
  不做人物简介，要做可复用的判断框架。
- `现代转译`
  历史人物的方法必须翻译到现代、合法、非伤害性的语境。
- `结构统一`
  让不同 skill 都能稳定被 AI 调用和复用。

## 当前已收录

| Skill | 人物 | 作用 |
| --- | --- | --- |
| `zeng-guofan` | 曾国藩 | 用曾国藩的修身、识人、处事、带队框架分析现实问题 |

技能目录：

- [`zeng-guofan/SKILL.md`](./.agents/skills/zeng-guofan/SKILL.md)
- [`zeng-guofan/references/source-map.md`](./.agents/skills/zeng-guofan/references/source-map.md)
- [`zeng-guofan/references/principles.md`](./.agents/skills/zeng-guofan/references/principles.md)

## 快速开始

### 1. 浏览 skill

进入 [`.agents/skills`](./.agents/skills) 查看已收录人物。

### 2. 调用 skill

在支持 skill 的环境里，你可以直接调用：

```text
Use $zeng-guofan to analyze this situation in 曾国藩式做事风格，并给出可执行建议。
```

### 3. 本地校验

提交前运行：

```bash
python3 scripts/validate_skills.py
```

### 4. 提交 PR

先看：

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`docs/review-checklist.md`](./docs/review-checklist.md)
- [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md)

### 5. 从模板开始

如果你要新增人物 skill，可以直接参考：

- [`templates/person-skill/SKILL.md`](./templates/person-skill/SKILL.md)
- [`templates/person-skill/references/source-map.md`](./templates/person-skill/references/source-map.md)
- [`templates/person-skill/references/principles.md`](./templates/person-skill/references/principles.md)
- [`templates/person-skill/agents/openai.yaml`](./templates/person-skill/agents/openai.yaml)

## 曾国藩 Skill 说明

### 这个 skill 做什么

这个 skill 把曾国藩的做事方式整理成一套现代可用框架，重点放在：

- 修身与自我整顿
- 团队治理与收拾烂摊子
- 识人、用人、分责
- 冲突处理与信任修复
- 长期工程的节奏控制
- 家庭、金钱、秩序与日常纪律

它不是为了模仿晚清权谋，也不是为了生产“成功学版曾国藩”。

### 参考了哪些内容

高优先级材料：

- `《曾国藩家书》`
- `《曾国藩日记》`
- `奏折、批牍、书信、读书札记、诗文`
- `《曾国藩全集》`

辅助解释材料：

- 唐浩明相关整理与研究
- 张宏杰相关传记与研究
- 年谱、导读、学术研究论文

低置信辅助材料：

- `《冰鉴》`
- `《挺经》`
- 网络流传的“曾国藩名言”与商业鸡汤式二次加工

这个仓库对来源的基本态度是：

`一手资料优先，二手研究辅助，流行金句降权。`

### 怎么使用

在支持 skill 调用的环境里，可以直接这样调用：

```text
Use $zeng-guofan to analyze this situation in 曾国藩式做事风格，并给出可执行建议。
```

也可以直接用自然语言触发：

- `按曾国藩的风格看，这个团队烂摊子该怎么收拾？`
- `如果是曾国藩，会怎么处理合作伙伴失信？`
- `用曾国藩的方法帮我定一个三十天自我整顿计划。`
- `我该不该现在辞职创业？请用曾国藩式做事法来判断。`

### 这个 skill 的输出风格

默认输出会尽量包含这些部分：

- `曾式总判`
- `先办什么`
- `暂不做什么`
- `今日 / 七日 / 三十日`
- `对人怎么说`
- `自省一问`

## 欢迎贡献

欢迎大家提交更多人物 skill，比如：

- 历史人物
- 企业家
- 投资人
- 学者
- 管理者
- 某个领域的顶尖实践者

但请不要把仓库做成：

- 语录大全
- 神化人物的宣传材料
- 没有来源的“成功学”
- 鼓吹操控、压迫、洗脑、伪科学的方法库

我们欢迎两类贡献：

- 直接提交新的 skill 或修正已有 skill
- 先通过 issue 提出人物候选、来源建议、争议材料核查点

## 仓库结构

```text
.agents/skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/
      source-map.md
      principles.md

docs/
  review-checklist.md

scripts/
  validate_skills.py

templates/
  person-skill/
    SKILL.md
    agents/openai.yaml
    references/
      source-map.md
      principles.md
```

## 自动校验

仓库包含一个本地校验脚本和 GitHub Action：

- 本地运行：`python3 scripts/validate_skills.py`
- PR 时自动运行：`.github/workflows/validate-skills.yml`

它会检查：

- skill 目录命名
- `SKILL.md` frontmatter
- 必需文件是否存在
- `openai.yaml` 的关键字段是否存在

## 审查原则

维护者会重点看 4 件事：

1. 来源是否靠谱
2. 方法是否真的可复用
3. 是否被翻译成现代、合法、非伤害性的建议
4. 结构是否统一，便于 AI 稳定调用

如果你愿意一起把这个仓库做成一个真正有质量的开源项目，欢迎直接提 PR。

## License

本仓库默认采用 [`MIT License`](./LICENSE)。

这意味着：

- 代码、脚本、结构和仓库组织方式可以自由复用
- 提交内容请确认你有权贡献
- 涉及受版权保护的长篇原文时，不要直接大段搬运
