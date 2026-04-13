[English](./README.md) | [简体中文](./README.zh-CN.md)

# 顶尖人 TopPerson

`TopPerson` 是一个开源的人物方法论 AI skill 仓库。

它要解决的问题很简单：

`遇到现实问题时，如果按某个顶尖人物的方式来判断、取舍和行动，会怎么做？`

## 目录

- [它能做什么](#它能做什么)
- [主要使用场景](#主要使用场景)
- [当前 Skill](#当前-skill)
- [蒸馏数据集](#蒸馏数据集)
- [蒸馏 Roadmap](#蒸馏-roadmap)
- [怎么使用](#怎么使用)
- [怎么提议新增 Skill](#怎么提议新增-skill)
- [贡献要求](#贡献要求)
- [校验方式](#校验方式)
- [License](#license)

## 它能做什么

TopPerson 会把人物的著作、书信、演讲、访谈、传记和可信研究，整理成可被 AI 调用的 skill。

这个仓库主要做三件事：

- 提炼人物的方法论
- 翻译成现代可执行建议
- 让 AI 能稳定调用

这个仓库不做：

- 语录合集
- 名人崇拜
- 空洞鸡汤
- 操控、伤害、伪科学内容

## 主要使用场景

你可以用 TopPerson 的 skill 来处理：

- `生活`：自律、习惯、情绪、长期节奏
- `学习`：理解、记忆、解释、练习、建立学习方法
- `工作`：执行、沟通、带队、管理、产品判断、决策
- `人生指导`：重大选择、低谷调整、方向判断、价值取舍

## 当前 Skill

当前仓库状态： [`.agents/skills`](./.agents/skills) 下已有 `45` 个 skill 目录。

### 参考示例

- [`曾国藩 / zeng-guofan-skill`](./.agents/skills/zeng-guofan-skill/SKILL.md)：晚清重臣与湘军领袖，常被用来讨论修身、带队和长期整顿。

### 其他已创建 Skill

- [`安迪·格鲁夫 / andy-grove-skill`](./.agents/skills/andy-grove-skill/SKILL.md)：Intel 前 CEO，以高标准管理、危机感和执行系统著称。
- [`本杰明·富兰克林 / benjamin-franklin-skill`](./.agents/skills/benjamin-franklin-skill/SKILL.md)：政治家、发明家、作家，常被视为习惯养成与自我改进的代表人物。
- [`曹操 / cao-cao-skill`](./.agents/skills/cao-cao-skill/SKILL.md)：三国政治家、军事家、诗人，代表现实判断、战略与用人。
- [`曹德旺 / cao-dewang-skill`](./.agents/skills/cao-dewang-skill/SKILL.md)：福耀玻璃创始人，代表实业经营、成本意识和务实执行。
- [`查理·芒格 / charlie-munger-skill`](./.agents/skills/charlie-munger-skill/SKILL.md)：投资人、巴菲特长期搭档，代表多元思维模型与“避免愚蠢”。
- [`段永平 / duan-yongping-skill`](./.agents/skills/duan-yongping-skill/SKILL.md)：企业家与投资人，代表长期主义、取舍和商业判断。
- [`马斯克 / elon-musk-skill`](./.agents/skills/elon-musk-skill/SKILL.md)：企业家，代表第一性原理、技术冒险和强边界判断。
- [`村上春树 / haruki-murakami-skill`](./.agents/skills/haruki-murakami-skill/SKILL.md)：日本小说家，代表节律、耐力和长期独立创作。
- [`宫崎骏 / hayao-miyazaki-skill`](./.agents/skills/hayao-miyazaki-skill/SKILL.md)：日本动画导演，代表创作标准、工匠纪律和长期创作。
- [`马云 / jack-ma-skill`](./.agents/skills/jack-ma-skill/SKILL.md)：企业家与演讲者，代表表达、市场教育和组织动员。
- [`贝索斯 / jeff-bezos-skill`](./.agents/skills/jeff-bezos-skill/SKILL.md)：Amazon 创始人，代表用户导向、飞轮思维和长期建设。
- [`黄仁勋 / jensen-huang-skill`](./.agents/skills/jensen-huang-skill/SKILL.md)：NVIDIA 创始人，代表长期研发、技术战略和创始人领导力。
- [`稻盛和夫 / kazuo-inamori-skill`](./.agents/skills/kazuo-inamori-skill/SKILL.md)：京瓷创始人，代表经营、自律、利他和长期组织建设。
- [`科比 / kobe-bryant-skill`](./.agents/skills/kobe-bryant-skill/SKILL.md)：篮球运动员，代表纪律、刻意练习和竞争标准。
- [`松下幸之助 / konosuke-matsushita-skill`](./.agents/skills/konosuke-matsushita-skill/SKILL.md)：松下电器创始人，代表经营哲学、育人和长期企业建设。
- [`李光耀 / lee-kuan-yew-skill`](./.agents/skills/lee-kuan-yew-skill/SKILL.md)：新加坡建国总理，代表长期规划、制度设计和现实取舍。
- [`雷军 / lei-jun-skill`](./.agents/skills/lei-jun-skill/SKILL.md)：企业家与产品型创始人，代表产品判断、效率、执行和真诚表达。
- [`罗翔 / luo-xiang-skill`](./.agents/skills/luo-xiang-skill/SKILL.md)：法学教师与普法讲者，代表原则推理、边界意识和公开解释。
- [`马可·奥勒留 / marcus-aurelius-skill`](./.agents/skills/marcus-aurelius-skill/SKILL.md)：古罗马皇帝与斯多葛代表人物，代表自我克制、情绪调节和责任感。
- [`拿破仑 / napoleon-skill`](./.agents/skills/napoleon-skill/SKILL.md)：法国军事与政治人物，代表战略、时机和集中力量。
- [`彼得·德鲁克 / peter-drucker-skill`](./.agents/skills/peter-drucker-skill/SKILL.md)：现代管理学代表人物，代表管理、目标和知识工作效率。
- [`纳达尔 / rafael-nadal-skill`](./.agents/skills/rafael-nadal-skill/SKILL.md)：网球运动员，代表稳定性、韧性和低失误执行。
- [`Ray Dalio / ray-dalio-skill`](./.agents/skills/ray-dalio-skill/SKILL.md)：桥水创始人，代表原则、系统化决策和反馈回路。
- [`任正非 / ren-zhengfei-skill`](./.agents/skills/ren-zhengfei-skill/SKILL.md)：华为创始人，代表危机意识、生存、组织和灰度管理。
- [`理查德·费曼 / richard-feynman-skill`](./.agents/skills/richard-feynman-skill/SKILL.md)：物理学家与科普讲者，代表学习、理解、解释和好奇心。
- [`乔布斯 / steve-jobs-skill`](./.agents/skills/steve-jobs-skill/SKILL.md)：Apple 共同创始人，代表产品品味、聚焦和高标准。
- [`苏轼 / su-shi-skill`](./.agents/skills/su-shi-skill/SKILL.md)：宋代文学家、书法家、官员，代表逆境弹性、情绪平衡和人生秩序。
- [`王兴 / wang-xing-skill`](./.agents/skills/wang-xing-skill/SKILL.md)：美团创始人，代表竞争判断、战略聚焦和组织扩张。
- [`王阳明 / wang-yangming-skill`](./.agents/skills/wang-yangming-skill/SKILL.md)：明代思想家、军事家，代表知行合一、行动和内耗治理。
- [`巴菲特 / warren-buffett-skill`](./.agents/skills/warren-buffett-skill/SKILL.md)：长期投资代表人物，代表能力圈、长期决策和耐心。
- [`张一鸣 / zhang-yiming-skill`](./.agents/skills/zhang-yiming-skill/SKILL.md)：字节跳动创始人，代表理性决策、信息处理和机制设计。
- [`诸葛亮 / zhuge-liang-skill`](./.agents/skills/zhuge-liang-skill/SKILL.md)：三国政治家、军事家，代表规划纪律、勤勉和尽责执行。

### 本轮新增 Draft Skills

- [`孔子 / confucius-skill`](./.agents/skills/confucius-skill/SKILL.md)：先秦思想家与教育者，代表修身、学习、角色责任与日常秩序。
- [`胡适 / hu-shi-skill`](./.agents/skills/hu-shi-skill/SKILL.md)：现代思想家与写作者，代表证据意识、怀疑精神和清楚表达。
- [`陶行知 / tao-xingzhi-skill`](./.agents/skills/tao-xingzhi-skill/SKILL.md)：教育家，代表教学做合一与实践成长。
- [`钱学森 / qian-xuesen-skill`](./.agents/skills/qian-xuesen-skill/SKILL.md)：科学家与工程家，代表系统思维和复杂工程综合判断。
- [`袁隆平 / yuan-longping-skill`](./.agents/skills/yuan-longping-skill/SKILL.md)：农业科学家，代表田野验证、长期试验和务实科研。
- [`屠呦呦 / tu-youyou-skill`](./.agents/skills/tu-youyou-skill/SKILL.md)：科学家，代表证据提取、安静求真和耐心验证。
- [`马化腾 / ma-huateng-skill`](./.agents/skills/ma-huateng-skill/SKILL.md)：腾讯创始人，代表产品克制、节奏判断与平台思维。
- [`张瑞敏 / zhang-ruimin-skill`](./.agents/skills/zhang-ruimin-skill/SKILL.md)：海尔管理者，代表问责、自我颠覆和组织变革。
- [`维克多·弗兰克尔 / viktor-frankl-skill`](./.agents/skills/viktor-frankl-skill/SKILL.md)：精神科医生与思想家，代表意义感、主体性和困境应对。
- [`大野耐一 / taiichi-ohno-skill`](./.agents/skills/taiichi-ohno-skill/SKILL.md)：丰田生产方式代表人物，代表去浪费、现场观察和流程优化。
- [`萨提亚·纳德拉 / satya-nadella-skill`](./.agents/skills/satya-nadella-skill/SKILL.md)：微软 CEO，代表共情、学习型文化和组织更新。
- [`丹尼尔·卡尼曼 / daniel-kahneman-skill`](./.agents/skills/daniel-kahneman-skill/SKILL.md)：心理学家，代表偏差识别、决策卫生和降噪。

更多规划可看：

- 英文 backlog：[`docs/person-backlog.md`](./docs/person-backlog.md)
- 中文 backlog：[`docs/person-backlog.zh-CN.md`](./docs/person-backlog.zh-CN.md)

## 蒸馏数据集

如果你想继续扩充到更大的人物池，可以直接看这套 100+ 结构化数据：

- 英文说明：[`docs/person-catalog.md`](./docs/person-catalog.md)
- 中文说明：[`docs/person-catalog.zh-CN.md`](./docs/person-catalog.zh-CN.md)
- JSON 数据：[`data/person-catalog.json`](./data/person-catalog.json)

## 蒸馏 Roadmap

如果你不想直接看完整人物池，而是想看“下一批该先做谁”，可以直接看：

- 英文 roadmap：[`docs/person-roadmap.md`](./docs/person-roadmap.md)
- 中文 roadmap：[`docs/person-roadmap.zh-CN.md`](./docs/person-roadmap.zh-CN.md)

## 怎么使用

### 1. 先选人物

进入 [`.agents/skills`](./.agents/skills) 选择一个人物。

### 2. 直接调用

例如：

```text
Use $zeng-guofan-skill to analyze this situation and give me actionable advice.
```

### 3. 按问题场景去问

例如：

```text
Use $wang-yangming-skill to help me stop overthinking and start acting.
Use $richard-feynman-skill to help me learn this topic clearly.
Use $lei-jun-skill to help me judge this product direction.
Use $duan-yongping-skill to help me decide whether this opportunity is worth doing.
```

### 4. 指定任务模式

大多数人物 skill 现在都支持这四种常用模式：

- `快速判断`
- `行动方案`
- `沟通草稿`
- `30天计划`

例如：

```text
Use $zeng-guofan-skill to give me a quick judgment on this team problem.
Use $confucius-skill to draft what I should say in this conflict.
Use $richard-feynman-skill to make me a 30-day learning plan for this topic.
```

### 5. 看内置示例

很多 skill 现在会带这些参考文件：

- `references/demo.en.md`
- `references/demo.zh-CN.md`
- `references/research.en.md`
- `references/research.zh-CN.md`

它们适合用来看“问题该怎么问”以及“更强的输出大概长什么样”。

## 怎么提议新增 Skill

如果你想新增一个人物 skill，建议按这个最短路径来：

1. 先选一个资料足够扎实的人物。
2. 说明普通人为什么能用这个人的方法。
3. 写清这个 skill 主要解决什么问题。
4. 列出一手资料和二手资料。
5. 提 issue 或直接发 PR。

相关入口：

- [`CONTRIBUTING.zh-CN.md`](./CONTRIBUTING.zh-CN.md)
- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`docs/review-checklist.zh-CN.md`](./docs/review-checklist.zh-CN.md)
- [`docs/review-checklist.md`](./docs/review-checklist.md)

推荐从这些模板开始：

- [`templates/person-skill/SKILL.md`](./templates/person-skill/SKILL.md)
- [`templates/person-skill/references/source-map.md`](./templates/person-skill/references/source-map.md)
- [`templates/person-skill/references/principles.md`](./templates/person-skill/references/principles.md)
- [`templates/person-skill/agents/openai.yaml`](./templates/person-skill/agents/openai.yaml)

## 贡献要求

好的贡献应该满足：

- 有来源
- 有方法论
- 能现代转译
- 能被 AI 稳定调用

请避免：

- 语录堆砌
- 神化人物
- 伪史料和伪引文
- 非法、欺骗、操控、伤害性建议

## 校验方式

发 PR 前运行：

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_person_catalog.py
python3 scripts/validate_skill_content.py
```

## License

本仓库采用 [`MIT License`](./LICENSE)。
