from keepary_core.digits import normalise_digits


def test_ascii_text_is_unchanged():
    assert normalise_digits("Total 120") == "Total 120"


def test_devanagari_digits_become_ascii():
    assert normalise_digits("१२०") == "120"
