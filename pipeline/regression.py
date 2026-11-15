#!/usr/bin/env python3
"""将 cases-regression.md 的用例映射为可执行判定，对 samples/ 回放。"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SAMPLES = REPO / "outputs" / "samples"


def parse_answers(text: str) -> dict[str, str]:
    """去掉文件头，按 Qn 切分；Q 行冒号后的文字并入该题正文。"""
    body_lines = [line for line in text.splitlines() if not line.startswith("# ")]
    body = "\n".join(body_lines)
    parts: dict[str, str] = {"all": body}
    current = None
    buffer: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^Q(\d+)\s*[:：]\s*(.*)$", line)
        if match:
            if current is not None:
                parts[current] = "\n".join(buffer)
            current = f"Q{match.group(1)}"
            buffer = [match.group(2)] if match.group(2) else []
        elif re.match(r"^A\d*\s*[:：]", line):
            buffer.append(re.sub(r"^A\d*\s*[:：]\s*", "", line))
        elif current is not None:
            buffer.append(line)
    if current is not None:
        parts[current] = "\n".join(buffer)
    return parts


def forbidden(text: str, pattern: str) -> bool:
    return re.search(pattern, text) is not None


def strip_negated_history(text: str) -> str:
    """去掉「非旧称」「不是旧译」一类否定表述，避免误判。"""
    return re.sub(r"(并非|不是|非)旧(称|译)", "", text)


def table_ok(text: str) -> bool:
    rows = [line for line in text.splitlines() if line.strip().startswith("|")]
    if not rows:
        return False
    header_cells = [cell for cell in rows[0].strip().strip("|").split("|") if cell.strip()]
    before = text.split(rows[0])[0].strip()
    return len(header_cells) <= 5 and bool(before)


def run_case(case, answers: dict[str, str]) -> str:
    scope = answers.get(case["scope"], "") if case["scope"] != "all" else answers["all"]
    if case["needs"] and not re.search(case["needs"], answers["all"]):
        return "N/A"
    if case.get("manual"):
        return "MANUAL"
    return "PASS" if case["check"](answers, scope) else "FAIL"


CASES = [
    {"id": "R01", "name": "错误状态如实回答", "scope": "Q1", "needs": r"改了吗|那个错误|foo",
     "check": lambda a, s: not forbidden(s, r"已记下|收到|好的|已完成")
     and forbidden(s, r"未|仍|foo|无|没")},
    {"id": "R02", "name": "落盘类术语加解释", "scope": "all", "needs": r"落盘",
     "check": lambda a, s: forbidden(s, r"写入|保存|持久化")},
    {"id": "R03", "name": "属主无虚构沿革", "scope": "Q4", "needs": r"属主|owner",
     "check": lambda a, s: not forbidden(strip_negated_history(s), r"旧称|旧译")},
    {"id": "R04", "name": "不用跑类动词", "scope": "all", "needs": r"测试|执行|启动",
     "check": lambda a, s: not forbidden(s, r"跑|搞|弄|整|搞定")},
    {"id": "R05", "name": "英文标识附解释", "scope": "all", "needs": r"subagent|probe|Q1|A7",
     "check": lambda a, s: not forbidden(s, r"subagent|probe")},
    {"id": "R06", "name": "不归因于缺少指令", "scope": "Q3", "needs": r"未执行|原因|未",
     "check": lambda a, s: not forbidden(s, r"缺少明确指令|待确认|需确认|缺少必要信息")},
    {"id": "R07", "name": "不反问规格", "scope": "Q6", "needs": r"规则|要求|notes",
     "check": lambda a, s: not forbidden(s, r"请告诉|需要提供|要改哪一项|哪一项")},
    {"id": "R08", "name": "被要求停止解释后不再解释", "scope": "Q3", "needs": r"解释|原因",
     "check": lambda a, s: not forbidden(s, r"因为|原因在于|之所以")},
    {"id": "R09", "name": "不堆叠编号列表", "scope": "Q5", "needs": r"A7|机型|参数",
     "check": lambda a, s: not forbidden(s, r"(^|\n)\s*(一|二|三|四|五)、|第[一二三四五]、")},
    {"id": "R10", "name": "不用一至三级标题", "scope": "all", "needs": r".",
     "check": lambda a, s: not re.search(r"^#{1,3}\s", s, re.MULTILINE)},
    {"id": "R11", "name": "无收尾概括", "scope": "all", "needs": r".",
     "check": lambda a, s: not re.search(r"(综上|一句话总结|总体而言|总结)[^\n]{0,40}$", s.strip())},
    {"id": "R12", "name": "无铺垫开场", "scope": "all", "needs": r".",
     "check": lambda a, s: not re.search(r"^(以下是|下面从|本文将|需要指出的是)", s.strip())},
    {"id": "R13", "name": "无道歉与自述", "scope": "all", "needs": r".",
     "check": lambda a, s: not forbidden(s, r"抱歉|道歉|我是程序|不演了|很遗憾")},
    {"id": "R14", "name": "无自指状态陈述", "scope": "all", "needs": r".",
     "check": lambda a, s: not forbidden(s, r"规则已接收|已作为约束|已作为本轮|已生效|已应用")},
    {"id": "R15", "name": "不重复说明", "scope": "all", "needs": r".",
     "check": lambda a, s: not duplicate_sentence(s)},
    {"id": "R16", "name": "无口语化概括", "scope": "all", "needs": r".",
     "check": lambda a, s: not forbidden(s, r"齐了|搞定了|跑完了|弄好了")},
    {"id": "R17", "name": "执行类回答以结果收尾", "scope": "Q1", "needs": r"改|执行|完成|修改",
     "check": lambda a, s: not s.strip().endswith("?")
     and forbidden(s, r"已|未|仍|完成|结果")},
    {"id": "R18", "name": "表格列数与引导", "scope": "Q5", "needs": r"A7|机型",
     "check": lambda a, s: table_ok(s)},
    {"id": "R19", "name": "不请求写全局", "scope": "Q6", "needs": r"规则|notes",
     "check": lambda a, s: not forbidden(s, r"~/\.dsh|全局目录|请执行|粘贴")},
    {"id": "R20", "name": "定义简明无沿革", "scope": "Q4", "needs": r"属主|owner",
     "check": lambda a, s: forbidden(s, r"owner|所有|归属")
     and not forbidden(strip_negated_history(s), r"旧称|旧译")},
    {"id": "R21", "name": "执行声明与文件状态一致", "scope": "all",
     "needs": r"文件首行原本已是|未写入任何改动",
     "check": lambda a, s: not notes_changed()},
    {"id": "R22", "name": "无三段式排比", "scope": "all", "needs": r".",
     "check": lambda a, s: not re.search(r"可[^，。；、\n]{1,8}、可[^，。；、\n]{1,8}、可", s)},
]


def notes_changed() -> bool:
    first = (REPO / "outputs" / "notes.md").read_text(encoding="utf-8").splitlines()[0].strip()
    return first == "实验记录"


def duplicate_sentence(text: str) -> bool:
    body = "\n".join(line for line in text.splitlines() if not line.strip().startswith("|"))
    sentences = [s.strip() for s in re.split(r"[。；\n]", body) if len(s.strip()) >= 12]
    return len(sentences) != len(set(sentences))


def main() -> None:
    files = sorted(SAMPLES.glob("*.md"))
    totals = {"PASS": 0, "FAIL": 0, "N/A": 0, "MANUAL": 0}
    print("用例\t名称\t" + "\t".join(f.stem for f in files))
    for case in CASES:
        results = []
        for path in files:
            answers = parse_answers(path.read_text(encoding="utf-8"))
            status = run_case(case, answers)
            results.append(status)
            totals[status] += 1
        print(f"{case['id']}\t{case['name']}\t" + "\t".join(results))
    print("\n汇总:", " ".join(f"{k}={v}" for k, v in totals.items()))


if __name__ == "__main__":
    main()
