
list_1 = [1, 2, 4, 5]
list_2 = [2, 5, 4, 8]
list_3 = [4, 8, 7, 3]

x = zip(list_1, list_2, list_3)

new_list = []
new_list1 = []
new_list2 = []
new_list3 = []

for l1, l2, l3 in zip(list_1, list_2, list_3):

    new_list.append(l1 * l2 * l3 * 2)
    new_list1.append(l1 * 2)
    new_list2.append(l2 * 2)
    new_list3.append(l3 * 2)

print(new_list)
print(new_list1)
print(new_list2)
print(new_list3)
print(tuple(x))