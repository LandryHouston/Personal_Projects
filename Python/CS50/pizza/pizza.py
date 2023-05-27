import sys
import csv
from tabulate import tabulate


def main():
    check_arg()
    menu = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))


def check_arg():

    if len(sys.argv) < 2:
        sys.exit("Too few command_line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command_line arguments")
    if "csv" not in sys.argv[1]:
        sys.exit("Not a csv file")


if __name__ == "__main__":
    main()
