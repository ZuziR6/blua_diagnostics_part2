from src.graph.workflow import app
import json

tests = [
    {"input": "dor no peito", "category": "red_flag"},
    {"input": "dor de cabeça", "category": "happy_path"}
]

results = []

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

    results.append({
        "input": t["input"],
        "category": t["category"],
        "route": out["route"],
        "answer": out["final_answer"],
        "tools": out["tools_used"]
    })

with open("evals/sprint2_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("OK")
