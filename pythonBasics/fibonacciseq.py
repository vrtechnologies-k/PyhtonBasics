
# In Fibonacci series, following number is the sum of the preceding two numbers.
a = 0
b = 1
count = 0
n = 13

while count < n:
    print(a)
    c = a + b
    # At last, we will update values
    a = b
    b = c
    count += 1