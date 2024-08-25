from datetime import date
import inflect
import sys


def main():
    dob = input("DOB: ")
    try:
        year, month, day = dob.split("-")
    except:
        sys.exit(1)
    print(converter(year, month, day))


def converter(year, month, day):
    today = date.today()
    dob = date(int(year), int(month), int(day))
    difference = today - dob
    p = inflect.engine()
    return (
        p.number_to_words(difference.days * 24 * 60, andword="").capitalize()
        + " minutes"
    )


if __name__ == "__main__":
    main()
