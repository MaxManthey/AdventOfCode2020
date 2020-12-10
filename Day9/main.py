myfile = open("input.txt", "r").read()
list_of_numbers = myfile.split("\n")


# PART 1

result_part1 = -1
index = 0
while True:
    test_index = index + 25
    sub_list = list_of_numbers[index:test_index]
    number_to_test = int(list_of_numbers[test_index])

    not_found = False
    check_sublist_index = 0
    for number in sub_list:
        if str(number_to_test - int(number)) in sub_list:
            complementing_number = number_to_test - int(number)
            if int(complementing_number) != int(number):
                break
        elif check_sublist_index == 24:
            not_found = True
            result_part1 = number_to_test
        check_sublist_index += 1
    if not_found:
        break
    index += 1

print("result: " + str(result_part1))


# PART 2

list_start = 0
list_end = 1
list_to_sum = [int(list_of_numbers[list_start])]
list_of_numbers.remove(str(result_part1))

while True:
    testme = sum(list_to_sum)
    if testme == result_part1:
        break
    elif testme < result_part1:
        list_to_sum.append(int(list_of_numbers[list_end]))
        list_end += 1
    elif testme > result_part1:
        list_start += 1
        list_end = list_start + 1
        list_to_sum = [int(list_of_numbers[list_start])]
    elif list_end == len(list_of_numbers) - 1 or list_start + 1 == len(list_of_numbers) - 1:
        print("bra :( bra :(")
        break

print("Result")
print(list_to_sum)
smallest = list_to_sum[0]
biggest = list_to_sum[0]
for number in list_to_sum:
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(smallest + biggest)
