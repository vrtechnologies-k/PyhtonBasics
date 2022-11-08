
greeting = "Good Morning"
a = 4

if a > 2:
    print(" Condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

mx = a if a > 2 else 2

print("Largest Number is:", mx)

#for loop

# multiply the values in the list using 2

obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)


# sum of First Natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("*******************************")
for k in range(1, 10, 5):
    print(k)
    print("**************SKIPPING FIRST INDEX*****************")

for m in range(10):
    print(m)

age = 35

if age == 40:

    print("The age is 40")


elif age == 35:

    print("The age is 35")

    def season(i):
        switcher = {
            0: 'Winter',
            1: 'Summer',
            2: 'Spring',
            3: 'Autumn',
            4: 'Monsoon',
            5: 'Fall',
        }
        return switcher.get(i, "Invalid Season")

print(season(2))


a = 40
if a == 40:
  pass
print("If Statement Executed")














