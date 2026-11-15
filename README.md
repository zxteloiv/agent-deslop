# "Agent.md" 的除味剂

把 AGENTS.md 当作可优化的参数，用两套信号迭代输出质量：用户指出的问题转成回归用例；网上收集的 AI 风格负例按 Grice 合作原则筛选。不训练模型，改动都发生在文本层，可回滚、可对比、可分享。

目标函数：

```
R(agent.md) = Σ_{x, y ∈ B} 1[ LLM(x; agent.md) ≠ y ] · GriceanCriterion( LLM(x; agent.md) )
```

其中 B 是负面案例集，x 是触发问题，y 是令人厌恶的样例输出，GriceanCriterion 按量、质、关系、方式四准则判定。

## 快速开始

```sh
python3 pipeline/build_badcases.py                      # 重建 210 条负例测试集
python3 pipeline/scan_badcases.py outputs/samples/*.md  # 扫描样本命中
python3 pipeline/regression.py                          # 执行 21 条回归用例
python3 pipeline/grice.py outputs/samples/style-2.md    # 按四准则检查
```

## 目录

| 路径 | 内容 |
|---|---|
| `rules/` | 规则版本，`AGENTS-v0.md` 为迭代起点 θ0，`history/` 保存历史版本 |
| `data/` | 210 条网络负例、21 条回归用例、采样问题集 |
| `pipeline/` | 测试集生成、负例扫描、回归执行、Grice 检查四个脚本 |
| `outputs/` | 采样输出与回归报告 |
| `docs/` | 方法论与实验记录 |

## θ0

`rules/AGENTS-v0.md` 是迭代初始值，内容为当前全局 AGENTS.md（v3），84 行。历史版本在 `rules/history/`，记录从 v1 到 v3 的改动：格式条款、否定对偶、抽象大词、免责套话、结构上限。

迭代方法见 [docs/agents-md-optimization.md](docs/agents-md-optimization.md)。

## 数据

网络负例覆盖五类：句式与结构 53、英文高频词 50、语气与防御 43、中文套话 34、英文套话 30。来源包括 tropes 清单、AI 高频词表、Wikipedia AI 写作标志、文本 slop 模式、中文去 AI 味指南与 hedging 清单，详见 [data/network-badcases-notes.md](data/network-badcases-notes.md)。

回归用例来自真实会话中用户指出的问题，字段为编号、触发输入、期望、禁用、来源。

## 追加用例

用户指出风格问题时，按 [data/cases-regression.md](data/cases-regression.md) 的格式追加一条，编号顺延，并同步补充 `pipeline/` 中对应检查词表，随后对 `outputs/samples/` 执行一次检查。

## 迭代记录

v1 调整格式条款，允许表格与小节，限制标题层级；v2 增加否定对偶、抽象大词、时代开场、排比破折、恭维开场与列表数量限制；v3 增加 Copula 替代、句尾补意义、免责套话、结构上限与市场数字来源要求。

历次回放结果见 [outputs/regression-report.md](outputs/regression-report.md)，实验过程见 [docs/experiment-log.md](docs/experiment-log.md)。

## License

MIT，见 [LICENSE](LICENSE)。
