def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
        except EOFError:
            break
        else:
            try:
                x, y = fraction.split("/")
            except ValueError:
                pass
            else:
                if is_correct(x, y):
                    try:
                        result = round(int(x) / int(y) * int(100))
                    except ZeroDivisionError:
                        pass
                    else:
                        if result >= 99:
                            print("F")
                        elif result <= 1:
                            print("E")
                        else:
                            print(f"{result}%")
                        break
            


def is_correct(i, n):
    if not i.isdigit() or not n.isdigit():
        return False
    elif int(i) > int(n):
        return False
    else:
        return True


main()

        