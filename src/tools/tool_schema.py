from langchain_core.tools import tool

@tool
def get_patient_record():
    """Retorna histórico do paciente"""
    return {
        "nome": "Maria",
        "idade": 34,
        "condicao": "hipertensão",
        "medicacao": "Losartana 50mg"
    }

@tool
def check_medication(med: str):
    """Checa interação de medicamento"""
    if med.lower() == "ibuprofeno":
        return "Pode aumentar pressão arterial"
    return "Sem interação relevante"
