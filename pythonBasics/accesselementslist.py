
names = ["Jack", "Jill", "Christopher", "Harvey"]

# append element to the list
names.append("Richard")

print(names)

# add multiple elements to the list

names.extend(["Robert", "Paul", "Vincent"])

print(names)

# print last element from the list

print(names[-1])

# print last but one element from the list

print(names[-2])

# print last but two element from the list

print(names[-3])

# remove the element from the list using string

names.remove("Paul")

print(names)

# To insert the elements at a defined index

names.insert(2, "venkat")

print(names)

# find element in the list

print("Robert" in names)

# slice the list , slice is nothing but we can cut the list from one index to another index

print(names[2:5])

