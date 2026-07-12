import sys
import pyfiglet
import random

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid usage")
    else:
        text = input("Input: ").strip()
        try:
            if sys.argv[2] in pyfiglet.FigletFont.getFonts():
                print(pyfiglet.figlet_format(text, font=sys.argv[2]))
            else:
                sys.exit("Invalid usage")
        except IndexError:
            print(pyfiglet.figlet_format(text, font=random.choice(pyfiglet.FigletFont.getFonts())))


main()
