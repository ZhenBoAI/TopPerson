# Contributing

欢迎为 `顶尖人 TopPerson` 提交新的 skill 或改进现有 skill。

这个仓库接收的不是普通文章，而是可被 AI 调用的结构化人物方法论 skill。所以我们更看重：

- 来源质量
- 方法抽象能力
- 结构一致性
- 现代适配能力

## 适合提交什么

适合：

- 某个历史人物的做事方法 skill
- 某个现代人物的决策风格 skill
- 对现有 skill 的来源补强、结构优化、错误纠正
- 更清晰的参考资料整理

不适合：

- 单纯的人物简介
- 没有方法论抽象的传记摘要
- 没有来源支撑的名言合集
- 含明显伪科学、相术、操控术、PUA、违法建议的内容

## 一个合格 skill 的最低结构

每个 skill 建议放在：

```text
.agents/skills/<skill-name>/
```

最低必需文件：

```text
.agents/skills/<skill-name>/SKILL.md
.agents/skills/<skill-name>/agents/openai.yaml
.agents/skills/<skill-name>/references/source-map.md
.agents/skills/<skill-name>/references/principles.md
```

说明：

- `SKILL.md`
  主 skill 文件，写清楚 skill 做什么、何时触发、怎么输出。
- `references/source-map.md`
  写清楚来源层级，一手资料、二手资料、低置信资料如何排序。
- `references/principles.md`
  把人物方法论翻译成现代可执行原则。
- `agents/openai.yaml`
  用于 UI 和调用元数据。

## 命名规范

- skill 文件夹名使用小写加连字符，例如 `zeng-guofan`
- `SKILL.md` frontmatter 中的 `name` 必须与文件夹名一致
- 名称应尽量简短、稳定、可预测

## 内容规范

### 1. 一手资料优先

优先使用：

- 著作
- 书信
- 日记
- 讲话
- 论文
- 访谈
- 原始公开材料

如果是一手资料不足的人物，可以使用高质量二手研究，但必须在 `source-map.md` 里说清楚。

### 2. 区分来源置信度

至少分成三层：

- 高置信来源
- 辅助解释来源
- 低置信或存疑来源

如果某个广为流传的说法其实来源不稳，请明确写出来，不要混进核心原则。

### 3. 不做“名言拼盘”

我们要的是：

- 可复用的判断框架
- 可执行的动作建议
- 明确的适用边界

而不是：

- 励志句子堆砌
- 伪古文口号
- 把人物神化成万能导师

### 4. 必须做现代适配

任何历史人物 skill 都不能直接照搬其时代环境。

必须转译成现代、合法、伦理上可接受的表达。例如：

- 不鼓励暴力
- 不鼓励操控和羞辱
- 不鼓励歧视或压迫
- 不鼓励把相术、出身、权谋当作核心方法

### 5. 给出明确输出结构

建议 skill 都提供默认输出结构，方便 AI 稳定使用。例如：

- 总判断
- 先做什么
- 不要做什么
- 短中期动作
- 沟通建议
- 反思问题

## 推荐编写流程

1. 先整理人物的真实来源
2. 在 `source-map.md` 里建立来源层级
3. 在 `principles.md` 里提炼核心方法
4. 在 `SKILL.md` 里写触发条件、使用方法、输出格式、边界
5. 本地运行校验脚本
6. 提交 PR

## 提交前自查

提交前至少确认：

- `python3 scripts/validate_skills.py` 可以通过
- `SKILL.md` frontmatter 完整
- 必需文件都在
- `references/source-map.md` 里写清来源层级
- `references/principles.md` 不是纯摘抄，而是做了方法抽象
- 没有明显的伪史料、伪名言、伪科学内容
- 没有鼓励非法、欺骗、操控、伤害性的建议

## PR 应该写什么

PR 描述请至少说明：

- 这个 skill 对应谁
- 主要参考了哪些来源
- 这个 skill 适合解决什么问题
- 你特别处理了哪些争议点或低置信内容

请直接使用仓库自带的 PR 模板。

## 维护者审查标准

维护者会按这几个维度审：

1. 来源质量
2. 结构完整度
3. 方法抽象质量
4. 现代适配与安全边界
5. 可读性与可调用性

更细的审查项见：

- [`docs/review-checklist.md`](./docs/review-checklist.md)

## 小建议

- 宁可少写，但要写准
- 宁可少引用金句，也要把方法讲清
- 宁可承认“这里不确定”，也不要装作确定
- 尽量让这个 skill 像一个可靠的“思考框架”，而不是一个花哨人格扮演器
