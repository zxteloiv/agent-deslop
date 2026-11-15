#!/usr/bin/env python3
"""扫描输出样本命中的负例条目。"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES = [json.loads(line) for line in (REPO / "data" / "badcases-v3.jsonl").read_text(encoding="utf-8").splitlines()]
# 语义型条目无法用正则判定，交由人工复核
MANUAL = {"B120", "B172"}


def scan(text: str) -> list[dict]:
    body = "\n".join(line for line in text.splitlines() if not line.startswith("# "))
    hits = []
    for case in CASES:
        if case["id"] in MANUAL:
            continue
        try:
            if re.search(case["detect"], body):
                hits.append(case)
        except re.error:
            continue
    return hits


def main() -> None:
    for arg in sys.argv[1:]:
        path = Path(arg)
        hits = scan(path.read_text(encoding="utf-8"))
        print(f"## {path.stem}: {len(hits)} 命中")
        for case in hits[:30]:
            print(f"  {case['id']}\t{case['category']}\t{case['bad']}")
        print("  类别分布:", dict(Counter(case["category"] for case in hits)))


if __name__ == "__main__":
    main()
