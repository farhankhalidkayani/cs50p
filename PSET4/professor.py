import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        res = num1+num2
        tries = 3
        while tries > 0:
            try:
                choice = int(input(f"{num1} + {num2} ="))
                if choice == res:
                    score += 1
                    break
                else:
                    tries -= 1
                    print("EEE")
            except ValueError:
                print("EEE")
        if tries == 0:
            print(f"{num1} + {num2} = {res}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input())
            if level not in (1, 2, 3):
                raise ValueError
            break
        except ValueError:
            pass
    return level


def generate_integer(level):
    start = "100"
    start = 0 if level == 1 else int(start[:level])
    level = int("9"*level)
    return random.randint(start, level)


if __name__ == "__main__":
    main()
