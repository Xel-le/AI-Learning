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
        result = float(eval("".join(temp_calc)))
        return result
    

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
                    priority_sequences[f"substitute{priority_counter}"] = temp_calc[priority_position-1:priority_position+(2*priority_length)]
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

    for i in range(len(priority_sequences)):
        priority_sequences[f"substitute{i}"] = float(eval("".join(priority_sequences[f"substitute{i}"])))

    for key in priority_sequences:
        if key in normal_sequences:
            normal_sequences[normal_sequences.index(key)] = str(priority_sequences[key])

    result = float(eval("".join(normal_sequences)))

    return result


if __name__ == "__main__":
    main()