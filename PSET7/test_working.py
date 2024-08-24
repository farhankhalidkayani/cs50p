from working import convert
import pytest


def test_with_minutes():
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_exception():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
