list1 = [10, 25, 1, 4, 45, 78, 5]

largest = 0

for i in range(len(list1)):
    if list1[i] > largest:
        largest = list1[i]

print(largest)

# sort the list in descending order
print(sorted(list1, reverse=True))

# 2 largest number in the list
newlist = sorted(list1, reverse=True)

print(newlist[1])

# Sort the String in descending order
print(sorted('venkat', reverse=True))

# reverse the String
s = "Welcome To Automation"

reverse_name= s[::-1]
print(reverse_name)

str1 = ""
for i in s:
    str1 = i + str1
print(str1)

#2 largest number in the List

list_val = [20, 30, 40, 25, 10]
# sorting the list in ascending order
list_val.sort()
print(list_val)
# Displaying the second last element of the list
print("The second largest element of the list is:", list_val[-2])