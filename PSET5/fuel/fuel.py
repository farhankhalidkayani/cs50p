
def gauge(res):
    if res >= 99:
        return "F"
    elif res <= 1:
        return "E"
    else:
        return f"{round(res)}%"


def convert(fuel):
    num, den = fuel.split("/")
    num = int(num)
    den = int(den)
    if den == 0:
        raise ZeroDivisionError
    res = (num/den)*100
    if res > 100:
        raise ValueError
    return res


def main():
    while True:
        try:
            fuel = input("Fraction: ")
            res = convert(fuel)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(gauge(res))
            break


if __name__ == "__main__":
    main()
