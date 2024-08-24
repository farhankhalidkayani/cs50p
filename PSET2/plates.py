def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    if 2 > len(str) or len(str) > 6:
        return False
    if not str[:2].isalpha():
        return False
    if not str.isalnum():
        return False
    for i in range(1, len(str)):
        if str[i] == '0' and str[i-1].isalpha():
            return False
        if str[i].isalpha() and str[i-1].isdigit():
            return False
    return True


main()
