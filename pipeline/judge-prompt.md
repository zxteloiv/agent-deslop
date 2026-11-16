# Grice 评审协议

正则只能拦截词面特征，不能判定语用质量。切题、信息量、真实性、清晰度四项需要语言模型逐条评审。本协议规定评审输入、判定标准与输出格式。

## 输入

每组输入包含用户问题 x 与模型回答 z。评审只依据 x 与 z，不参考规则文本。

## 判定标准

按 Paul Grice 合作原则四准则与四项附加判据逐项判定，每项给出通过或失败，并引用回答中的原句作为证据。

| 准则 | 通过条件 | 失败条件 |
|---|---|---|
| 量 | 信息量满足问题所需，无冗余 | 复述问题、堆砌背景、收尾总结、重复同一结论、只答一半 |
| 质 | 陈述有依据，不确定处有标注 | 编造数据或来源、把推测写成事实、无来源的绝对断言 |
| 关系 | 直接回应问题，不跑题 | 答非所问、先寒暄再回答、追加未问内容、反问规格 |
| 方式 | 表达清楚、简短、有序 | 术语未解释、句子歧义、结构堆叠、抽象大词、套话 |
| 附加·代词 | 无「你、我、您、我们、咱们」 | 出现任一代词 |
| 附加·口语 | 无「齐了」「重来」「走一遍」一类说法 | 出现口语说法 |
| 附加·单字 | 无跑、搞、弄、整、混、爽、牛、坑、怼的口语用法 | 出现任一类 |
| 附加·拟人 | 无「已记下」「抱歉」「我是程序」一类表述 | 出现任一类 |

## 输出格式

每个问题输出一行 JSON，字段为 id、quantity、quality、relation、manner、pronoun、colloquial、single_char、anthropomorphic、evidence、verdict。verdict 为四准则与四项附加判据全部通过时的 pass，否则 fail。

```json
{"id": "v0/Q1", "quantity": "pass", "quality": "pass", "relation": "pass", "manner": "pass", "pronoun": "pass", "colloquial": "pass", "single_char": "pass", "anthropomorphic": "pass", "evidence": "回答直接给出产品功能，无总结段", "verdict": "pass"}
```

## 执行方式

评审由语言模型执行，不使用正则。正则检测器仅作为高召回预筛，命中项进入人工或模型复核，未命中项不能自动判为通过。

评审任务由 `pipeline/judge.py` 生成，写入 `outputs/judge-tasks.md`；评审结果写入 `outputs/judge-report.md`。
