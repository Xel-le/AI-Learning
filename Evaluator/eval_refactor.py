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
    #calc = normalize(calc)
    apply(calc)
    return float(calc[0])

#def normalize(calc_list):
#    temp_calc = list(calc_list)
#   normalized_calc = []
#    for i in range(len(temp_calc)):
#        if temp_calc[i] in ["a", "b", "c", "d"]:
#            if temp_calc[i-1] == " ":
#
#        else:
#           normalized_calc.append(temp_calc[i])
#    print(normalized_calc)

def apply(calc_list):
    while "/" in calc_list or "*" in calc_list:
        for pos in range(len(calc_list)):
            if calc_list[pos] == "/":
                calc_list[pos-1]=f"{float(calc_list[pos-1])/float(calc_list[pos+1])}"
                del calc_list[pos:pos+2]
                break
            elif calc_list[pos] == "*":
                calc_list[pos-1]=f"{float(calc_list[pos-1])*float(calc_list[pos+1])}"
                del calc_list[pos:pos+2]
                break

    while "+" in calc_list or "-" in calc_list:
            for pos in range(len(calc_list)):
                if calc_list[pos] == "-":
                    calc_list[pos-1]=f"{float(calc_list[pos-1])-float(calc_list[pos+1])}"
                    del calc_list[pos:pos+2]
                    break
                elif calc_list[pos] == "+":
                    calc_list[pos-1]=f"{float(calc_list[pos-1])+float(calc_list[pos+1])}"
                    del calc_list[pos:pos+2]
                    break


if __name__ == "__main__":
    main()