#!/usr/bin/env python3
"""构建 220 条 AI 风格负例测试集，输出 JSONL。"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

EXAMPLES = {
    "Not X, but Y（否定对偶）": "It's not bold. It's backwards.",
    "Not just X, but Y": "Not just a tool, but a movement.",
    "Not X. Not Y. Just Z.": "Not ten. Not fifty. Five hundred.",
    "自问自答（The X? A Y.）": "The result? Devastating.",
    "Tricolon 三连排比": "更快、更稳、更智能。",
    "Em dash 插入语": "问题——没人提的那部分——是结构性的。",
    "短句堆叠（一句一段）": "他发表了。公开地。在书里。",
    "Gerund fragments": "修小 bug。写简单功能。处理明确的工单。",
    "Listicle in trench coat": "第一，……第二，……第三，……",
    "Here's the kicker": "Here's the kicker: nobody saw it coming.",
    "Think of it as": "Think of it as a highway system for data.",
    "Imagine a world": "Imagine a world where every tool has a quiet intelligence.",
    "False vulnerability": "说实话，我并不完美。",
    "The truth is simple": "真相很简单。",
    "意义膨胀": "这次会面意义深远。",
    "空洞升华": "让我们携手开启新篇章。",
    "绝对化断言": "这一方案必然成功。",
    "模糊归因": "专家认为这是最佳方案。",
    "无来源数字": "市场规模将达到 370 亿美元。",
    "防御式免责": "以上内容仅供参考。",
    "假谦虚": "个人浅见，说得不一定对。",
    "元评论": "本文将介绍三个要点。",
    "重复问题": "你问的是如何提高效率。",
    "恭维开场": "好问题！",
    "过度 hedging": "这可能会也可能不会有效。",
    "通用结论": "总而言之，前景广阔。",
    "每段小结": "本节小结：……",
    "三段式结构": "首先……其次……最后……",
    "模板段落": "首先……其次……最后……",
    "挑战转折公式": "尽管存在挑战，但前景依然乐观。",
    "Copula avoidance": "该建筑充当城市遗产的见证。",
    "Participle tail": "系统自动同步，从而提升效率。",
    "Vague connection": "该指标与增长密切相关。",
    "Elegant variation": "该工具……该系统……该平台……",
    "Bold-first bullets": "- **安全**：基于环境的配置。",
    "Emoji 装饰": "🚀 快速上手",
    "Unicode 箭头": "输入 → 处理 → 输出",
    "标题层级过深": "##### 小节标题",
    "标题紧接标题": "## 标题\n### 子标题",
    "表格代替叙述": "| 项目 | 值 |",
    "分隔线滥用": "---",
    "粗体滥用": "**重点**……**关键**……**核心**……",
    "代码块装饰": "```",
    "复选框列表": "- [ ] 待办",
    "嵌套列表过深": "      - 子项",
    "一句一段": "很快。",
    "段落等长": "（连续等长段落）",
    "结构预告": "本文分三个方面说明。",
    "结尾重申": "以上已经说明。",
    "通行话转场": "说到这里，",
    "套话问候": "希望这些对你有帮助。",
    "客户端口吻": "如需帮助，欢迎随时联系。",
    "过度承诺": "一定能解决。",
    "伪精确": "高达 99%。",
    "空泛结论": "总的来说，这很重要。",
    "正确的废话": "既要效率，又要质量。",
    "同义反复": "这个问题的问题在于。",
    "形容词堆砌": "高效、稳定、可靠、安全的方案。",
    "滥用类比": "就像高速公路一样。",
    "泛化概括": "大多数人都这样认为。",
    "道歉套话": "抱歉，上一轮拖太久了。",
    "免责声明": "以上内容仅供参考。",
}

EN_WORDS = [
    "delve", "tapestry", "landscape", "nuanced", "multifaceted", "pivotal",
    "crucial", "foster", "leverage", "streamline", "paradigm", "holistic",
    "robust", "comprehensive", "seamless", "revolutionize", "cutting-edge",
    "game-changer", "empower", "elevate", "resonate", "moreover", "furthermore",
    "nevertheless", "harnessing", "underscore", "realm", "myriad", "intricate",
    "captivating", "testament", "embark", "bespoke", "unwavering", "utilize",
    "showcase", "bolster", "cultivate", "enhance", "navigate", "interplay",
    "synergy", "meticulous", "vibrant", "valuable", "significant", "garner",
    "boast", "in order to", "the fact that",
]

EN_PHRASES = [
    "In today's fast-paced world", "In the ever-evolving landscape",
    "In today's digital age", "It's important to note that", "It's worth noting that",
    "Here's why", "Let's dive in", "Let's explore", "At its core", "In essence",
    "As we navigate the complexities", "A testament to", "The power of",
    "Stands as a beacon of", "In an era where", "Serves as a cornerstone",
    "Additionally, ", "Moreover, ", "Furthermore, ", "That being said",
    "In conclusion", "In summary", "Overall, ", "To sum up", "At the end of the day",
    "It could be argued that", "It seems that", "One could argue", "Some might say",
    "Generally speaking",
]

CN_WORDS = [
    "赋能", "抓手", "闭环", "底层逻辑", "生态位", "范式转移", "里程碑", "全方位",
    "多维度", "在当今", "随着时代的发展", "未来可期", "前途无量", "充满希望",
    "值得注意的是", "由此可见", "不难看出", "综上所述", "总而言之", "总之",
    "首先", "其次", "最后，", "与此同时", "于是乎", "从而", "因而", "诚然",
    "不仅要", "更是", "正确的废话", "既要", "有意义", "价值升华",
]

PATTERNS = [
    ("Not X, but Y（否定对偶）", r"不是[^，。]{1,15}，?而是|not [^.]{1,20}, but", "方式"),
    ("Not just X, but Y", r"不仅[^，。]{1,15}，?更是|not just [^.]{1,20}, but", "方式"),
    ("Not X. Not Y. Just Z.", r"不是[^。]{1,10}。不是[^。]{1,10}。", "方式"),
    ("自问自答（The X? A Y.）", r"[^。？\n]{2,12}？\s*(答案|它|这|真相)[^。]{0,15}。", "方式"),
    ("Anaphora 重复开头", r"(^|\n)([^。\n]{2,10})[^。\n]*。(?:\2)", "方式"),
    ("Tricolon 三连排比", r"([^，。、]{1,8})、([^，。、]{1,8})、([^，。、]{1,8})", "方式"),
    ("Em dash 插入语", r"——[^—]{2,30}——", "方式"),
    ("短句堆叠（一句一段）", r"^.{1,12}。\n.{1,12}。\n.{1,12}。$", "量"),
    ("Gerund fragments", r"(^|\n)([^。\n]{1,10}[。，]){3,}", "方式"),
    ("Listicle in trench coat", r"第一[，、].{0,40}第二[，、]", "方式"),
    ("Here's the kicker", r"Here's the (kicker|thing|deal)|精彩的是", "方式"),
    ("Think of it as", r"可以把它想象成|相当于一个|Think of it as", "方式"),
    ("Imagine a world", r"想象一下|Imagine a world", "方式"),
    ("False vulnerability", r"坦白说|说实话|说出来可能不信|And yes", "方式"),
    ("The truth is simple", r"真相是|事实很简单|答案很明显", "质"),
    ("意义膨胀", r"意义深远|前所未有|里程碑式|历史性", "方式"),
    ("空洞升华", r"让我们共同|携手|开启新篇章|迈向未来", "方式"),
    ("绝对化断言", r"必然|一定会|毫无疑问|显然|毋庸置疑", "质"),
    ("模糊归因", r"专家认为|研究表明|业内普遍认为|数据显示|据统计", "质"),
    ("无来源数字", r"(增长|下降|市场|规模|营收|利润|占比|渗透率)[^。]{0,12}\d+(\.\d+)?\s*(%|亿|万|倍|美元)", "质"),
    ("防御式免责", r"仅供参考|不构成建议|建议咨询专业人士|因人而异|具体情况具体分析", "关系"),
    ("假谦虚", r"不是专家|个人浅见|说得不一定对|能力有限", "方式"),
    ("元评论", r"本文将|下面介绍|接下来讨论|需要说明的是|值得一提的是", "关系"),
    ("重复问题", r"你问的是|关于你的问题|就你提到的", "关系"),
    ("恭维开场", r"好问题|问得好|这个想法很好|Great question", "关系"),
    ("过度 hedging", r"(可能|也许|或许|大概|似乎).{0,20}(可能|也许|或许|大概|似乎)", "方式"),
    ("通用结论", r"总而言之|总的来说|综上所述|未来可期|前途无量", "量"),
    ("每段小结", r"(综上|总之)[^\n]{0,20}\n", "量"),
    ("三段式结构", r"首先[^\n]{0,60}\n[^\n]{0,80}\n其次", "方式"),
    ("模板段落", r"首先[^\n]{0,40}。其次[^\n]{0,40}。最后", "方式"),
    ("挑战转折公式", r"尽管[^，。]{1,20}，但[^，。]{1,20}。|Despite its", "方式"),
    ("Copula avoidance", r"充当[^，。]{0,8}|serves as|stands as", "方式"),
    ("Participle tail", r"，(从而|进而|使得|确保了|体现了|彰显了)[^。]{0,20}。", "方式"),
    ("Vague connection", r"与[^，。]{1,10}相关联|与[^，。]{1,10}密切相关", "质"),
    ("Elegant variation", r"该(工具|系统|平台|方案).{0,20}该(工具|系统|平台|方案)", "方式"),
    ("Bold-first bullets", r"^\s*[-*]\s*\*\*[^*]+\*\*[：:]", "方式"),
    ("Emoji 装饰", r"[\U0001F300-\U0001FAFF✅🚀💡👉]", "方式"),
    ("Unicode 箭头", r"→|⇒", "方式"),
    ("标题层级过深", r"^#{5,6}\s", "方式"),
    ("标题紧接标题", r"^#{2,6}[^\n]*\n\s*#{2,6}", "方式"),
    ("表格代替叙述", r"^\|.*\|$", "量"),
    ("分隔线滥用", r"^---$", "方式"),
    ("粗体滥用", r"(\*\*[^*]+\*\*[^\n]{0,40}){4,}", "方式"),
    ("代码块装饰", r"```", "量"),
    ("复选框列表", r"^\s*[-*]\s*\[[ x]\]", "方式"),
    ("嵌套列表过深", r"^\s{6,}[-*]", "方式"),
    ("一句一段", r"^[^。\n]{1,20}。$", "方式"),
    ("段落等长", r"^[^\n]{40,80}$", "方式"),
    ("结构预告", r"(本文|下面|接下来)[^，。]{0,10}(分|从|为)[^，。]{0,10}(三|四|几)个", "关系"),
    ("结尾重申", r"(前面|以上)[^。]{0,20}(已经|都)[^。]{0,10}(说明|提到)", "量"),
    ("通行话转场", r"说到这里|话又说回来|不得不说", "方式"),
    ("套话问候", r"希望(这些|上述|以上)[^。]{0,10}(对|有)[^。]{0,10}(帮助|用)", "关系"),
    ("客户端口吻", r"如需|欢迎(随时)?(联系|告知)|我会(继续|随时)", "关系"),
    ("过度承诺", r"(?<!不)保证(能|会)|一定(能|会)|包(你|您)满意", "质"),
    ("伪精确", r"精确到|高达\s*\d+|超过\s*\d+%", "质"),
    ("空泛结论", r"总的来说[^。]{0,30}(重要|关键|必要)", "量"),
    ("正确的废话", r"既要[^。]{1,20}又要[^。]{1,20}", "量"),
    ("同义反复", r"([^，。]{2,6})[^。]{0,10}\1", "量"),
    ("形容词堆砌", r"([^，。]{1,6}的){4,}", "方式"),
    ("滥用类比", r"就像[^。]{1,20}一样|好比", "方式"),
    ("泛化概括", r"大多数|几乎所有|普遍认为", "质"),
]

STRUCTURE = [
    ("标题层级超过两级", r"^#{1,3}\s", "方式"),
    ("小节数量过多", r"(^#{4,5}\s.*\n){6,}", "量"),
    ("每节末尾小结", r"(本节|这一节)[^。]{0,10}(小结|总结)", "量"),
    ("全文结尾总结", r"^(综上|总之|总的来说)", "量"),
    ("列表条目凑数", r"^\s*\d+[.、]\s*.{1,10}$", "量"),
    ("表格列数过多", r"^\|.*\|.*\|.*\|.*\|.*\|.*\|", "量"),
    ("无引导表格", r"^Q\d+:\s*\n\s*\|", "方式"),
    ("嵌套三层以上", r"^\s{8,}[-*]", "方式"),
    ("粗体标签列表连续", r"(\*\*[^*]+\*\*[：:].*\n){4,}", "方式"),
    ("段落一句一换行", r"(^[^。\n]{1,25}。\n){5,}", "方式"),
    ("代码块代替说明", r"```[\s\S]{200,}```", "量"),
    ("引用块装饰", r"^>\s", "方式"),
    ("分割线分隔每节", r"^---\s*$[\s\S]{0,80}^---\s*$", "方式"),
    ("斜体强调滥用", r"((?<!\*)\*[^*\n]+\*(?!\*)[^\n]{0,30}){4,}", "方式"),
    ("链接堆砌", r"(\[[^\]]+\]\([^)]+\)\s*){4,}", "量"),
    ("emoji 标题装饰", r"^#{1,6}\s*[\U0001F300-\U0001FAFF]", "方式"),
    ("表格后无结论", r"\|[^\n]*\n\s*$", "方式"),
    ("列表后无收束", r"^[-*].*\n(?!\s*[-*\n])", "方式"),
    ("小节之间无过渡", r"^#{4,5}[^\n]*\n\n#{4,5}", "方式"),
    ("标题即段落", r"^#{4,5}[^\n]*\n\n[^\n]{0,10}$", "方式"),
]

TONE = [
    ("谄媚开场", r"^(好问题|问得好|很高兴|感谢提问)", "关系"),
    ("附和式应答", r"^(当然|确实|没错|Absolutely|Exactly)", "关系"),
    ("情绪安抚", r"理解你的|别担心|不用着急|放心", "关系"),
    ("自我贬低", r"我只是|我不太|能力有限|不太确定", "方式"),
    ("道歉套话", r"^(抱歉|对不起|很遗憾)", "关系"),
    ("求助式结尾", r"(还有|如果)(需要|想)[^。]{0,10}(告诉|说|问)", "关系"),
    ("询问式收尾", r"(要不要|需要我)[^。]{0,20}？$", "关系"),
    ("过度承诺服务", r"(随时|尽快|立刻)[^。]{0,10}(为|帮)", "质"),
    ("免责声明", r"仅供参考|风险自负|据此操作", "关系"),
    ("价值判断模糊", r"因人而异|看情况|视情况而定", "质"),
    ("回避正面", r"这个问题(很|比较)复杂|难以一概而论", "关系"),
    ("万能建议", r"建议(咨询|寻求)[^。]{0,10}(专业|医生|律师)", "关系"),
    ("情绪化强调", r"非常重要|极其重要|千万要", "方式"),
    ("命令式建议", r"必须(要)?[^。]{0,10}!|一定要", "方式"),
    ("过度共情", r"这种感觉|深有同感|换作是谁", "关系"),
]


def build():
    rows = []
    for index, word in enumerate(EN_WORDS, start=1):
        rows.append({
            "id": f"B{len(rows) + 1:03d}", "category": "英文高频词", "trigger": "用英文撰写一段产品说明",
            "bad": f"使用 {word} 一类 AI 高频词", "grice": "方式", "source": "slop-vocabulary / ai-writing-signs", "example": "",
            "detect": rf"\b{word}\b",
        })
    for phrase in EN_PHRASES:
        rows.append({
            "id": f"B{len(rows) + 1:03d}", "category": "英文套话", "trigger": "用英文介绍一个概念",
            "bad": f"使用 {phrase} 一类套话", "grice": "量" if "conclusion" in phrase or "summary" in phrase else "方式", "source": "text-patterns",
            "detect": rf"{phrase.strip()}",
        })
    for word in CN_WORDS:
        rows.append({
            "id": f"B{len(rows) + 1:03d}", "category": "中文套话", "trigger": "用中文介绍一个主题",
            "bad": f"使用「{word}」", "grice": "方式", "source": "humanizer-guide", "example": "",
            "detect": word,
        })
    for name, pattern, grice in PATTERNS + STRUCTURE + TONE:
        rows.append({
            "id": f"B{len(rows) + 1:03d}", "category": "句式与结构" if grice == "方式" else "语气与防御",
            "trigger": "回答一个通用问题", "bad": name, "grice": grice, "source": "tropes / text-patterns / platforms", "example": EXAMPLES.get(name, ""), "detect": pattern,
        })
    return rows


def main():
    rows = build()
    out = REPO / "data" / "badcases-v3.jsonl"
    out.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
    categories = {}
    for row in rows:
        categories[row["category"]] = categories.get(row["category"], 0) + 1
    print("total", len(rows))
    for name, count in sorted(categories.items(), key=lambda item: -item[1]):
        print(name, count)


if __name__ == "__main__":
    main()
