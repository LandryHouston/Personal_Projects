from numb3rs import validate

def main():
    test_one()
    test_two()

def test_one():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False

def test_two():
    assert validate(r'255.255.255.255') == True
    assert validate(r'500.1.1.1') == False
    assert validate(r'1.500.1.1') == False
    assert validate(r'1.1.500.1') == False
    assert validate(r'1.1.1.500') == False

if __name__ == "__main__":
    main()