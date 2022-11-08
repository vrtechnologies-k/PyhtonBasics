
# print even numbers in the list

natural_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
evenlist = []
for i in range(1,len(natural_numbers)+1):
    if i % 2 == 0:
        evenlist.append(i)
print(evenlist)

oddlist = []
for i in range(1,len(natural_numbers)+1):
    if i % 2 !=0:
        oddlist.append(i)
print(oddlist)

even = [i for i in natural_numbers if i % 2 == 0]
odd = [i for i in natural_numbers if i % 2 != 0]
print(even)
print(odd)
