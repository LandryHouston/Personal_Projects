from project import (
    check_birth_date,
    check_state_name,
    check_zip_code,
)
import pytest


def main():
    print(test_check_birth_date)
    print(test_check_state_name)
    print(test_check_zip_code)


def test_check_birth_date():
    assert check_birth_date("05/24/1999") == "05/24/1999"

    with pytest.raises(ValueError):
        check_birth_date("5/24/1999")
        check_birth_date("05-24-1999")
        check_birth_date("cat")


def test_check_state_name():
    assert check_state_name("Nevada") == "Nevada"

    with pytest.raises(ValueError):
        check_state_name("nevada") == "Nevada"
        check_state_name("NEVADA") == "Nevada"
        check_state_name("  Nevada   ") == "Nevada"


def test_check_zip_code():
    assert check_zip_code("89012") == "89012"
    assert check_zip_code("12345-6789") == "12345-6789"

    with pytest.raises(ValueError):
        check_zip_code("1234")
        check_zip_code("cat")
        check_zip_code("123456")
        check_zip_code("   89012   ")


if __name__ == "__main__":
    main()
