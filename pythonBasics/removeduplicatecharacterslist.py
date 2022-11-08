l = [1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5]

l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(l1)



value = [1,2,3,4,5]
try:
    value = value[5]/0
except(ZeroDivisionError):
    print('Zero', end= "")
else:
    print('Hello world', end = "")
finally:
    print("Water", end="")

    k = 0
    while k<2:
        print k
    k++