
# Reverse String

# When you pass -1 as step, the start point goes to the end and stop at the front

number1 = 123
print(str(number1)[::-1])

number2 = ""
for i in str(number1):
    number2 = i + str(number2)

print(str(number2))

str13 = "Venkat Kandula"
str14 = ""
for i in str13:
    str14 = i + str14

print(str14)
