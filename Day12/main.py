myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")

possible_directions = ["N", "E", "S", "W"]


def turn_right(facing_direction, value):
    direction_index = possible_directions.index(facing_direction)
    value = int(value)
    while value > 0:
        value -= 90
        if direction_index + 1 > len(possible_directions) - 1:
            direction_index = 0
        else:
            direction_index += 1
    return possible_directions[direction_index]


def turn_left(facing_direction, value):
    direction_index = possible_directions.index(facing_direction)
    value = int(value)
    while value > 0:
        value -= 90
        if direction_index - 1 < 0:
            direction_index = len(possible_directions) - 1
        else:
            direction_index -= 1
    return possible_directions[direction_index]


def manhattan_distance(ew, ns):
    return abs(ew) + abs(ns)


def part1(actions):
    facing_direction = "E"
    east_west = 0
    north_south = 0

    for action in actions:
        command = action[:1]
        value = action[1:]
        if command == "R":
            facing_direction = turn_right(facing_direction, value)
        elif command == "L":
            facing_direction = turn_left(facing_direction, value)
        elif command == "F":
            if facing_direction == "E":
                east_west += int(value)
            elif facing_direction == "W":
                east_west -= int(value)
            elif facing_direction == "N":
                north_south += int(value)
            else:
                north_south -= int(value)
        elif command == "E":
            east_west += int(value)
        elif command == "W":
            east_west -= int(value)
        elif command == "N":
            north_south += int(value)
        else:
            north_south -= int(value)

    return manhattan_distance(east_west, north_south)


print("Result part 1: " + str(part1(inputar)))


def rotate_wp_right(wp_ew, wp_ns, value):
    rotated_points = []
    value = int(value)

    while value > 0:
        value -= 90
        hold_ew = wp_ew * -1
        wp_ew = wp_ns
        wp_ns = hold_ew

    rotated_points.append(wp_ew)
    rotated_points.append(wp_ns)
    return rotated_points


def rotate_wp_left(wp_ew, wp_ns, value):
    rotated_points = []
    value = int(value)

    while value > 0:
        value -= 90
        hold_ns = wp_ns * -1
        wp_ns = wp_ew
        wp_ew = hold_ns

    rotated_points.append(wp_ew)
    rotated_points.append(wp_ns)
    return rotated_points


def part2(actions):
    wp_ew = 10
    wp_ns = 1
    s_ew = 0
    s_ns = 0

    for action in actions:
        command = action[:1]
        value = action[1:]
        if command == "E":
            wp_ew += int(value)
        elif command == "W":
            wp_ew -= int(value)
        elif command == "N":
            wp_ns += int(value)
        elif command == "S":
            wp_ns -= int(value)
        elif command == "F":
            s_ew += wp_ew * int(value)
            s_ns += wp_ns * int(value)
        elif command == "R":
            new_wps = rotate_wp_right(wp_ew, wp_ns, value)
            wp_ew = new_wps[0]
            wp_ns = new_wps[1]
        else:
            new_wps = rotate_wp_left(wp_ew, wp_ns, value)
            wp_ew = new_wps[0]
            wp_ns = new_wps[1]
        print(command + " " + value)
        print("wp_ew: " + str(wp_ew) + "  wp_ns: " + str(wp_ns))
        print("s_ew: " + str(s_ew) + "  s_ns: " + str(s_ns) + "\n")

    return manhattan_distance(s_ew, s_ns)


print("Result part 2: " + str(part2(inputar)))