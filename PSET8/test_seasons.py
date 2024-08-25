from seasons import converter


def test_converter():
    assert (
        converter("2004", "08", "30")
        == "Ten million, five hundred twelve thousand minutes"
    )
