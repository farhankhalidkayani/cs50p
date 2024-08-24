from um import count


def test_um():
    assert count("um") == 1


def test_um1():
    assert count("UM") == 1


def test_um2():
    assert count("album") == 0
