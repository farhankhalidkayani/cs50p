from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(11) == None
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    assert jar.withdraw(11) == None
    with pytest.raises(ValueError):
        jar.withdraw(2)
