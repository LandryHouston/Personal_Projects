from seasons import check_birthdate


def main():
    test_check_birthdat()


def test_check_birthday():
    assert check_birthdate("1999-05-24") == ("1999", "05", "24")
    assert check_birthdate("1999-5-24") == None
    assert check_birthdate("May 24, 1999") == None


if __name__ == "__main__":
    main()
