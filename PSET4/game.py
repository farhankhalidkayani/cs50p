import random


while True:
    try:
        number = int(input("Level: "))
        if number < 1:
            continue
        break
    except ValueError:
        pass
comp = random.randint(1, number)
while True:
    try:
        choice = int(input("Guess: "))
        if choice < 1:
            continue
        elif choice < comp:
            print("Too small!")
        elif choice > comp:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
