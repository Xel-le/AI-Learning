def main():
    while True:
            try:
                initial_fraction = input("Fraction: ").strip()
            except EOFError:
                break
            else:
                try:
                    print(gauge(convert(initial_fraction)))
                except ValueError, ZeroDivisionError:
                    pass
                else:
                    break


def convert(fraction):
    try:
        x, y = fraction.split("/")
    except AttributeError:
        raise ValueError
    else:
        if not x.isdigit() or not y.isdigit():
            raise ValueError
        elif int(x) < 0 or int(y) < 0:
            raise ValueError
        elif int(y) == 0:
            raise ZeroDivisionError
        elif int(x) > int(y):
            raise ValueError
        else:
            return round(int(x) / int(y) * int(100))


def gauge(percentage):
    try:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return f"{percentage}%"
    except TypeError:
        raise ValueError


if __name__ == "__main__":
    main()