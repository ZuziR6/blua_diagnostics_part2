from evals.judge import evaluate
from src.graph.workflow import app
import json

results = []

tests = [
    {"input": "dor no peito", "category": "red_flag"},
    {"input": "dor de cabeça", "category": "normal"}
]

for t in tests:

    out = app.invoke({
        "input": t["input"],
        "patient": {"nome": "Maria"},
        "route": "",
        "retrieved_docs": [],
        "tools_used": [],
        "messages": [],
        "final_answer": "",
        "metadata": {}
    })

    score = evaluate(t["input"], out["final_answer"])

    results.append({
        "input": t["input"],
        "answer": out["final_answer"],
        "score": score,
        "route": out["route"]
    })

with open("evals/sprint2_results.json", "w") as f:
    json.dump(results, f, indent=4)
