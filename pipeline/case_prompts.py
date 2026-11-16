#!/usr/bin/env python3
"""从 cases-raw.md 生成回放提示，输出 JSONL。"""

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "data" / "cases-raw.md"
OUT = REPO / "data" / "case-prompts.jsonl"


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    premise_match = re.search(r"## 大前提\n\n([\s\S]*?)\n\n## ", text)
    premise = premise_match.group(1).strip().split("\n\n")[0] if premise_match else ""

    rows = []
    for block in re.split(r"\n(?=## 场景)", text):
        header = re.search(r"## (场景[^\n]+)", block)
        summary = re.search(r"### 摘要\n\n([^\n]+)", block)
        if not header or not summary:
            continue
        for case in re.split(r"\n(?=### C\d)", block):
            cid = re.search(r"### (C\d+)", case)
            user = re.search(r"用户：([^\n]+)", case)
            if not cid or not user:
                continue
            prompt = (
                f"背景：{premise}\n\n"
                f"场景：{summary.group(1).strip()}\n\n"
                f"用户：{user.group(1).strip()}\n\n"
                "请直接回答用户。"
            )
            rows.append({"id": cid.group(1), "prompt": prompt})

    OUT.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
    print("written", OUT, len(rows))


if __name__ == "__main__":
    main()
