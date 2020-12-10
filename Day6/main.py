myfile = open("input.txt", "r").read()
groups = myfile.split("\n\n")


result_one = 0

for group in groups:
    person = group.split("\n")
    group_answers = set()
    for answers in person:
        for answer in answers:
            group_answers.add(answer)
    result_one += len(group_answers)

print("Result part 1: " + str(result_one))


result_two = 0
for group in groups:
    person = group.split("\n")
    group_sets = []
    for answers in person:
        individual_answers = set()
        for answer in answers:
            individual_answers.add(answer)
        group_sets.append(individual_answers)
    result_two += len(group_sets[0].intersection(*group_sets))

print(result_two)
