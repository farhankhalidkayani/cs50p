import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    _, extension1 = sys.argv[1].split(".")
    _, extension2 = sys.argv[2].split(".")
    if extension1 != "csv":
        sys.exit("Not a CSV file")
    if extension2 != "csv":
        sys.exit("Not a CSV file")
    changer(sys.argv[1], sys.argv[2])


def changer(input, output):
    with open(input, "r") as file_input, open(output, "w") as file_output:
        reader = csv.DictReader(file_input)
        writer = csv.DictWriter(file_output, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].strip().split(",")
            house = row["house"]
            writer.writerow({"first": first.strip(), "last": last.strip(), "house": house})


if __name__ == "__main__":
    main()
