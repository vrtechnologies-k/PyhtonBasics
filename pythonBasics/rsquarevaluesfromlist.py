natural_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

even_list = []
unsqu_list = []

count = 1

for i in range(1,len(natural_numbers)+1):
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

list_1 = [25, 27, 36, 9, 15, 64, 16, 4]

even_numbers = []

for i in range(1,len(list_1)+1):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
