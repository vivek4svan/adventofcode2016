def move_left(value, position):
    new_position = calc_new_pos(position, "L")
    if new_position == 0:
        coordinate[1] += int(value)
    elif new_position == 1:
        coordinate[0] += int(value)
    elif new_position == 2:
        coordinate[1] -= int(value)
    elif new_position == 3:
        coordinate[0] -= int(value)
    return new_position


def move_right(value, position):
    new_position = calc_new_pos(position, "R")
    if new_position == 0:
        coordinate[1] += int(value)
    elif new_position == 1:
        coordinate[0] += int(value)
    elif new_position == 2:
        coordinate[1] -= int(value)
    elif new_position == 3:
        coordinate[0] -= int(value)
    return new_position


def calc_new_pos(old_position, direction):
    new_position = old_position
    if old_position == 0 and direction == "L":
        new_position = 3
    elif old_position != 0 and direction == "L":
        new_position -= 1
    if old_position == 3 and direction == "R":
        new_position = 0
    elif old_position != 3 and direction == "R":
        new_position += 1
    return new_position


def move_santa(instructions):
    position = 0
    for instruction in instructions:
        if "L" in instruction:
            new_pos = move_left(instruction[1:], position)
        elif "R" in instruction:
            new_pos = move_right(instruction[1:], position)
        position = new_pos
        print instruction
        print coordinate

coordinate = [0, 0]
with open("day_01_01.txt", "r") as f:
    for line in f:
        move_santa(line.split(', '))

print "\nFinal Co-ordinates : " + str(coordinate)
print "Total Distance from origin : " + str(abs(0-coordinate[0]) + abs(0-coordinate[1]))
