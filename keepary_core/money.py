"""Money formatting."""


def format_inr(amount: int) -> str:
    """Format a whole-rupee amount with thousands separators."""
    return f"{amount:,}"
