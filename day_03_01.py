def chk_triangle_possibility(triangle_data):
    for i in range(3):
        if triangle_data[i] >= sum(triangle_data) - triangle_data[i]:
            return False
    return True

possible_triangles = []
with open("day_03_01.txt") as f:
    for line in f:
        possible_triangles.append(chk_triangle_possibility([int(a) for a in (line.strip().split())]))
print possible_triangles.count(True)
