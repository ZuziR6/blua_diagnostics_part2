def test_red_flag_detection():
    symptoms = "dor no peito e falta de ar"

    red_flags = [
        "dor no peito",
        "falta de ar"
    ]

    assert any(flag in symptoms for flag in red_flags)


def test_out_of_scope():
    question = "como hackear um banco"

    forbidden = [
        "hackear",
        "fraude"
    ]

    assert any(word in question for word in forbidden)
