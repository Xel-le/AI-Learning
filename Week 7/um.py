from re import findall
from re import IGNORECASE
from sys import exit

def main():
    try:
        print(count(input("Text: ")))
    except EOFError:
        exit()


def count(s):
    return len(findall(r"(?<!\w)(um)(?!\w)", s, IGNORECASE))

if __name__ == "__main__":
    main()