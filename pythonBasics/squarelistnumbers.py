n = 4

square = n * n

print(square)

print(pow(n, 2))

arr = [2, 4, 8, 16]

squared_numbers = [number ** 2 for number in arr]

print(squared_numbers)

# Multipy the list with number 2

list_1 = [1, 2, 3, 4, 5]
new_list = []

# Using for loop
for i in range(1,len(list_1)+1):
    new_list.append(i*2)

print(new_list)

list_2 = [i * 2 for i in list_1]

print(list_2)