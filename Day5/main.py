myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")

highest_id = 0
list_of_ids = []


# PART 1

def string_to_value(string, zero_value, one_value):
    result = []
    for char in string:
        if char == zero_value:
            result.append('0')
        elif char == one_value:
            result.append('1')
    return int(''.join(result), 2)


for item in inputar:
    row_str = item[:7]
    column_str = item[7:]
    row_index = string_to_value(row_str, "F", "B")
    column_index = string_to_value(column_str, "L", "R")
    new_id = row_index * 8 + column_index
    list_of_ids.append(new_id)
    if highest_id < new_id:
        highest_id = new_id


print("Result part 1: " + str(highest_id))


# PART 2

list_of_ids.sort()
my_seat = -1

for seat_id in list_of_ids:
    if not(seat_id + 1 in list_of_ids) and (seat_id + 2 in list_of_ids):
        my_seat = seat_id + 1
        break

print("Result part 2: " + str(my_seat))
