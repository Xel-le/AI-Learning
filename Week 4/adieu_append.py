import sys

def main():
    #Checking for errors
    names=[]
    while True: 
        try:
            input_value = input("Input: ")
            names.append(input_value)
        except EOFError:
            if len(names) == 0:
                sys.exit("No names were provided")
            elif len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")
                sys.exit()
            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
                sys.exit()
            else:
                print(f"Adieu, adieu, to {names[0]}", sep="", end="")
                for name in names[1:-1]:
                    print(f", {name}", sep="", end="")
                print(f", and {names[-1]}", sep="")
                sys.exit()


main()