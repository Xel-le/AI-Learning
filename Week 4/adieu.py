import sys

def main():
    #Checking for errors
    if len(sys.argv) == 1:
        sys.exit("No names were provided")
    elif len(sys.argv) == 2:
        print(f"Adieu, adieu, to {sys.argv[1]}")
        sys.exit()
    elif len(sys.argv) == 3:
        print(f"Adieu, adieu, to {sys.argv[1]} and {sys.argv[2]}")
        sys.exit()
    else:
        print(f"Adieu, adieu, to {sys.argv[1]}", sep="", end="")
        for name in sys.argv[2:-1]:
            print(f", {name}", sep="", end="")
        print(f", and {sys.argv[-1]}", sep="")
        sys.exit()


main()
