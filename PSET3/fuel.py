import math

while True:
    try:
        fuel = input("Fraction: ")
        num, den = fuel.split("/")
        num = int(num)
        den = int(den)
        res = (num/den)*100
        if res > 100:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if res >= 99:
            print("F")
        elif res <= 1:
            print("E")
        else:
            print(f"{round(res)}%")
        break
