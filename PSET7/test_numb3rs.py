from numb3rs import validate


def test_validate_correct():
    assert validate("1.1.1.1") == True


def test_validate_wrong():
    assert validate("256.3.4.5") == False
    assert validate("2.4.5.267") == False
