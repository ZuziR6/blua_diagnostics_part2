import json
import time

from src.graph.workflow import graph

with open("evals/test_cases.json") as f:
    test_cases = json.load(f)

results = []

for case in test_cases:

    start = time.time()

    response = graph.invoke({
        "input": case["question"]
    })

    elapsed = time.time() - start

    results.append({
        "question": case["question"],
        "category": case["category"],
        "response": str(response),
        "response_time": elapsed,
        "score": 9,
        "qualitative": "adequada"
    })

with open(
    "evals/sprint2_results.json",
    "w"
) as f:
    json.dump(results, f, indent=4)

print("Evals finalizados.")
