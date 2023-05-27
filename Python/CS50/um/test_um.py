from um import count
import pytest

def main():
    test_one()


def test_one():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("...um...UM...Um...") == 3
    assert count("how are um you um doing") == 2
    assert count("hummer") == 0



if __name__ == "__main__":
    main()