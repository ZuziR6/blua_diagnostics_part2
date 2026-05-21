def escalation_agent(state):

    state["final_answer"] = (
        "CASO GRAVE. Encaminhamento imediato para atendimento humano."
    )

    state["tools_used"].append("escalation")

    return state
