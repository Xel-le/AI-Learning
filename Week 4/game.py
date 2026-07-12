import random
import sys

def main():
    while True:
        try:
            top_number = int(input("Level: "))
        except EOFError:
            sys.exit()
        except ValueError:
            print("That is not a number")
        else:
            if top_number <= 0:
               print("The provided number is negative or equal to zero")
               continue
            else:
                rnd_number = random.randrange(1, top_number+1)
                while True:
                    try:
                        user_number = int(input("Guess: "))
                    except ValueError:
                        print("That is not a number")
                        continue
                    except EOFError:
                        sys.exit()
                    else:
                        if user_number < rnd_number:
                            print("Too small!")
                        elif user_number > rnd_number:
                            print("Too large!")
                        else:
                            sys.exit("Just right")


main()