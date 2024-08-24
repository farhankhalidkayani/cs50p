import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    name, extension = sys.argv[1].split(".")
    if extension != "csv":
        sys.exit("Not a CSV file")
    print(formatter(sys.argv[1]))


def formatter(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            table = []
            for row in reader:
                table.append([i for i in row.values()])
            return tabulate(table, header, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
