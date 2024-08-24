from validator_collection import checkers


def main():
    email = input("What's your email address: ")
    print(valid(email))


def valid(email):
    if checkers.is_email(email):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
