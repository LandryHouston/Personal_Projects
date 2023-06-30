import sys

def main():
    command_line_arguments()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count_lines = 0
    for line in lines:
        if check_line(line) == False:
            count_lines += 1
    print(count_lines)

def command_line_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

def check_line(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith('#'):
        return True
    else:
        return False


if __name__ == "__main__":
    main()