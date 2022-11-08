
# Function to demonstrate printing star pattern

myList = []
for i in range(1, 6):
    myList.append("*"*i)
print("\n".join(myList))

# Function to demonstrate printing triangle pattern

# number of spaces
k = 6 - 1

# outer loop to handle number of rows
for i in range(0, 6):

    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
        print(end=" ")

    # decrementing k after each loop
    k = k - 1

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

    # ending line after each row
    print("\r")

    # Function to demonstrate printing pattern of numbers

    # Number without reassigning

    # initializing starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, 6):

        # not re assigning num
        # num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")


    # Number pattern
    # initialising starting number
    num = 1

    # outer loop to handle number of rows
    for i in range(0, 5):

        # re assigning num
        num = 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            print(num, end=" ")

            # incrementing number at each column
            num = num + 1

        # ending line after each row
        print("\r")

    # Character pattern
        # initializing value corresponding to 'A'
        # ASCII value
        num = 65

        # outer loop to handle number of rows
        # 5 in this case
        for i in range(0, 5):

            # inner loop to handle number of columns
            # values changing acc. to outer loop
            for j in range(0, i + 1):
                # explicitly converting to char
                ch = chr(num)

                # printing char value
                print(ch, end=" ")

            # incrementing number
            num = num + 1

            # ending line after each row
            print("\r")

    # initializing value corresponding to 'A'
    # ASCII value
    num = 65

    # outer loop to handle number of rows
    # Continuous character pattern
for i in range(0, 5):

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # explicitly converting to char
        ch = chr(num)

        # printing char value
        print(ch, end=" ")

        # incrementing at each column
        num = num + 1

    # ending line after each row
    print("\r")