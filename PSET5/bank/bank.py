def main():
    greeting = input("Greeting: ").lower().strip()
    print(greeting(greeting))


def value(greeting):
    if greeting[:5].lower().strip() == "hello":
        return 0
    elif greeting[0].lower().strip() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
