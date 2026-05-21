import logging

logger = logging.getLogger(__name__)

logger.info("SupervisorAgent acionado")

from typing import TypedDict, List, Dict, Any

class ClinicalState(TypedDict):
    input: str
    patient: Dict[str, Any]
    route: str
    retrieved_docs: List[str]
    tools_used: List[str]
    messages: List[Dict[str, str]]
    final_answer: str
    metadata: Dict[str, Any]
