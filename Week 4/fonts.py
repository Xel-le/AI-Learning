import sys
import pyfiglet

def main():
    print(sys.argv)
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Invalid usage")
    else:
        text = input("Input: ").strip()
        try:
            print(pyfiglet.figlet_format(text, font=sys.argv[2]))
        except Exception:
            sys.exit("Invalid usage")


main()
