from src.tools.guardrails import (
    detect_red_flags,
    out_of_scope
)

def supervisor_route(user_input):

    if out_of_scope(user_input):
        return "out_of_scope"

    if detect_red_flags(user_input):
        return "escalation"

    if "remédio" in user_input.lower():
        return "prescription"

    return "triage"
