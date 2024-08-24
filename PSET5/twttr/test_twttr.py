from twttr import shorten


def test_shortner_default():
    assert shorten("twitter") == "twttr"


def test_shortner_capital():
    assert shorten("TWITTER") == "TWTTR"


def test_shortner_number():
    assert shorten("tw1it3t4er") == "tw1t3t4r"


def test_shortner_punctuation():
    assert shorten("tw,it.t er") == "tw,t.t r"
