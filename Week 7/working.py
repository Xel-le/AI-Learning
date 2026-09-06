from re import search
from sys import exit

def main():
    try:
        time = input("Time: ").strip()
    except EOFError:
        exit()
    else:
        try:
            print(convert(time))
        except ValueError:
            exit("Unknown format")

def convert(s):
    if matches := search(r"^([0-9]+):?([0-9]*)[ ]*(AM|PM) ?t?o? ?([0-9]+):?([0-9]*)[ ]*(AM|PM)$", s):
        time1 = to_24_h(matches.group(1), matches.group(2), matches.group(3))
        time2 = to_24_h(matches.group(4), matches.group(5), matches.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError

def to_24_h(t1, t2, meridiem):
    if 1 <= int(t1) <= 12 and t2 == "":
        if meridiem == "AM":
            if int(t1) == 12:
                time = "00:00"
            elif 1 <= int(t1) <= 9:
                time = f"0{int(t1)}:00"
            else:
                time = f"{t1}:00"
        else:
            if int(t1) == 12:
                time = f"{int(t1)}:00"
            else:
                time = f"{int(t1)+12}:00"
    elif 1 <= int(t1) <= 12 and 0 <= int(t2) <= 59:
        if meridiem == "AM":
            if int(t1) == 12:
                time = f"00:{t2}"
            elif 1 <= int(t1) <= 9:
                time = f"0{int(t1)}:{t2}"
            else:
                time = f"{t1}:{t2}"
        else:
            if int(t1) == 12:
                time = f"{int(t1)}:{t2}"
            else:
                time = f"{int(t1)+12}:{t2}"
    else:
        raise ValueError
    return time

if __name__ == "__main__":
    main()