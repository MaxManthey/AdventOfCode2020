myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")


def count_occupied(seat_plan):
    counter = 0
    for row in seat_plan:
        for seat in row:
            if seat == "#":
                counter += 1
    return counter


def occupy_seat(seat):
    if seat == "L":
        return "#"
    else:
        return "."


def occupy_all_seats(seat_plan):
    new_row = []
    for row in seat_plan:
        new_row.append(list(map(occupy_seat, row)))
    return new_row


def seat_occupied(seatplan, row_to_check, seat_to_check):
    row_length = len(seatplan) - 1
    seat_length = len(seatplan[0]) - 1
    if seat_to_check < 0 or row_to_check < 0 or row_to_check > row_length or seat_to_check > seat_length:
        return 0
    elif seatplan[row_to_check][seat_to_check] == "#":
        return 1
    else:
        return 0


def surrounding_seats(seat_plan, row_to_check, seat_to_check):
    return(seat_occupied(seat_plan, row_to_check, seat_to_check - 1) +  # left
           seat_occupied(seat_plan, row_to_check, seat_to_check + 1) +  # right
           seat_occupied(seat_plan, row_to_check - 1, seat_to_check) +  # above
           seat_occupied(seat_plan, row_to_check + 1, seat_to_check) +  # bottom
           seat_occupied(seat_plan, row_to_check - 1, seat_to_check - 1) +  # above left
           seat_occupied(seat_plan, row_to_check + 1, seat_to_check - 1) +  # below left
           seat_occupied(seat_plan, row_to_check - 1, seat_to_check + 1) +  # above right
           seat_occupied(seat_plan, row_to_check + 1, seat_to_check + 1))  # above left


def part1(seat_plan):
    seat_plan = occupy_all_seats(seat_plan)
    state_changed = True

    while state_changed:
        state_changed = False
        new_seats = []
        row_to_check = 0
        for row in seat_plan:
            new_row = []
            seat_to_check = 0
            for seat in row:
                if seat == ".":
                    new_row.append(".")
                else:
                    adjacent_seats = surrounding_seats(seat_plan, row_to_check, seat_to_check)
                    if seat == "#" and adjacent_seats > 3:
                        new_row.append("L")
                        state_changed = True
                    elif seat == "L" and adjacent_seats == 0:
                        new_row.append("#")
                        state_changed = True
                    else:
                        new_row.append(seat)
                seat_to_check += 1
            new_seats.append(new_row)
            row_to_check += 1
        seat_plan = new_seats

    return count_occupied(seat_plan)


print("Result part 1: " + str(part1(inputar)))



def seat_occupied_part2(seatplan, row_to_check, seat_to_check, position):
    row_length = len(seatplan) - 1
    seat_length = len(seatplan[0]) - 1
    if seat_to_check < 0 or row_to_check < 0 or row_to_check > row_length or seat_to_check > seat_length:
        # print("oob: " + position)
        return 0
    elif seatplan[row_to_check][seat_to_check] == "#":
        # print("oc: " + position)
        return 1
    elif seatplan[row_to_check][seat_to_check] == "L":
        # print("em: " + position)
        return 0
    else:
        if position == "l":
            return seat_occupied_part2(seatplan, row_to_check, seat_to_check - 1, "l")
        elif position == "r":
            return seat_occupied_part2(seatplan, row_to_check, seat_to_check + 1, "r")
        elif position == "a":
            return seat_occupied_part2(seatplan, row_to_check - 1, seat_to_check, "a")
        elif position == "b":
            return seat_occupied_part2(seatplan, row_to_check + 1, seat_to_check, "b")
        elif position == "al":
            return seat_occupied_part2(seatplan, row_to_check - 1, seat_to_check - 1, "al")
        elif position == "bl":
            return seat_occupied_part2(seatplan, row_to_check + 1, seat_to_check - 1, "bl")
        elif position == "ar":
            return seat_occupied_part2(seatplan, row_to_check - 1, seat_to_check + 1, "ar")
        else:
            return seat_occupied_part2(seatplan, row_to_check + 1, seat_to_check + 1, "br")


def surrounding_seats_part2(seat_plan, row_to_check, seat_to_check):
    return(seat_occupied_part2(seat_plan, row_to_check, seat_to_check - 1, "l") +  # left
           seat_occupied_part2(seat_plan, row_to_check, seat_to_check + 1, "r") +  # right
           seat_occupied_part2(seat_plan, row_to_check - 1, seat_to_check, "a") +  # above
           seat_occupied_part2(seat_plan, row_to_check + 1, seat_to_check, "b") +  # bottom
           seat_occupied_part2(seat_plan, row_to_check - 1, seat_to_check - 1, "al") +  # above left
           seat_occupied_part2(seat_plan, row_to_check + 1, seat_to_check - 1, "bl") +  # below left
           seat_occupied_part2(seat_plan, row_to_check - 1, seat_to_check + 1, "ar") +  # above right
           seat_occupied_part2(seat_plan, row_to_check + 1, seat_to_check + 1, "br"))  # below right


def part2(seat_plan):
    seat_plan = occupy_all_seats(seat_plan)
    state_changed = True

    while state_changed:
        state_changed = False
        new_seats = []
        row_to_check = 0
        for row in seat_plan:
            new_row = []
            seat_to_check = 0
            for seat in row:
                if seat == ".":
                    new_row.append(".")
                else:
                    adjacent_seats = surrounding_seats_part2(seat_plan, row_to_check, seat_to_check)
                    if seat == "#" and adjacent_seats >= 5:
                        new_row.append("L")
                        state_changed = True
                    elif seat == "L" and adjacent_seats == 0:
                        new_row.append("#")
                        state_changed = True
                    else:
                        new_row.append(seat)
                seat_to_check += 1
            new_seats.append(new_row)
            row_to_check += 1
        seat_plan = new_seats
        print("\n")
        for row in seat_plan:
            print(row)
    return count_occupied(seat_plan)


print("Result part 2: " + str(part2(inputar)))

# print(surrounding_seats_part2(inputar, 8, 0))
