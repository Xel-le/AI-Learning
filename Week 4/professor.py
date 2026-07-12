import random
import sys


def main():
    errors = 0
    score = 0
    selected_level = get_level()
    x, y = generate_integer(selected_level)
    for i in range(10):
        while True:
            try:
                answer = int(input(f"{x[i]} + {y[i]} = "))
            except EOFError:
                sys.exit()
            else:
                if answer != (x[i] + y[i]) and errors < 2:
                    errors += 1
                    print("EEE")
                elif answer != (x[i] + y[i]) and errors == 2:
                    errors = 0
                    print("EEE")
                    print(f"{x[i]} + {y[i]} = {x[i] + y[i]}")
                    break
                else:
                    score += 1
                    break
    print(f"Score: {score}")
            




def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except EOFError:
            sys.exit()
        except ValueError:
            continue
        else:
            if level <= 0:
                continue
            else:
                return level


def generate_integer(l):
    x_func = []
    y_func = []
    for _ in range(10):
        x_func.append(random.randrange((10**(l-1)),(10**l)))
        y_func.append(random.randrange((10**(l-1)),(10**l)))
    return x_func, y_func


main()