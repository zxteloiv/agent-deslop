#!/usr/bin/env python3
"""对仓库状态与规则文件执行静态回归检查。"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def check_source_field() -> bool:
    rows = [json.loads(line) for line in (REPO / "data" / "badcases-v3.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    return all(row.get("source") for row in rows)


def check_readme_purpose() -> bool:
    text = (REPO / "README.md").read_text(encoding="utf-8")
    return "目标" in text or "目的" in text


def check_judge_impl() -> bool:
    pipeline = REPO / "pipeline"
    return (pipeline / "judge-prompt.md").exists() and (pipeline / "judge.py").exists() and not (pipeline / "grice.py").exists()


def check_controlled_eval() -> bool:
    text = (REPO / "pipeline" / "evaluate.py").read_text(encoding="utf-8")
    return "DSH_HOME" in text and "/tmp/dsh-eval" in text


CASES = [
    ("sourced-test-data", "测试数据标注来源", check_source_field),
    ("readme-purpose", "README 给出目标", check_readme_purpose),
    ("model-judge", "语用判据由模型执行", check_judge_impl),
    ("isolated-eval", "评测隔离且单一规则源", check_controlled_eval),
]


def main() -> None:
    failed = 0
    for case_id, name, check in CASES:
        ok = check()
        failed += 0 if ok else 1
        print(f"{case_id}\t{name}\t{'PASS' if ok else 'FAIL'}")
    print(f"\n汇总: PASS={len(CASES) - failed} FAIL={failed}")


if __name__ == "__main__":
    main()
