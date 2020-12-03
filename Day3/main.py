myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")
line_length = len(inputar[0]) - 1


def calculate_route(right, down):
    current_index = 0
    tree_counter = 0
    skip_line_counter = down - 1
    liner = 0

    for line in inputar:
        if skip_line_counter == down - 1:
            liner += 1
            if line[current_index] == "#":
                tree_counter += 1
            if (current_index + right) > line_length:
                current_index = (current_index + right - 1) - line_length
            else:
                current_index += right
            skip_line_counter = 0
        else:
            skip_line_counter += 1
    return tree_counter


one_one = calculate_route(1, 1)
three_one = calculate_route(3, 1)
five_one = calculate_route(5, 1)
seven_one = calculate_route(7, 1)
one_two = calculate_route(1, 2)

print("one_one " + str(one_one))
print("three_one " + str(three_one))
print("five_one " + str(five_one))
print("seven_one " + str(seven_one))
print("one_two " + str(one_two))

print(one_one * three_one * five_one * seven_one * one_two)