from keepary_core.money import format_inr


def test_zero_has_no_separator():
    assert format_inr(0) == "0"


def test_three_digit_amount_has_no_separator():
    assert format_inr(999) == "999"
