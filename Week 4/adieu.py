import sys

def main():
    #Checking for errors
    if len(sys.argv) == 1:
        sys.exit("No names were provided")

    #Printing
    print(f"Adieu, adieu, to {sys.argv[1]}", sep="", end="")
    for arg in sys.argv[2:-1]:
        print(f", {arg}", sep="", end="")
    print(f", and {sys.argv[-1]}", sep="")

main()
