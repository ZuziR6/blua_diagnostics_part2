from langgraph.graph import StateGraph, END

from src.agents.supervisor import supervisor_route
from src.agents.triage_agent import triage_agent
from src.agents.prescription_agent import prescription_agent
from src.agents.escalation_agent import escalation_agent

workflow = StateGraph(dict)

def router(state):
    return supervisor_route(state["input"])

workflow.add_node("triage", triage_agent)
workflow.add_node("prescription", prescription_agent)
workflow.add_node("escalation", escalation_agent)

workflow.set_conditional_entry_point(
    router,
    {
        "triage": "triage",
        "prescription": "prescription",
        "escalation": "escalation"
    }
)

workflow.add_edge("triage", END)
workflow.add_edge("prescription", END)
workflow.add_edge("escalation", END)

graph = workflow.compile()
