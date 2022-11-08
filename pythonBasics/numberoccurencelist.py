

# Total no of 1’s in 1 to 100 numbers
counter = 0
for i in range(1, 100 + 1):
    # Convert to String
    str1 = str(i)
    # counter = counter + str1.count("1")
    counter += str1.count("1")
print(counter)

list1 = [1, 1, 1, 2, 3, 2, 1]

# Counts the number of times 1 appears in list1
print(list1.count(1))

list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']

# Counts the number of times 'b' appears in list2
print(list2.count('b'))

list3 = ['Cat', 'Bat', 'Sat', 'Cat', 'cat', 'Mat']

# Counts the number of times 'Cat' appears in list3
print(list3.count('Cat'))

# index of element in the list

print(list3.index('Sat'))

# Remove elements from the list using pop

list3.pop(2)

print(list3)

# will clear the elements in the list and make it empty list
print(list3.clear())

print(len(list2))

print(len(list3))