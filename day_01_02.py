def move_left(value, position):
    global x, y
    new_position = calc_new_pos(position, "L")
    for i in range(int(value)):
        if new_position == 0:
            y += 1
        elif new_position == 1:
            x += 1
        elif new_position == 2:
            y -= 1
        elif new_position == 3:
            x -= 1
        if [x, y] in visited_pool:
            return -1
        else:
            visited_pool.append([x, y])
    return new_position


def move_right(value, position):
    global x, y
    new_position = calc_new_pos(position, "R")
    for i in range(int(value)):
        print i
        if new_position == 0:
            y += 1
        elif new_position == 1:
            x += 1
        elif new_position == 2:
            y -= 1
        elif new_position == 3:
            x -= 1
        if [x, y] in visited_pool:
            return -1
        else:
            visited_pool.append([x, y])
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
    global x, y
    position = 0
    for instruction in instructions:
        if "L" in instruction:
            new_pos = move_left(instruction[1:], position)
        elif "R" in instruction:
            new_pos = move_right(instruction[1:], position)
        position = new_pos
        if new_pos == -1:
            break
        print instruction + " : [" + str(x) + ", " + str(y) + "]"


visited_pool = []
x = 0
y = 0
with open("day_01_01.txt", "r") as f:
    for line in f:
        move_santa(line.split(', '))

print visited_pool
print "\nFinal Co-ordinates : [" + str(x) + ", " + str(y) + "]"
print "Total Distance from origin : " + str(abs(0-x) + abs(0-y))
