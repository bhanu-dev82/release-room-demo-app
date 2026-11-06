"""Digit helpers for receipt text."""

_DEVANAGARI_TO_ASCII = str.maketrans("०१२३४५६७८९", "0123456789")


def normalise_digits(text: str) -> str:
    """Return text with Devanagari digits replaced by ASCII 0-9."""
    return text.translate(_DEVANAGARI_TO_ASCII)
