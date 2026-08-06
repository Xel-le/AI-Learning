from sys import exit

def main():
    try:
        calculation = input("Your calculation: ").strip()
    except EOFError:
        exit()
    else:
        print(calculate(calculation))
    

#10 + 12 - -2 * 5 + 15 / 5 * 7 / 3 + 19

def calculate(calc):
    calc = calc.split()
    apply(calc)
    return float(calc[0])

def apply(calc_list):
    while "/" in calc_list or "*" in calc_list:
        for pos in range(len(calc_list)):
            if calc_list[pos] == "/" or calc_list[pos] == "*":
                calc_list[pos-1]=f"{do_calc(float(calc_list[pos-1]), calc_list[pos], float(calc_list[pos+1]))}"
                del calc_list[pos:pos+2]
                break

    while "+" in calc_list or "-" in calc_list:
            for pos in range(len(calc_list)):
                if calc_list[pos] == "-" or calc_list[pos] == "+":
                    calc_list[pos-1]=f"{do_calc(float(calc_list[pos-1]), calc_list[pos], float(calc_list[pos+1]))}"
                    del calc_list[pos:pos+2]
                    break

def do_calc(a, op, b):
    if op == "+":
        return a+b
    if op == "-":
        return a-b
    if op == "/":
        return a/b
    if op == "*":
        return a*b
    

if __name__ == "__main__":
    main()