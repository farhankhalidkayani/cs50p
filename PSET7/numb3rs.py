import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        a, b, c, d = ip.split(".")
        if (
            0 <= int(a) <= 255
            and 0 <= int(b) <= 255
            and 0 <= int(c) <= 255
            and 0 <= int(d) <= 255
        ):
            return True
        return False
    except:
        return False


if __name__ == "__main__":
    main()
