#!/usr/bin/env python3
"""对受控评测产物执行全文类回归用例。

题号相关的用例（R01 至 R03、R05 至 R09、R17 至 R21）需要专用样本，
不在本脚本执行，定义见 data/cases-regression.md。
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVAL = REPO / "outputs" / "eval"

CASES = [
    {"id": "R04", "name": "不用跑类动词", "check": lambda s: not re.search(r"跑|搞|弄|整|搞定", s)},
    {"id": "R10", "name": "不用一至三级标题", "check": lambda s: not re.search(r"^#{1,3}\s", s, re.MULTILINE)},
    {"id": "R11", "name": "无收尾概括", "check": lambda s: not re.search(r"(综上|一句话总结|总体而言)[^\n]{0,40}$", s.strip())},
    {"id": "R12", "name": "无铺垫开场", "check": lambda s: not re.search(r"^(以下是|下面从|本文将|需要指出的是)", s.strip())},
    {"id": "R13", "name": "无道歉与自述", "check": lambda s: not re.search(r"抱歉|道歉|我是程序|不演了|很遗憾", s)},
    {"id": "R14", "name": "无自指状态陈述", "check": lambda s: not re.search(r"规则已接收|已作为约束|已作为本轮|已生效|已应用", s)},
    {"id": "R15", "name": "不重复说明", "check": lambda s: not duplicate(s)},
    {"id": "R16", "name": "无口语化概括", "check": lambda s: not re.search(r"齐了|搞定了|跑完了|弄好了", s)},
    {"id": "R22", "name": "无三段式排比", "check": lambda s: not re.search(r"可[^，。；、\n]{1,8}、可[^，。；、\n]{1,8}、可", s)},
]


def duplicate(text: str) -> bool:
    body = "\n".join(line for line in text.splitlines() if not line.strip().startswith("|"))
    sentences = [s.strip() for s in re.split(r"[。；\n]", body) if len(s.strip()) >= 12]
    return len(sentences) != len(set(sentences))


def main() -> None:
    files = [Path(arg) for arg in sys.argv[1:]] or sorted(EVAL.glob("*.jsonl"))
    if not files:
        print("no eval files")
        return
    totals = {"PASS": 0, "FAIL": 0}
    for path in files:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        print(f"## {path.stem} ({len(rows)} answers)")
        for case in CASES:
            results = []
            for row in rows:
                ok = case["check"](row.get("answer", ""))
                results.append("PASS" if ok else "FAIL")
            passed = results.count("PASS")
            totals["PASS"] += passed
            totals["FAIL"] += results.count("FAIL")
            print(f"{case['id']}\t{case['name']}\t{passed}/{len(results)}")
    print("\n汇总:", " ".join(f"{k}={v}" for k, v in totals.items()))


if __name__ == "__main__":
    main()
