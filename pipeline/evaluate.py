#!/usr/bin/env python3
"""受控评测：隔离 DSH_HOME 与空工作区，唯一规则源为 home 下的 AGENTS.md。

用法：
  python3 pipeline/evaluate.py --rules rules/AGENTS-v0.md --label v0 --limit 3
  python3 pipeline/evaluate.py --rules rules/history/AGENTS-v2.md --label v2
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOME = Path(os.environ.get("EVAL_DSH_HOME", "/tmp/dsh-eval-home"))
WORKDIR = Path(os.environ.get("EVAL_WORKDIR", "/tmp/dsh-eval-run"))
QUESTIONS = REPO / "data" / "validate-questions.md"
OUT = REPO / "outputs" / "eval"


def api_key() -> str:
    if os.environ.get("DEEPSEEK_API_KEY"):
        return os.environ["DEEPSEEK_API_KEY"]
    text = (Path.home() / ".dsh" / ".credentials.yaml").read_text(encoding="utf-8")
    match = re.search(r"DEEPSEEK_API_KEY:\s*(\S+)", text)
    if not match:
        raise SystemExit("缺少 DEEPSEEK_API_KEY")
    return match.group(1)


def load_questions() -> list[str]:
    items = []
    for line in QUESTIONS.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s*\d+\.\s*(.+)$", line)
        if match:
            items.append(match.group(1).strip())
    return items


def run_one(question: str, env: dict[str, str]) -> str:
    node = os.environ["DSH_NODE_EXECUTABLE"]
    bin_js = str(Path(os.environ["DSH_INSTALL_DIR"]) / "lib" / "bin.js")
    command = [node, bin_js, "--profile", "headless", "--permission-mode", "read-only", question]
    result = subprocess.run(
        command, cwd=WORKDIR, env=env, capture_output=True, text=True, timeout=300,
    )
    if result.returncode != 0:
        return f"[ERROR] {result.stderr.strip()[-300:]}"
    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rules", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--questions", default=str(QUESTIONS))
    args = parser.parse_args()

    rules_path = Path(args.rules)
    rules_text = rules_path.read_text(encoding="utf-8")
    digest = hashlib.sha256(rules_text.encode("utf-8")).hexdigest()[:12]
    HOME.mkdir(parents=True, exist_ok=True)
    WORKDIR.mkdir(parents=True, exist_ok=True)
    (HOME / "AGENTS.md").write_text(rules_text, encoding="utf-8")

    env = dict(os.environ)
    env["DSH_HOME"] = str(HOME)
    env["DEEPSEEK_API_KEY"] = api_key()

    questions = load_questions()
    if args.limit:
        questions = questions[: args.limit]

    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{args.label}.jsonl"
    rows = []
    for index, question in enumerate(questions, start=1):
        answer = run_one(question, env)
        rows.append({
            "label": args.label,
            "rules": str(rules_path),
            "sha256": digest,
            "question": question,
            "answer": answer,
        })
        print(f"[{args.label}] {index}/{len(questions)} {answer[:60]}", file=sys.stderr)
    target.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
    print(f"written {target} ({len(rows)} answers, rules sha256 {digest})")


if __name__ == "__main__":
    main()
