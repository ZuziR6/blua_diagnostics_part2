CARDIOLOGY_KEYWORDS = [
    "dor no peito",
    "pressão alta",
    "hipertensão",
    "taquicardia"
]


def cardiology_router(state):

    question = state["question"].lower()

    for keyword in CARDIOLOGY_KEYWORDS:
        if keyword in question:
            return "cardiology"

    return "prescription"
