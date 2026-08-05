def main():
    direction = 0
    position = [0, 0]
    dict_directions = {
            0: "North",
            1: "East",
            2: "South",
            3: "West"
        }
    while True:
        try:
            command = input("Command: ").lower()
        except EOFError:
            break
        else:
            command = command.replace(" ", "")
            position, direction = directions(command, position, direction)
            print(f"{position}, facing {dict_directions[direction]}")

def directions(commands_list, coordinates, direct):
    movement_vectors = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0]
    }
    valid_letters = {"f", "l", "r", "b"}
    coordinates_temp = list(coordinates)
    direction_temp = direct
    for cmnd in commands_list:
        if cmnd not in valid_letters:
            print("Unknown command sequence. Only letters 'F', 'B', 'L', 'R' are permitted. Command ignored.")
            return(coordinates_temp, direction_temp)

    for cmnd in commands_list:
            if cmnd == "l":
                direction_temp = (direction_temp-1)%4
            elif cmnd == "r":
                direction_temp = (direction_temp+1)%4
            elif cmnd == "f":
                if coordinates_temp[0] + movement_vectors[direction_temp][0] < 11 and coordinates_temp[0] + movement_vectors[direction_temp][0] > -11:
                    coordinates_temp[0] += movement_vectors[direction_temp][0]
                if coordinates_temp[1] + movement_vectors[direction_temp][1] < 11 and coordinates_temp[1] + movement_vectors[direction_temp][1] > -11:
                    coordinates_temp[1] += movement_vectors[direction_temp][1]
            elif cmnd == "b":
                if coordinates_temp[0] - movement_vectors[direction_temp][0] < 11 and coordinates_temp[1] - movement_vectors[direction_temp][1] > -11:
                    coordinates_temp[0] -= movement_vectors[direction_temp][0]
                if coordinates_temp[1] - movement_vectors[direction_temp][1] < 11 and coordinates_temp[1] - movement_vectors[direction_temp][1] > -11:
                    coordinates_temp[1] -= movement_vectors[direction_temp][1]
    return(coordinates_temp, direction_temp)

if __name__ == "__main__":
    main()