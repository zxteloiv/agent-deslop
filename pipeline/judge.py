#!/usr/bin/env python3
"""生成 Grice 评审任务清单，供语言模型逐条评审。"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SAMPLES = REPO / "outputs" / "samples"
OUT = REPO / "outputs" / "judge-tasks.md"


def parse(text: str) -> list[tuple[str, str, str]]:
    items = []
    current = None
    buffer: list[str] = []
    question = ""
    for line in text.splitlines():
        if line.startswith("# "):
            continue
        match = re.match(r"^Q(\d+)\s*[:：]\s*(.*)$", line)
        if match:
            if current is not None:
                items.append((current, question, "\n".join(buffer).strip()))
            current = f"Q{match.group(1)}"
            question = match.group(2)
            buffer = []
        elif re.match(r"^A(?:\d+)?n?\s*[:：]", line):
            buffer.append(re.sub(r"^A(?:\d+)?n?\s*[:：]\s*", "", line))
        elif current is not None:
            buffer.append(line)
    if current is not None:
        items.append((current, question, "\n".join(buffer).strip()))
    return items


def load_items(path: Path) -> list[tuple[str, str, str]]:
    if path.suffix == ".jsonl":
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        return [(f"Q{index}", row.get("question", ""), row.get("answer", "")) for index, row in enumerate(rows, start=1)]
    return parse(path.read_text(encoding="utf-8"))


def main() -> None:
    files = [Path(arg) for arg in sys.argv[1:]] or sorted(SAMPLES.glob("*.md"))
    lines = ["# Grice 评审任务", "", "按 pipeline/judge-prompt.md 的协议逐条评审，结果写入 outputs/judge-report.md。", ""]
    for path in files:
        lines.append(f"## {path.stem}")
        lines.append("")
        for index, question, answer in load_items(path):
            lines.append(f"### {path.stem}/{index}: {question}")
            lines.append("")
            lines.append(answer if answer else "（空）")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("written", OUT, len(lines), "lines")


if __name__ == "__main__":
    main()
