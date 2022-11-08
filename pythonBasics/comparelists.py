list1 = [11, 12, 13, 14, 15]
list2 = [12, 13, 11, 15, 14]

a = set(list1)
b = set(list2)

if a == b:
    print("The list1 and list2 are equal")
else:
    print("The list1 and list2 are not equal")

list3 = ["venkat", "kandula", "reddy"]
list4 = ["reddy", "venkat", "kandula"]

if set(list3) == set(list4):
    print("The list3 and list4 are equal")
else:
    print("The list3 and list4 are not equal")