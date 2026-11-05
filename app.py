from find import find_answer
from fastapi import FastAPI
app=FastAPI()
@app.get("/ask")
def ask(q: str):
    r = find_answer(q)
    return {"question": q, "answer": r.get("answer", ""),
        "refused": r.get("refused", False),
        "source": r.get("source", []) 
          # 假设 source 是列表结构，按实际类型调整
          }