
list1  = [1, "hi", "Python", 2]
#Checking type of given list
print(type(list1))

# List slicing
print (list1[3:])  # print 3 index value in the list

# List slicing
print (list1[:3]) # print before 3 index values in the list

values = [1, 2, "venkat", 4, 5]

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  #5  # How to find the last index value in the python
print(values[1:3])  # 2 venkat
values.insert(3, "kandula")   #[1, 2, 'venkat', 'kandula', 4, 5]
print(values)
values.append("End")  #[1, 2, 'venkat', 'shetty', 4, 5, 'End']
print(values)

values[2] = "VENKAT" #Updating

del values[0]

print(values)  # [2, 'VENKAT', 'shetty', 4, 5, 'End']