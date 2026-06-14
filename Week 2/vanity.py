def main():
    error_code = 0
    plate = input("Plate: ")
    error_code = is_valid(plate)
    if error_code == 0:
        print("Valid")
    else:
        print(error_code)
        print("Invalid")


def is_valid(s):
    since_last_char = 0
    if len(s) > 6 or len(s) < 2:
        return 1
    for c in range(len(s)):
        if (c == 0 or c == 1) and not s[c].isalpha():
                return 2
        else:
            if s[c].isalpha():
                if since_last_char > 0:
                    return 3
            elif s[c].isdigit():
                if since_last_char == 0 and s[c] == "0":
                    return 4
                since_last_char += 1
            else:
                return 5
    return 0

main()