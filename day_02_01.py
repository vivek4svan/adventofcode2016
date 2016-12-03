def get_security_digit(code_line, i, j):
    print line.strip()
    for char in code_line:
        if char == "R" and j < 2:
            j += 1
        elif char == "L" and j > 0:
            j -= 1
        elif char == "U" and i > 0:
            i -= 1
        elif char == "D" and i < 2:
            i += 1
    return [i, j]


def create_lock_panel(size):
    for i in range(0, size*size, size):
        row = []
        for j in range(i+1, i + size + 1):
            row.append(j)
        lock_panel.append(row)

lock_panel = []
with open("day_02_01.txt") as f:
    i_pos = 1
    j_pos = 1
    lock_panel_size = 3
    create_lock_panel(lock_panel_size)
    for line in f:
        new_security_digit = get_security_digit(line.strip(), i_pos, j_pos)
        i_pos = new_security_digit[0]
        j_pos = new_security_digit[1]
        print "Security Code Digit : " + str(lock_panel[i_pos][j_pos])

print lock_panel
