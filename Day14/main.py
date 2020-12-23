myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")


def int_to_binary(number):
    result = []
    index = 0
    bin_num = "{0:b}".format(number)
    while index < 36 - len(bin_num):
        result.append("0")
        index += 1
    for char in bin_num:
        result.append(char)
    return result # "".join(result)


def binary_to_int(number):
    return int(number, 2)


def modify_input(all_commands):
    docking_programm = []
    parts_of_programm = []
    for command in all_commands:
        if command[:4] == "mask":
            docking_programm.append(parts_of_programm)
            parts_of_programm = [command[7:]]
        elif command[:3] == "mem":
            sub_list = []
            mems = command.split("]")
            sub_list.append(int(mems[0][4:]))
            sub_list.append(int(mems[1][3:]))
            parts_of_programm.append(sub_list)
    docking_programm.append(parts_of_programm)
    docking_programm.pop(0)
    return docking_programm


def all_mask_combinationes(mask):
    result = [""]
    for char in mask:
        if char == "X":
            new_result = []
            for masks in result:
                new_mask0 = masks + "0"
                new_mask1 = masks + "1"
                new_result.append(new_mask0)
                new_result.append(new_mask1)
            result = new_result
        else:
            new_result = []
            for masks in result:
                new_mask = masks + char
                new_result.append(new_mask)
            result = new_result
    return result


def part1(docking_programm):
    mems = {}
    for mask_parts in docking_programm:
        mask = str(mask_parts[0])
        index = 0
        for mem_commands in mask_parts:
            if index != 0:
                mem_part = mem_commands[0]
                bin_num = list(int_to_binary(mem_commands[1]))
                bin_index = 0
                for num in mask:
                    if num == "0" or num == "1":
                        bin_num[bin_index] = num
                    bin_index += 1
                mems[mem_part] = binary_to_int("".join(bin_num))
            index += 1
    result = 0
    for mem in mems:
        result += mems[mem]
    return result


def part2(docking_programm):
    mems = {}
    for mask_parts in docking_programm:
        mask = str(mask_parts[0])
        index = 0
        for mem_commands in mask_parts:
            if index != 0:
                bin_num = list(int_to_binary(mem_commands[0]))
                num_part = mem_commands[1]
                bin_index = 0
                for num in mask:
                    if num == "1":
                        bin_num[bin_index] = num
                    elif num == "X":
                        bin_num[bin_index] = num
                    bin_index += 1
                mask_combinations = all_mask_combinationes("".join(bin_num))
                for masks in mask_combinations:
                    mems[binary_to_int(masks)] = num_part
            index += 1
    result = 0
    for mem in mems:
        result += mems[mem]
    return result


print("Result part 1: " + str(part1(modify_input(inputar))))
print("Result part 2: " + str(part2(modify_input(inputar))))
