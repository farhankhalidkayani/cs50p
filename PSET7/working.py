import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if " to " not in s:
        raise ValueError
    match = re.search(
        r"(?P<start_hr>(0)?[0-9]{1}|1[0-2]{1})(:(?P<start_min>[0-5]{1}[0-9]{1}))? (?P<start>AM|PM) to (?P<end_hr>(0)?[0-9]{1}|1[0-2]{1})(:(?P<end_min>[0-5]{1}[0-9]{1}))? (?P<end>AM|PM)",
        s,
    )
    try:
        start_hr = int(match.group("start_hr"))
        start_min = int(match.group("start_min")) if match.group("start_min") else 0
        start = match.group("start")
        end_hr = int(match.group("end_hr"))
        end_min = int(match.group("end_min")) if match.group("end_min") else 0
        end = match.group("end")
    except AttributeError:
        raise ValueError
    if start == "PM" and start_hr != 12:
        start_hr += 12
    if end == "PM" and end_hr != 12:
        end_hr += 12
    if start == "AM" and start_hr == 12:
        start_hr = 0
    if end == "AM" and end_hr == 12:
        end_hr = 0
    return f"{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}"


if __name__ == "__main__":
    main()
