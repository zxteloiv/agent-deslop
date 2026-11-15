#!/usr/bin/env python3
"""按 Grice 四准则检查回答样本。"""

import re
import sys
from pathlib import Path

QUANTITY = {
    "收尾总结": r"(综上所述|总的来说|总之|总而言之|一句话总结)",
    "重复句": None,
}
QUALITY = {
    "无来源归因": r"(专家认为|研究表明|数据显示|业内普遍认为)",
    "裸数字": r"\d+(\.\d+)?\s*(%|亿|万|倍|美元)",
}
RELATION = {
    "恭维开场": r"^(这是个好问题|好问题|问得好)",
    "复述问题": r"^(你问的|关于你提到的|就你提出的)",
}
MANNER = {
    "套路衔接": r"(首先|其次|再次|最后|值得注意的是|由此可见|不难看出)",
    "否定对偶": r"(不是[^，。]{1,12}，而是|不仅仅[^，。]{1,12}，更是)",
    "抽象大词": r"(底层逻辑|赋能|抓手|闭环|生态位|范式转移|时代脉搏|生活的肌理|丰富图景|关键支柱)",
    "排比破折": r"——[^—\n]{1,6}——",
}


def parse(text: str) -> dict[str, str]:
    parts: dict[str, str] = {}
    current = None
    buffer: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            continue
        match = re.match(r"^Q(\d+)\s*[:：]\s*(.*)$", line)
        if match:
            if current:
                parts[current] = "\n".join(buffer)
            current = f"Q{match.group(1)}"
            buffer = [match.group(2)] if match.group(2) else []
        elif re.match(r"^A\d*\s*[:：]", line):
            buffer.append(re.sub(r"^A\d*\s*[:：]\s*", "", line))
        elif current:
            buffer.append(line)
    if current:
        parts[current] = "\n".join(buffer)
    return parts


def sentence_duplicate(text: str) -> bool:
    sentences = [s.strip() for s in re.split(r"[。；\n]", text) if len(s.strip()) >= 10]
    return len(sentences) != len(set(sentences))


def run(text: str) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {"量": [], "质": [], "关系": [], "方式": []}
    if re.search(QUANTITY["收尾总结"], text):
        hits["量"].append("收尾总结")
    if sentence_duplicate(text):
        hits["量"].append("重复句")
    for name, pattern in QUALITY.items():
        for match in re.finditer(pattern, text):
            if name == "裸数字" and re.search(r"(来源|据|引自|参考)", text):
                continue
            hits["质"].append(name)
            break
    for name, pattern in RELATION.items():
        if re.search(pattern, text.strip()):
            hits["关系"].append(name)
    for name, pattern in MANNER.items():
        if re.search(pattern, text):
            hits["方式"].append(name)
    return hits


def main() -> None:
    for arg in sys.argv[1:] or ["outputs/samples/style-1.md"]:
        path = Path(arg)
        answers = parse(path.read_text(encoding="utf-8"))
        print(f"## {path.stem}")
        for question in sorted(answers, key=lambda k: int(k[1:])):
            hits = run(answers[question])
            status = "PASS" if not any(hits.values()) else "FAIL"
            detail = "; ".join(f"{k}:{','.join(v)}" for k, v in hits.items() if v)
            print(f"{question}\t{status}\t{detail or '无命中'}")


if __name__ == "__main__":
    main()
