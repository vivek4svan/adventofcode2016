def display_room_data(room_parameters):
    """
    Used to just display the room attributes in original form [slightly formatted]
    :param room_parameters: List of room attributes.
                            Accepts room code and sector id as input for displaying these in readable format.
    :return: Nothing
    """
    print "--------------------------"
    print "Room Code : " + room_parameters[0]
    print "Sector ID : " + str(room_parameters[1])


def extract_room_parameters(room_data):
    """
    This function extracts the info from input string and parses to individual elements of list for room data.
    :param room_data: it is list of strings from input strings split by "-"
    :return: returns formatted list of attributes of room i.e. room code and sector id
    """
    pos_sec_cksum = len(room_data) - 1
    pos_sq_brackt = str(room_data[pos_sec_cksum]).index("[")
    room_code = "".join(room_data[:pos_sec_cksum])
    sector_id = int(room_data[pos_sec_cksum][:pos_sq_brackt])
    return [room_code, sector_id]


def shift_cipher(room_data):
    """
    Follows the shift cipher algorithm to determine the actual value of the input string for room code
    when rotated by sector_id times the actual value.
    :param room_data: Input of type list having Encrypted Room Code and Sector Id.
    :return: New decrypted room code (as string) after processing shift cipher
    """
    room_code = room_data[0]
    sector_id = room_data[1]
    new_code = ""
    increase_by = (sector_id % 26)
    for char in room_code:
        inc = increase_by
        if ord(char) + inc > 122:
            inc = increase_by - (122 - ord(char))
            new_code += chr(96 + inc)
        else:
            new_code += chr(ord(char) + increase_by)
    return new_code


def main():
    """
    This is the main function which reads the input from file and sends it to
    various functions in sequences to calculate the output.
    :return: Nothing
    """
    with open("day_04_01.txt","r") as f:
        for line in f:
            room_params = extract_room_parameters(line.strip().split("-"))
            new_room_code = shift_cipher(room_params)
            if "northpoleobjects" in new_room_code:
                print "\n!!! Gotcha !!! "
                display_room_data(room_params)
                print "Decoded   : " + new_room_code

if __name__ == "__main__":
    main()
