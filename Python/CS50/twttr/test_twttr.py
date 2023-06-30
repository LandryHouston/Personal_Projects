from twttr import shorten

def main():
    print(test_default)
    print(test_numbers)
    print(test_pun)
    print(test_capital)


    
def test_default():
    assert shorten('twitter') == "twttr"

def test_capital():
    assert shorten('TWITTER') == "TWTTR"

def test_numbers():
    assert shorten('1234') == "1234"

def test_pun():
    assert shorten('?!.,') == "?!.,"



if __name__ == "__main__":
    main()