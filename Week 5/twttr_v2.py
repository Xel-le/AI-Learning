import sys

def main():
    try:
        text = input("Input: ").strip()
    except EOFError:
        sys.exit("Input cancelled")
    print(shorten(text))

def shorten(t):
    result = ""
    for c in t:
        if not c.lower() in "aeiou":
            result += c
    return result

if __name__ == "__main__":
    main()