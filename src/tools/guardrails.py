RED_FLAGS = [
    "dor no peito",
    "falta de ar",
    "desmaio",
    "convulsão",
    "paralisia"
]

OUT_OF_SCOPE = [
    "bitcoin",
    "hackear",
    "programação"
]

def detect_red_flags(text):
    for flag in RED_FLAGS:
        if flag in text.lower():
            return True
    return False

def out_of_scope(text):
    for term in OUT_OF_SCOPE:
        if term in text.lower():
            return True
    return False
