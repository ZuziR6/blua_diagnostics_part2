def check_medication_interaction(medication):
    interactions = {
        "ibuprofeno": "Pode elevar pressão arterial.",
        "dipirona": "Sem interação grave identificada."
    }

    return interactions.get(
        medication.lower(),
        "Nenhuma interação encontrada."
    )
