# Day 2: Bathroom Security
# Part 2

def get_security_digit(code_line, i, j):
    print line.strip()
    for char in code_line:
        if char == "R" and lock_panel[i][j+1] != "0":
            j += 1
        elif char == "L" and lock_panel[i][j-1] != "0":
            j -= 1
        elif char == "U" and lock_panel[i-1][j] != "0":
            i -= 1
        elif char == "D" and lock_panel[i+1][j] != "0":
            i += 1
    return [i, j]


def create_lock_panel(size):
    lock_panel.append(["0", "0", "0", "0", "0", "0", "0"])
    lock_panel.append(["0", "0", "0", "1", "0", "0", "0"])
    lock_panel.append(["0", "0", "2", "3", "4", "0", "0"])
    lock_panel.append(["0", "5", "6", "7", "8", "9", "0"])
    lock_panel.append(["0", "0", "A", "B", "C", "0", "0"])
    lock_panel.append(["0", "0", "0", "D", "0", "0", "0"])
    lock_panel.append(["0", "0", "0", "0", "0", "0", "0"])

lock_panel = []
with open("day_02_01.txt") as f:
    i_pos = 3
    j_pos = 1
    lock_panel_size = 3
    create_lock_panel(lock_panel_size)
    for line in f:
        new_security_digit = get_security_digit(line.strip(), i_pos, j_pos)
        i_pos = new_security_digit[0]
        j_pos = new_security_digit[1]
        print "Security Code Digit : " + str(lock_panel[i_pos][j_pos])
