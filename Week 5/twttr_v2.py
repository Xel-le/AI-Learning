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
        if not isVowel(c.lower()):
            result += c
    if len(result) == 0:
        sys.exit("All characters were filtered out")
    else:
        return result

def isVowel(c):
    if c in "aeiouy":
        return True
    else:
        return False

if __name__ == "__main__":
    main()