from bank import value

def main():
    print(test_one)
    print(test_two)
    print(test_three)

def test_one():
    assert value('hello landry') == 0
    assert value('Hello') == 0
    assert value('HeLlO lAnDrY') == 0

def test_two():
    assert value('hey') == 20
    assert value('Hi') == 20

def test_three():
    assert value('good morning') == 100
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()