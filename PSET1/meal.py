def main():
    time = input("Time: ")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    time = hour+minutes/60
    return time


if __name__ == "__main__":
    main()
