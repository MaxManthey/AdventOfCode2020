myfile = open("input.txt", "r").read()
inputar = myfile.split("\n\n")


def modify_input(ticket_input):
    train_data = []
    for line in ticket_input:
        train_data.append(line.split("\n"))

    val_data = train_data[0]
    validations = []
    for line in val_data:
        val_parts = line.split(": ")
        val_nums = val_parts[1].split(" or ")
        validations.append(val_nums)

    my_ticket = train_data[1]
    my_ticket.pop(0)
    nearby_tickets = train_data[2]
    nearby_tickets.pop(0)
    return list([validations, my_ticket, nearby_tickets])


def number_is_valid(number, validations):
    for rule in validations:
        rule1 = rule[0].split("-")
        rule2 = rule[1].split("-")
        if (int(rule1[0]) <= number <= int(rule1[1])) or (int(rule2[0]) <= number <= int(rule2[1])):
            return list([True, rule])
    return list([False, 0])


def all_valid_tickets(validations, nearby_tickets):
    valid_tickets = []
    for ticket in nearby_tickets:
        single_numbers = ticket.split(",")
        ticket_is_valid = True
        for number in single_numbers:
            if not number_is_valid(int(number), validations)[0]:
                ticket_is_valid = False
                break
        if ticket_is_valid:
            valid_tickets.append(ticket)
    return valid_tickets


def possible_rules(ticket_nums, validations):
    all_rules = []
    for ticket in ticket_nums:
        all_rules.append(number_is_valid(int(ticket), validations)[1])
    return all_rules


def part1(train_data):
    validations = train_data[0]
    nearby_tickets = train_data[2]
    invalid_tickets = 0
    for ticket in nearby_tickets:
        single_numbers = ticket.split(",")
        for number in single_numbers:
            if not number_is_valid(int(number), validations)[0]:
                invalid_tickets += int(number)
                break
    return invalid_tickets


def part2(train_data):
    validations = train_data[0]
    my_ticket = train_data[1]
    my_ticket = my_ticket[0].split(",")
    nearby_tickets = train_data[2]

    valid_tickets = all_valid_tickets(validations, nearby_tickets)

    index = 0
    ticket_indices = []
    while index < len(valid_tickets[0].split(",")):
        ticket_at_index = []
        for ticket in valid_tickets:
            ticket_nums = ticket.split(",")
            ticket_at_index.append(ticket_nums[index])
        index += 1
        ticket_indices.append(ticket_at_index)
    # print(ticket_indices[0])

    index_rules = []
    for ticket_index in ticket_indices:
        index_rules.append(possible_rules(ticket_index, validations))
    # print(index_rules)

    ticket_number_positions = []
    for i in range((len(valid_tickets[0].split(",")))):
        ticket_number_positions.append(-1)

    while -1 in ticket_number_positions:
        for index in ticket_number_positions:
            if index != -1:
                validations[index] = ['0-0', '0-0']
        first_neg_one = ticket_number_positions.index(-1)
        new_possible_rules = possible_rules(ticket_indices[first_neg_one], validations)
        # print(new_possible_rules)
        highest_index = -1
        for rule in new_possible_rules:
            validation_index = 0
            for validation in validations:
                if rule == validation:
                    break
                validation_index += 1
            if validation_index > highest_index:
                highest_index = validation_index
        ticket_number_positions[first_neg_one] = highest_index
    print(ticket_number_positions)
    print(validations)

    to_multiply = 1
    for number in ticket_number_positions:
        # print(number)
        if number < 6:
            # print("hit it")
            to_multiply *= int(my_ticket[number])
    return to_multiply


# print("Result part 1: " + str(part1(modify_input(inputar))))
print("Result part 2: " + str(part2(modify_input(inputar))))

# 441254988313 too low
# 1429779530273 correct
