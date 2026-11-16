#!/usr/bin/env python3
"""用 DeepSeek API 回放 case，绕开 DSH 进程启动开销。

system 放 AGENTS.md 全文，user 放拼接后的 case prompt，与 DSH 回放的请求结构一致。
"""

import argparse
import hashlib
import json
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES = REPO / "data" / "case-prompts.jsonl"
OUT = REPO / "outputs" / "eval"
API = "https://api.deepseek.com/chat/completions"


def api_key() -> str:
    text = (Path.home() / ".dsh" / ".credentials.yaml").read_text(encoding="utf-8")
    match = re.search(r"DEEPSEEK_API_KEY:\s*(\S+)", text)
    if not match:
        raise SystemExit("缺少 DEEPSEEK_API_KEY")
    return match.group(1)


def call(key: str, model: str, rules: str, prompt: str) -> str:
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": rules},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "max_tokens": 4096,
    }
    request = urllib.request.Request(
        API,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        data = json.load(response)
    message = data["choices"][0]["message"]
    return {
        "content": message.get("content") or "",
        "reasoning": message.get("reasoning_content") or "",
        "usage": data.get("usage", {}),
        "raw": data,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", default=str(CASES))
    parser.add_argument("--rules", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--model", default="deepseek-flash")
    args = parser.parse_args()

    rules_text = Path(args.rules).read_text(encoding="utf-8")
    digest = hashlib.sha256(rules_text.encode("utf-8")).hexdigest()[:12]
    rows = [json.loads(line) for line in Path(args.cases).read_text(encoding="utf-8").splitlines() if line.strip()]
    if args.limit:
        rows = rows[: args.limit]

    key = api_key()
    started = time.time()

    def run(row: dict) -> dict:
        try:
            result = call(key, args.model, rules_text, row["prompt"])
        except Exception as error:  # 网络或限流错误原样记录
            result = {"content": f"[ERROR] {error}", "reasoning": "", "usage": {}, "raw": {"error": str(error)}}
        return {
            "label": args.label,
            "rules": args.rules,
            "sha256": digest,
            "id": row["id"],
            "prompt": row["prompt"],
            "answer": result["content"],
            "content": result["content"],
            "reasoning": result["reasoning"],
            "usage": result["usage"],
            "raw": result["raw"],
        }

    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        results = list(pool.map(run, rows))

    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{args.label}.jsonl"
    target.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in results) + "\n", encoding="utf-8")
    elapsed = time.time() - started
    print(f"written {target} ({len(results)} answers, {elapsed:.1f}s, rules sha256 {digest})")


if __name__ == "__main__":
    main()
