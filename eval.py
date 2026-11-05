from find import find_answer

cases = [
    ("转专业绩点要求", False),
    ("转专业申请时间", False),
    ("校园卡挂失补办", False),
    ("校园卡工本费多少", False),
    ("奖学金什么时候评", False),
    ("校长办公室电话", True),
    ("帮我写入党申请书", True),
    ("附近好吃的火锅", True),
    ("今天天气怎么样", True),
    ("如何追喜欢的人", True),
]

right = 0
lines = []
for i, (q, want) in enumerate(cases, 1):
    r = find_answer(q)
    ok = (r["refused"] == want)
    right += ok
    lines.append(f"{i}. {q} | 期望拒答={want} | 实际拒答={r['refused']} | {'对' if ok else '错'}")

open("eval_log.md", "w", encoding="utf-8").write(
    "# eval_log\n\n" + "\n".join(lines) + f"\n\nscore: {right}/{len(cases)}\n"
)
print("written eval_log.md", right, "/", len(cases))