from langchain_openai import ChatOpenAI
from src.tools.tool_schema import get_patient_record, check_medication

llm = ChatOpenAI(model="gpt-4o-mini")

tools = [get_patient_record, check_medication]
llm_tools = llm.bind_tools(tools)

def triage_agent(state):

    response = llm_tools.invoke([
        {"role": "user", "content": state["input"]}
    ])

    state["final_answer"] = response.content
    state["tools_used"].append("tool_calling")

    return state
