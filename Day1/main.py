myfile = open("input.txt", "r").read()
inputar = myfile.split("\n")
intar = []

for num in inputar:
    intar.append(int(num))


res1 = 0
res2 = 0
for num1 in intar:
    for num2 in intar:
        if num2 + num1 == 2020:
            res1 = num1
            res2 = num2
            break

result = res1 * res2
print("Result 1: " + str(result))


result = 0
intar.sort()
start = 0
middle = 1
end = len(intar) - 1
while 1:
    if intar[start] + intar[middle] + intar[end] == 2020:
        print("numbers: " + str(intar[start])+ " " + str(intar[middle]) + " " + str(intar[end]))
        print("Result 2: " + str(intar[start] * intar[middle] * intar[end]))
        break
    elif intar[start] + intar[middle] + intar[end] < 2020:
        middle += 1
    elif (intar[start] + intar[middle] + intar[end] > 2020) and (middle != start+1):
        start += 1
        middle = start + 1
    else:
        start = 0
        middle = 1
        end -= 1
