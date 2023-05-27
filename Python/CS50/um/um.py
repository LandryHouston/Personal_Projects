import re


def main():
    print(count(input("Text: ")))


def count(s):
    find = re.findall(r"\b\W*um\W*\b", s, re.IGNORECASE)
    return len(find)


if __name__ == "__main__":
    main()