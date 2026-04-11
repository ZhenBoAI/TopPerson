[English](./person-catalog.md) | [简体中文](./person-catalog.zh-CN.md)

# TopPerson 人物 Catalog

这是一份用于后续人物 skill 蒸馏的 100+ 结构化人物数据。

它和 backlog 的区别是：

- `docs/person-backlog.*` 是当前较小的人物规划清单
- `data/person-catalog.json` 是更大的结构化人物数据池

## 数据文件

- JSON 数据：[`data/person-catalog.json`](../data/person-catalog.json)

## 当前数量

- 总人物数：`110`
- 成熟参考 skill：`1`
- 已创建初版 skill：`44`
- 还没建 skill 目录的新候选人：`65`

## 主要字段

- `slug`
  仓库里稳定使用的人物 id
- `name_zh` / `name_en`
  中英文人物名
- `fit_buckets`
  主要适用场景：`life`、`study`、`work`、`life-guidance`
- `status`
  当前状态：`reference_skill`、`draft_skill`、`candidate`
- `distillation_priority`
  当前打磨或蒸馏优先级
- `primary_use_case`
  这个人物最适合解决什么现实问题
- `ordinary_people_value`
  为什么普通人也能用这个人的方法
- `source_readiness`
  来源准备度，当前用 `strong` / `medium`
- `risk_note`
  做 skill 时最需要注意的风险点
- `recommended_skill_angle`
  最适合切入的第一个 skill 角度
- `source_hints`
  后续补资料时可以优先看的来源方向

## 推荐的下一批蒸馏人物

如果你想在现有 33 个 skill 之外继续扩充，下面这批比较适合优先做：

- 孔子
- 胡适
- 陶行知
- 钱学森
- 袁隆平
- 屠呦呦
- 马化腾
- 张瑞敏
- 维克多·弗兰克尔
- 大野耐一
- 本田宗一郎
- 萨提亚·纳德拉
- 约翰·伍登
- 丹尼尔·卡尼曼

## 怎么用这份数据

常见用法：

- 按 `fit_buckets` 过滤生活 / 学习 / 工作 / 人生指导人物
- 按 `status` 区分已建 skill 和待蒸馏候选人
- 按 `source_readiness` 先挑资料更扎实的人物
- 按 `distillation_priority` 选下一批要做的 skill

## 说明

这份 catalog 是蒸馏规划数据，不是最终史料定稿。
每个人物在真正做成成熟 skill 前，仍然要继续做来源审查和边界处理。
