myfile = open("input.txt", "r").read()
inputar = myfile.split(",")


def number_game(numbers, wanted_number):
    spoken_numbers = {}
    for number in numbers:
        for amount in spoken_numbers:
            spoken_numbers[amount] += 1
        spoken_numbers[int(number)] = 0
    turns = len(numbers)
    last_number_spoken = numbers[len(numbers) - 1]
    while turns < wanted_number:
        if last_number_spoken in spoken_numbers:
            new_last_spoken = spoken_numbers[last_number_spoken]
            spoken_numbers[last_number_spoken] = 0
            last_number_spoken = new_last_spoken
        else:
            spoken_numbers[last_number_spoken] = 0
            last_number_spoken = 0
        spoken_numbers = {k: v + 1 for k, v in spoken_numbers.items()}
        turns += 1
    return last_number_spoken


def number_game2(numbers, wanted_number):
    spoken_numbers = {}
    turns = 0
    for number in numbers:
        turns += 1
        spoken_numbers[int(number)] = turns
    last_number_spoken = int(numbers[len(numbers) - 1])
    while turns < wanted_number:
        if last_number_spoken in spoken_numbers:
            new_last_spoken = turns - spoken_numbers[last_number_spoken]
            spoken_numbers[last_number_spoken] = turns
            last_number_spoken = new_last_spoken
        else:
            spoken_numbers[last_number_spoken] = turns
            last_number_spoken = 0
        # print(spoken_numbers)
        turns += 1
    return last_number_spoken

print("Result part 1: " + str(number_game2(inputar, 2020)))
print("Result part 2: " + str(number_game2(inputar, 30000000)))

