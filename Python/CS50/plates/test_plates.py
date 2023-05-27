from plates import is_valid



def main():
    print(test_one)
    print(test_two)
    print(test_three)
    print(test_four)
    print(test_five)
    
def test_one():
    assert is_valid("L") == False
    assert is_valid("LA") == True
    assert is_valid("LaNdRy") == True
    assert is_valid("LANDRYHOUSTON") == False


def test_two():
    assert is_valid("LL") == True
    assert is_valid("L3") == False
    assert is_valid("3L") == False
    assert is_valid("33") == False

def test_three():
    assert is_valid("LAN33H") == False
    assert is_valid("LAN333") == True

def test_four():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_five():
    assert is_valid("LA3.33") == False
    assert is_valid("LA3!33") == False
    assert is_valid("LA 33") == False

if __name__ == "__main__":
    main()