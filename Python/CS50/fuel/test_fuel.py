from fuel import convert, gauge
import pytest

def main():
    test_one()
    test_two()
    test_three()

def test_one():
    assert convert('1/4') == 25 and gauge(25) == "25%"
    assert convert('1/100') == 1 and gauge(1) == "E"
    assert convert('99/100') == 99 and gauge(99) == "F"


def test_two():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_three():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

if __name__ == "__main__":
    main()