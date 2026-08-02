def main():
    while True:
            try:
                initial_fraction = input("Fraction: ").strip()
            except EOFError:
                break
            else:
                try:
                    print(gauge(convert(initial_fraction)))
                except ValueError:
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
        elif int(x) > int(y):
            raise ValueError
        else:
            try:
                result = round(int(x) / int(y) * int(100))
            except ZeroDivisionError:
                raise ValueError
            else:
                return result


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