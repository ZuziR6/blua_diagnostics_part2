from src.graph.workflow import app

result = app.invoke({
    "input": "dor no peito",
    "patient": {"nome": "Maria", "idade": 34},
    "route": "",
    "retrieved_docs": [],
    "tools_used": [],
    "messages": [],
    "final_answer": "",
    "metadata": {}
})

print(result)
