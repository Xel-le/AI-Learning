def main():
    text = input("Input: ")
    output = ""
    characters = list(text)
    for c in range(len(characters)):
        if not is_vowel(characters[c]):
            output += characters[c]
    print(f"Output: {output}")

def is_vowel(letter):
    if letter.lower() in "aeiou":
        return True
    else:
        return False


main()