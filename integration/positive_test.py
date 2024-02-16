import number


def test_positive():
    assert number.positive(5) == "positive"


def test_negative():
    assert number.negative(-5) == "positive"
