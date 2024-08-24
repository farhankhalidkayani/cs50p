from bank import value


def test_greeting():
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("Salam") == 100
