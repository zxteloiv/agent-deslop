#!/usr/bin/env python3
"""按固定字段检查实验样本，输出每个文件的命中计数。"""

import re
import sys
from pathlib import Path

CHECKS = {
    "代词": re.compile(r"你|我|您|咱们|大家|我们|\b(I|me|my|you|your|we|us|our)\b"),
    "拟人动词": re.compile(r"看到|听到|觉得|认为|明白|记住|忘记|理解|希望|担心|乐意|愿意|喜欢"),
    "确认应答": re.compile(r"已记下|记下了|收到|好的|明白|了解"),
    "自指状态": re.compile(r"已写入|已执行|已生效|已作为|已应用|规则已|已改|已在"),
    "口语化": re.compile(r"跑|搞|弄|整|搞定|齐了"),
    "黑话": re.compile(r"落盘"),
    "虚构沿革": re.compile(r"旧称|旧译"),
    "标题": re.compile(r"^#{1,3}\s", re.MULTILINE),
    "表格行": re.compile(r"^\s*\|", re.MULTILINE),
}


def scan(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    body = "\n".join(
        line for line in text.splitlines() if not line.startswith("# ")
    )
    row = {name: len(pattern.findall(body)) for name, pattern in CHECKS.items()}
    row["字符数"] = len(body)
    return row


def main() -> None:
    files = [Path(arg) for arg in sys.argv[1:]]
    if not files:
        files = sorted(Path("outputs/samples").glob("*.md"))
    columns = ["文件", *CHECKS.keys(), "字符数"]
    print("\t".join(columns))
    for path in files:
        row = scan(path)
        print("\t".join([path.stem, *(str(row[c]) for c in CHECKS), str(row["字符数"])]))


if __name__ == "__main__":
    main()
