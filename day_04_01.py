def display_room_data(room_parameters):
    print "--------------------------"
    print "Room Code : " + room_parameters[0]
    print "Sector ID : " + str(room_parameters[1])
    print "Checksum  : " + room_parameters[2]


def extract_room_parameters(room_data):
    pos_sec_cksum = len(room_data) - 1
    len_sec_cksum = len(room_data[pos_sec_cksum])
    pos_sq_brackt = str(room_data[pos_sec_cksum]).index("[")
    room_code = "".join(room_data[:pos_sec_cksum])
    sector_id = room_data[pos_sec_cksum][:pos_sq_brackt]
    checksum = room_data[pos_sec_cksum][pos_sq_brackt+1:len_sec_cksum-1]
    return [room_code, int(sector_id), checksum]


def check_room_for_real(room_parameters):
    dict_code = {}
    ordered_code = []
    set_of_chars = set(room_parameters[0])
    for char in set_of_chars:
        count = room_parameters[0].count(char)
        dict_code[char] = count
    set_of_value = sorted(set(dict_code.values()),reverse=True)
    for i in set_of_value:
        elem = sorted([key for key, value in dict_code.items() if value == i])
        for char in elem:
            ordered_code.append(char)
    valid = match_checksum(room_parameters[2], "".join(ordered_code))
    if valid:
        return room_parameters[1]
    else:
        return 0


def match_checksum(room_cksum, ordered_code):
    if room_cksum in ordered_code:
        return True
    else:
        return False

sum_sector_id = 0
with open("day_04_01.txt","r") as f:
    for line in f:
        room_params = extract_room_parameters(line.strip().split("-"))
        display_room_data(room_params)
        sum_sector_id += check_room_for_real(room_params)

print "\n Sum of Sector ID(s) of Valid Rooms is : " + str(sum_sector_id)
