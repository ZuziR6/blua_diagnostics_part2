import json

def log_run(state):

    log = {
        "input": state["input"],
        "route": state["route"],
        "tools_used": state["tools_used"],
        "retrieved_docs": state["retrieved_docs"],
        "final_answer": state["final_answer"]
    }

    print(json.dumps(log, indent=2))

    return log
