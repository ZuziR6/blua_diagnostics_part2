import logging

logger = logging.getLogger(__name__)

logger.info("SupervisorAgent acionado")

from langgraph.graph import StateGraph, END

from src.graph.state import ClinicalState
from src.agents.supervisor import supervisor
from src.agents.triage_agent import triage_agent
from src.agents.prescription_agent import prescription_agent
from src.agents.escalation_agent import escalation_agent

def route(state):
    return state["route"]

graph = StateGraph(ClinicalState)

graph.add_node("supervisor", supervisor)
graph.add_node("triage", triage_agent)
graph.add_node("prescription", prescription_agent)
graph.add_node("escalation", escalation_agent)

graph.set_entry_point("supervisor")

graph.add_conditional_edges(
    "supervisor",
    route,
    {
        "triage": "triage",
        "prescription": "prescription",
        "escalation": "escalation",
        "out_of_scope": "escalation"
    }
)

graph.add_edge("triage", END)
graph.add_edge("prescription", END)
graph.add_edge("escalation", END)

app = graph.compile()

from src.utils.logger import log_run
