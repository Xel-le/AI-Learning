def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    since_last_char = 0
    if len(s) > 6 or len(s) < 2:
        return False
    for c in range(len(s)):
        if (c == 0 or c == 1) and not s[c].isalpha():
                return False
        else:
            if s[c].isalpha():
                if since_last_char > 0:
                    return False
            elif s[c].isdigit():
                if since_last_char == 0 and s[c] == "0":
                    return False
                since_last_char += 1
            else:
                return False
    return True

if __name__ == "__main__":
    main()