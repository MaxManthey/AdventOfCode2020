myfile = open("input.txt", "r").read()
list_of_command = myfile.split("\n")
print(len(list_of_command))


# print(list_of_commands[0][4])

def part1(list_of_commands):
    index = 0
    list_of_indices = []
    accumulator = 0
    was_stopped = False
    print(list_of_commands)
    while not(index in list_of_indices): # or (index >= len(list_of_commands)):
        list_of_indices.append(index)
        command = list_of_commands[index][:3]
        if command == "nop":
            index += 1
        elif command == "acc":
            if list_of_commands[index][4] == "+":
                accumulator += int(list_of_commands[index][5:])
            else:
                accumulator -= int(list_of_commands[index][5:])
            index += 1
        else:
            if list_of_commands[index][4] == "+":
                index += int(list_of_commands[index][5:])
            else:
                index -= int(list_of_commands[index][5:])
        if index in list_of_indices:
            was_stopped = True
            break
        if index >= len(list_of_commands):
            break
    print("acc: " + str(accumulator))
    result = [accumulator, was_stopped]
    return result


def part2(list_of_commands):
    print(list_of_commands)
    last_index = len(list_of_commands)
    print("last index " + str(last_index))
    index = 0
    accumulator = 0
    # list_to_manipulate[index] = list_to_manipulate[index].replace("nop", "jmp")
    # print("original: " + list_of_commands[index])
    # print("fake " + list_to_manipulate[index])

    while index < last_index:
        if list_of_commands[index][:3] == "nop":
            list_of_commands[index] = list_of_commands[index].replace("nop", "jmp")
            result = part1(list_of_commands)
            if not result[1]:
                accumulator = result[0]
                break
            else:
                list_of_commands[index] = list_of_commands[index].replace("jmp", "nop")
        elif list_of_commands[index][:3] == "jmp":
            list_of_commands[index] = list_of_commands[index].replace("jmp", "nop")
            result = part1(list_of_commands)
            if not result[1]:
                accumulator = result[0]
                break
            else:
                list_of_commands[index] = list_of_commands[index].replace("nop", "jmp")
        index += 1
        # print(index)
        # if index == last_index:

    return str(accumulator)


result = part1(list_of_command)
print("Result 1: " + str(result[0]))
print("Result 2: " + part2(list_of_command))
