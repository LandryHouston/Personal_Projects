import re


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first = ""
    second = ""
    lines = ""
    x = ""
    output = ""
    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if len(first_number) >= 5 or len(second_number) >= 5:
            return "Error: Numbers cannot be more than four digits."
        sum = ""
        if operator == "+":
            sum = str(int(first_number) + int(second_number))
        elif operator == "-":
            sum = str(int(first_number) - int(second_number))
        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        y = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            x += y + "    "
        else:
            first += top
            second += bottom
            lines += line
            x += y

    if solve:
        output = first + "\n" + second + "\n" + lines + "\n" + x
    else:
        output = first + "\n" + second + "\n" + lines
    return output
