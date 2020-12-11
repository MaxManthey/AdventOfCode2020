myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")

list_of_number = list(map(lambda x: int(x), inputar))


def part1(list_of_numbers):
    list_of_numbers.append(0)
    list_of_numbers.sort()
    list_of_numbers.append(list_of_numbers[len(list_of_numbers) - 1] + 3)
    ones = []
    threes = []
    index = 1
    for number in list_of_numbers:
        if index + 1 == len(list_of_numbers):
            threes.append(list_of_numbers[index] + 3)
            break
        elif list_of_numbers[index] - number == 1:
            ones.append(list_of_numbers[index])
        elif list_of_numbers[index] - number == 3:
            threes.append(list_of_numbers[index])
        index += 1
    result = len(ones) * len(threes)
    print("Result part 1: " + str(result))


def part2(list_of_numbers):
    list_of_numbers.append(0)
    list_of_numbers.sort()
    last_number = list_of_numbers[len(list_of_numbers) - 1] + 3
    list_of_numbers.append(last_number)
    dict_of_numbers = dict()

    for number in list_of_numbers:
        if number == 0:
            dict_of_numbers[number] = 1
        else:
            dict_of_numbers[number] = 0
            if number - 1 in dict_of_numbers:
                dict_of_numbers[number] = dict_of_numbers[number] + dict_of_numbers[number - 1]
            if number - 2 in dict_of_numbers:
                dict_of_numbers[number] = dict_of_numbers[number] + dict_of_numbers[number - 2]
            if number - 3 in dict_of_numbers:
                dict_of_numbers[number] = dict_of_numbers[number] + dict_of_numbers[number - 3]
        print(dict_of_numbers)
    print("Result part 2: " + str(dict_of_numbers[last_number]))


part1(list_of_number)
part2(list_of_number)
