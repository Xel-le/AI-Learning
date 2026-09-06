from re import search
from re import IGNORECASE
from sys import exit


def main():
    try:
        print(parse(input("HTML: ")))
    except EOFError:
        exit()

def parse(s):
    if matches := search(r"https?://www\.youtube\.com/embed/([\w-]+)\"", s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()