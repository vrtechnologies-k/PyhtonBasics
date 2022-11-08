
str1 = "venkat kandula"

# using join() + sorted()
res = ''.join(sorted(str1))

res1 = ''.join(sorted(str1, reverse=True))

print(res)

print(res1)

number1 = 45287

res = ''.join(sorted(str(number1)))

res1 = ''.join(sorted(str(number1), reverse=True))

print(res)

print(res1)