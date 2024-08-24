import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    name, extension = sys.argv[1].split(".")
    if extension != "py":
        sys.exit("Not a Python file")
    print(lines_of_code(sys.argv[1]))


def lines_of_code(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            res = 0
            for line in lines:
                if line.strip() == "" or line.strip().startswith("#"):
                    continue
                res += 1
            return res
    except FileNotFoundError:
        return "File does not exist"


if __name__ == "__main__":
    main()
