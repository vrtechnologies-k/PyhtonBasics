# prime number between 1 to 10

# we used For Loop to iterate a loop between 1 and 100 values.
for i in range(1, 11):
    count = 0
    # Within the for loop, we used another For Loop to check whether the number is divisible or not
    for j in range(2, (i // 2 + 1)):
        # If true, count incremented, and break statement skip that number
        if (i % j == 0):
            count = count + 1
            break

    # Next, the if statement checks whether the count is zero, and the given number is not equal to 1.
    # If it is true, it prints the number because it is a Prime Number.
    if count == 0 and i != 1:
        print(" %d" % i, end='  ')
