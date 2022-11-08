sqaure_numbers = [2, 4, 6, 8, 10]

unsqu_list = []

count = 1

for i in range(0, len(sqaure_numbers)):
    unsqu_list.append(sqaure_numbers[i] - count)
    print(unsqu_list)
    count = count + 1
print(unsqu_list)