"""Receipt parsing."""

import re
from dataclasses import dataclass

_TOTAL_RE = re.compile(
    r"(?:total|कुल)\s*:?\s*₹?\s*([0-9][0-9,]*(?:\.[0-9]{1,2})?)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Receipt:
    date: str
    total: float | None


def parse_receipt(text: str, date: str | None) -> Receipt:
    """Extract the date and grand total from receipt text."""
    cleaned_date = date.strip()
    match = _TOTAL_RE.search(text)
    total = float(match.group(1).replace(",", "")) if match else None
    return Receipt(date=cleaned_date, total=total)
