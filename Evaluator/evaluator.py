import sys

def main():
    try:
        calculation = input("Your calculation: ").strip()
    except EOFError:
        sys.exit()
    else:
        print(calculate(calculation))
    

#10 + 12 - 2 * 5 + 15 / 5 * 7 / 3 + 19

def calculate(calc):
    priority_total = 0
    priority_counter = -1
    priority_length = 0
    priority_sequences = dict()
    temp_calc = calc.split()

    #Getting the number of priority ops to know the longest sequence
    for c in range(len(temp_calc)):
        if temp_calc[c] == "*" or temp_calc[c] == "/":
            priority_total += 1

    #Edge-case handling where all ops are priority
    if priority_total*2+1 == len(temp_calc):
        while "/" in temp_calc or "*" in temp_calc:
            for pos in range(len(temp_calc)):
                if temp_calc[pos] == "/":
                    temp_calc[pos-1]=f"{float(temp_calc[pos-1])/float(temp_calc[pos+1])}"
                    del temp_calc[pos:pos+2]
                    break
                elif temp_calc[pos] == "*":
                    temp_calc[pos-1]=f"{float(temp_calc[pos-1])*float(temp_calc[pos+1])}"
                    del temp_calc[pos:pos+2]
                    break

        return float(temp_calc[0])
    

    #Derermining priority sequences
    for c in range(len(temp_calc)):
        if temp_calc[c] == "*" or temp_calc[c] == "/":
            priority_position = c
            priority_length += 1
            n = 2
            while n % 2 == 0:
                if c+n < len(temp_calc) and (temp_calc[c+n] == "*" or temp_calc[c+n] == "/"):
                    priority_length += 1
                    n += 2
                    if priority_length >= priority_total:
                        n = 1
                else:
                    priority_counter += 1
                    priority_sequences[f"{priority_counter}"] = temp_calc[priority_position-1:priority_position+(2*priority_length)]
                    if priority_total*2+1 != len(temp_calc):
                        for index in range(priority_position-1, priority_position+(2*priority_length)):
                            temp_calc[index] = f"substitute{priority_counter}"
                    else:
                        for index in range(len(temp_calc)):
                            temp_calc[index] = f"substitute{priority_counter}"
                    priority_length = 0
                    n = 1

    normal_sequences = []
    for index in range(len(temp_calc)):
        if "substitute" not in temp_calc[index]:
            normal_sequences.append(temp_calc[index])
        elif "substitute" in temp_calc[index]:
            if temp_calc[index] not in normal_sequences:
                normal_sequences.append(temp_calc[index])

    for k in range(len(priority_sequences)):
        while "/" in priority_sequences[f"{k}"] or "*" in priority_sequences[f"{k}"]:
            for pos in range(len(priority_sequences[f"{k}"])):
                if priority_sequences[f"{k}"][pos] == "/":
                    priority_sequences[f"{k}"][pos-1]=f"{float(priority_sequences[f"{k}"][pos-1])/float(priority_sequences[f"{k}"][pos+1])}"
                    del priority_sequences[f"{k}"][pos:pos+2]
                    break
                elif priority_sequences[f"{k}"][pos] == "*":
                    priority_sequences[f"{k}"][pos-1]=f"{float(priority_sequences[f"{k}"][pos-1])*float(priority_sequences[f"{k}"][pos+1])}"
                    del priority_sequences[f"{k}"][pos:pos+2]
                    break

        #priority_sequences[f"substitute{i}"] = float(eval("".join(priority_sequences[f"substitute{i}"])))

    for key in priority_sequences:
        if f"substitute{key}" in normal_sequences:
            normal_sequences[normal_sequences.index(f"substitute{key}")] = "".join(priority_sequences[key])

    while "+" in normal_sequences or "-" in normal_sequences:
                for pos in range(len(normal_sequences)):
                    if normal_sequences[pos] == "-":
                        normal_sequences[pos-1]=f"{float(normal_sequences[pos-1])-float(normal_sequences[pos+1])}"
                        del normal_sequences[pos:pos+2]
                        break
                    elif normal_sequences[pos] == "+":
                        normal_sequences[pos-1]=f"{float(normal_sequences[pos-1])+float(normal_sequences[pos+1])}"
                        del normal_sequences[pos:pos+2]
                        break

    return float(normal_sequences[0])

if __name__ == "__main__":
    main()