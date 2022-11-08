# Arrange the list tuples in arranging and descending order

first_touple_elements = []

first_touple_element = [('a', 'b'), ('c', 'd')]

for first_touple in first_touple_element:
    first_touple_elements.append(first_touple[0])

print(first_touple_elements)

data = [(1, 'sravan'), (2, 'ojaswi'), (3, 'bobby'),
        (4, 'rohith'), (5, 'ganesh')]

data.sort(key=lambda x: x[-1])  # last index

print(data)

data.sort(key=lambda x: x[0])  # first index

print(data)

# Sort by the Second element value

my_data = [('P', 1), ('M', 3), ('A', 2), ('B', 4)]

my_data.sort(key=lambda tup: tup[1])

print(my_data)

# Sort by the First element value

my_data.sort(key=lambda tup: tup[0])

print(my_data)
