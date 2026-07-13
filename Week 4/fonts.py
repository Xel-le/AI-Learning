import sys
import pyfiglet
import random

def main():
    if len(sys.argv) == 1:
        font=random.choice(pyfiglet.FigletFont.getFonts())
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid usage")
    else:
        font=sys.argv[2]
    text = input("Input: ").strip()
    try:
        if sys.argv[2] in pyfiglet.FigletFont.getFonts():
            print(pyfiglet.figlet_format(text, font))
        else:
            sys.exit("Invalid font")
    except IndexError:
        print(pyfiglet.figlet_format(text, font))


main()
