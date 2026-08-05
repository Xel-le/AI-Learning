def main():
    x = 0
    y = 0
    direction = 1
    dict_directions = {
        1: "North",
        2: "East",
        3: "South",
        4: "West"
    }

    while True:
        try:
            command = input("Command: ").lower()
        except EOFError:
            break
        else:
            command = command.replace(" ", "")
            x, y, direction = determine_coordinates(command, x, y, direction)
            #determine_coordinates(command, x, y, direction)
            print(f"Position: ({x}, {y}), facing {dict_directions[direction]}")


def determine_coordinates(commands_list, pos_x, pos_y, direct):
    valid_letters = {"f", "l", "r", "b"}
    x_temp = pos_x
    y_temp = pos_y
    direction_temp = direct
    for cmnd in commands_list:
        if cmnd not in valid_letters:
            print("Unknown command sequence. Only letters 'F', 'B', 'L', 'R' are permitted. Command ignored.")
            return(x_temp, y_temp, direction_temp)
    for cmnd in commands_list:
        if cmnd == "l":
            if direction_temp != 1:
                direction_temp = direction_temp-1
            else:
                direction_temp = 4
        elif cmnd == "r":
            if direction_temp != 4:
                direction_temp = direction_temp+1
            else:
                direction_temp = 1
        elif cmnd == "f":
            if direction_temp == 1 and y_temp < 10:
                y_temp = y_temp+1
            elif direction_temp == 2 and x_temp < 10:
                x_temp = x_temp+1
            elif direction_temp == 3 and -10 < y_temp:
                y_temp = y_temp-1
            elif direction_temp == 4 and -10 < x_temp:
                x_temp = x_temp-1
            else:
                print("Cannot go futher")
        elif cmnd == "b":
            if direction_temp == 1 and -10 < y_temp:
                y_temp = y_temp-1
            elif direction_temp == 2 and -10 < x_temp:
                x_temp = x_temp-1
            elif direction_temp == 3 and y_temp < 10:
                y_temp = y_temp+1
            elif direction_temp == 4 and x_temp < 10:
                x_temp = x_temp+1
            else:
                print("Cannot go futher")
    return(x_temp, y_temp, direction_temp)


main()