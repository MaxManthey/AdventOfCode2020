import re

myfile = open("input.txt", "r").read()
inputar = myfile.split("\n\n")

replace_newline = [item.replace('\n', ' ') for item in inputar]

print(replace_newline)

correct_id_counter = 0

for item in replace_newline:
    passport = item.split(" ")
    if len(passport) > 6:
        if len(passport) == 8:
            correct_id_counter += 1
        else:
            single_credentials = []
            for credential in passport:
                single_credentials.append(credential.split(":"))
            flattened_list = [val for sublist in single_credentials for val in sublist]
            if not ("cid" in flattened_list):
                correct_id_counter += 1

print("Result Part 1: " + str(correct_id_counter))


def byr_check(input):
    return (input > 1919) and (input < 2003)


def iyr_check(input):
    return (input > 2009) and (input < 2021)


def eyr_check(input):
    return (input > 2019) and (input < 2031)


def hgt_check(unf_input):
    if "cm" in unf_input:
        unf_input = unf_input.replace("cm", "")
        fm_input = int(unf_input)
        return (fm_input > 149) and (fm_input < 194)
    elif "in" in unf_input:
        unf_input = unf_input.replace("in", "")
        fm_input = int(unf_input)
        return  (fm_input > 58) and (fm_input < 77)
    else:
        return False


def hcl_check(input):
    hcl_correct = re.match('^#(?:[0-9a-f]{6})$', input)
    if hcl_correct:
        return True
    else:
        return False


def ecl_check(input):
    ecl_correct = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return input in ecl_correct


def pid_check(input):
    pid_correct = re.match(r'^(?:[0-9]{9})$', input)
    if pid_correct:
        return True
    else:
        return False


# print(hgt_check("167cm"))

correct_id_counter = 0

for item in replace_newline:
    passport = item.split(" ")
    single_credentials = []
    for credential in passport:
        single_credentials.append(credential.split(":"))
    flattened_list = [val for sublist in single_credentials for val in sublist]
    if (len(passport) == 8) or ((len(passport) == 7) and not("cid" in flattened_list)):
        credential_dict = {}
        name_counter = 0
        value_counter = 1
        while value_counter < len(flattened_list):
            credential_dict[flattened_list[name_counter]] = flattened_list[value_counter]
            name_counter += 2
            value_counter += 2
        credentials_evaluation = [byr_check(int(credential_dict["byr"])),
                                  iyr_check(int(credential_dict["iyr"])),
                                  eyr_check(int(credential_dict["eyr"])),
                                  hgt_check(credential_dict["hgt"]), hcl_check(credential_dict["hcl"]),
                                  ecl_check(credential_dict["ecl"]), pid_check(credential_dict["pid"])]
        if not (False in credentials_evaluation):
            if len(passport) == 8:
                correct_id_counter += 1
            elif not ("cid" in flattened_list):
                correct_id_counter += 1

print("Result part 2: " + str(correct_id_counter))