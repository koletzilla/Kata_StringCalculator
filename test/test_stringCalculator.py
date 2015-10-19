from kata.calculator import stringCalculator


def test_shouldBeZeroIfInputIsEmpty():
    sc = stringCalculator()
    sum = sc.add("")
    assert sum == 0

