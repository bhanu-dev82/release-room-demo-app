from keepary_core.parse import parse_receipt


def test_reads_ascii_total_and_strips_date():
    receipt = parse_receipt("Milk 40\nTotal: 120", "  2026-11-01 ")
    assert receipt.total == 120.0
    assert receipt.date == "2026-11-01"


def test_total_with_decimals_and_no_colon():
    receipt = parse_receipt("Total 45.50", "2026-11-01")
    assert receipt.total == 45.5


def test_missing_total_returns_none():
    assert parse_receipt("Thank you", "2026-11-01").total is None
