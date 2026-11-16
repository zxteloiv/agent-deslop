# "Agent.md" 的除味剂

AI怪味的成因可能当前还不清楚，另外对常用的模型普通人也难以后训练或PEFT。故暂时用修改agent.md的方案来注入一些需求，不见得有效，但希望泛用性好一些。

具体地，把 AGENTS.md 当作可优化的参数，用两套信号迭代输出质量：用户指出的问题转成回归用例；网上收集的 AI 风格负例按 Grice 合作原则筛选。改动只发生在 AGENTS.md，模型参数不变；每版规则保存在 rules/，差异由 git 记录。

目标函数：

```
R(agent.md) = Σ_{x, y ∈ B} 1[ LLM(x; agent.md) ≠ y ] · GriceanCriterion( LLM(x; agent.md) )
```

其中 B 是负面案例集，x 是触发问题，y 是令人厌恶的样例输出，GriceanCriterion 按量、质、关系、方式四准则判定。

## 快速开始

```sh
python3 pipeline/build_badcases.py
python3 pipeline/evaluate.py --rules rules/AGENTS-v0.md --label v0
python3 pipeline/scan_badcases.py outputs/eval/v0.jsonl   # 正则预筛
python3 pipeline/regression.py outputs/eval/v0.jsonl      # 全文类回归用例
python3 pipeline/judge.py outputs/eval/v0.jsonl           # 生成 Grice 评审任务
```

Grice 四准则由语言模型按 `pipeline/judge-prompt.md` 的协议逐条评审，正则检测器只做预筛。

## 目录

| 路径 | 内容 |
|---|---|
| `rules/` | 规则版本，`AGENTS-v0.md` 为迭代起点 θ0 |
| `data/` | 210 条网络负例、22 条回归用例、采样问题集 |
| `pipeline/` | 测试集生成、受控评测、正则预筛、回归执行、评审任务生成 |
| `outputs/eval/` | 受控评测产物与评审输入 |
| `docs/` | 方法论 |

## θ0

`rules/AGENTS-v0.md` 是迭代初始值，内容为当前全局 AGENTS.md，84 行。后续版本在 `rules/` 下按 `AGENTS-v1.md`、`AGENTS-v2.md` 递增，差异由 git 记录。

迭代方法见 [docs/agents-md-optimization.md](docs/agents-md-optimization.md)。

## 数据

网络负例覆盖五类：句式与结构 53、英文高频词 50、语气与防御 43、中文套话 34、英文套话 30。来源包括 tropes 清单、AI 高频词表、Wikipedia AI 写作标志、文本 slop 模式、中文去 AI 味指南与 hedging 清单，详见 [data/network-badcases-notes.md](data/network-badcases-notes.md)。

回归用例来自真实会话中用户指出的问题，字段为编号、触发输入、期望、禁用、来源。

## 追加用例

用户指出风格问题时，按 [data/cases-regression.md](data/cases-regression.md) 的格式追加一条，编号顺延，并同步补充 `pipeline/` 中对应检测项，随后对 `outputs/eval/` 执行一次检查。

## 评测记录

受控评测使用独立 `DSH_HOME`、空工作区与 headless profile，规则唯一来源是 home 下的 AGENTS.md。每次评测记录规则 sha256、问题与答案，写入 `outputs/eval/<label>.jsonl`。判定由正则预筛、全文回归用例与 Grice 模型评审三层组成。

## License

MIT，见 [LICENSE](LICENSE)。
