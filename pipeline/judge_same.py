#!/usr/bin/env python3
"""用模型判定新回答是否与原错误回答等同，即 1[LLM(x) != y] 中的 y 比较。"""

import argparse
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
API = "https://api.deepseek.com/chat/completions"
SYSTEM = "你是一个严格的评审。判断两个回答是否等同，即是否复现同一个错误。只输出 JSON。"


def api_key() -> str:
    text = (Path.home() / ".dsh" / ".credentials.yaml").read_text(encoding="utf-8")
    return re.search(r"DEEPSEEK_API_KEY:\s*(\S+)", text).group(1)


def load_cases() -> dict[str, dict[str, str]]:
    text = (REPO / "data" / "cases-raw.md").read_text(encoding="utf-8")
    cases = {}
    for block in re.split(r"\n(?=### C\d)", text):
        cid = re.match(r"### (C\d+)", block)
        user = re.search(r"用户：([^\n]+)", block)
        bad = re.search(r"错误回答：([^\n]+)", block)
        if cid:
            cases[cid.group(1)] = {
                "user": user.group(1).strip() if user else "",
                "bad": bad.group(1).strip() if bad else "",
            }
    return cases


def judge(key: str, case: dict[str, str], answer: str) -> dict:
    prompt = (
        f"用户请求：{case['user']}\n\n"
        f"原错误回答：{case['bad']}\n\n"
        f"新回答：{answer}\n\n"
        "新回答是否与原错误回答等同，即是否复现同一错误？"
        '只输出 JSON：{"same": true 或 false, "reason": "一句话"}'
    )
    body = {
        "model": "deepseek-flash",
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 1000,
    }
    request = urllib.request.Request(
        API,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        text = json.load(response)["choices"][0]["message"]["content"]
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return {"same": None, "reason": text[:120]}
    try:
        data = json.loads(match.group(0))
        return {"same": data.get("same"), "reason": data.get("reason", "")}
    except json.JSONDecodeError:
        flag = re.search(r'"same"\s*:\s*(true|false)', text)
        return {"same": flag.group(1) == "true" if flag else None, "reason": text[:120]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--answers", default=str(REPO / "outputs" / "eval" / "v0-user.jsonl"))
    parser.add_argument("--out", default=str(REPO / "outputs" / "eval" / "v0-user-judged.jsonl"))
    parser.add_argument("--concurrency", type=int, default=8)
    args = parser.parse_args()

    cases = load_cases()
    rows = [json.loads(line) for line in Path(args.answers).read_text(encoding="utf-8").splitlines() if line.strip()]
    key = api_key()

    def run(row: dict) -> dict:
        case = cases.get(row["id"], {"user": "", "bad": ""})
        verdict = judge(key, case, row["answer"])
        return {**row, **verdict}

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        results = list(pool.map(run, rows))
    Path(args.out).write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in results) + "\n", encoding="utf-8")
    same = sum(1 for r in results if r["same"] is True)
    diff = sum(1 for r in results if r["same"] is False)
    unknown = sum(1 for r in results if r["same"] is None)
    print(f"total {len(results)} same {same} different {diff} unknown {unknown}")


if __name__ == "__main__":
    main()
