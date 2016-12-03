def triangles_set(triangle_data_3):
    valid_triangle = []
    for i in range(3):
        new_set = [int(triangle_data_3[0][i]), int(triangle_data_3[1][i]), int(triangle_data_3[2][i])]
        valid_triangle.append(chk_triangle_possibility(new_set))
    return valid_triangle.count(True)


def chk_triangle_possibility(triangle_data):
    for i in range(3):
        if triangle_data[i] >= sum(triangle_data) - triangle_data[i]:
            return False
    return True

valid = 0
with open("day_03_01.txt") as f:
    lines_3 = []
    for line in f:
        lines_3.append(line.strip().split())
        if len(lines_3) % 3 == 0:
            valid += triangles_set(lines_3)
            lines_3 = []

print "\nNo of possible Triangles : " + str(valid)
