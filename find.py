import glob

def load_docs():
    docs = []
    for path in sorted(glob.glob("data/*.txt")):
        text = open(path, encoding="utf-8").read()
        docs.append({
            "source": path,
            "text": text
        })
    return docs

def find_answer(question):
    docs = load_docs()
    best = None
    best_score = 0

    for d in docs:
        score = 0
        for ch in set(question):
            if "\u4e00" <= ch <= "\u9fff":
                score += d["text"].count(ch)

        if score > best_score:
            best_score = score
            best = d

    if best is not None and best_score >= 3:
        return {
            "answer": best["text"],
            "source": best["source"],
            "score": best_score,
            "refused": False
        }

    return {
        "answer": "资料里没有，建议去教务处或一卡通中心确认。",
        "source": None,
        "score": best_score,
        "refused": True
    }