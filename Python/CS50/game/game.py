import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

r_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < r_number:
                print("Too small!")
            elif guess > r_number:
                print("Too large!")
            else:
                print("Just right!")
                break

    except:
        pass