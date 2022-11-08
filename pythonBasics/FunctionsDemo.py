#In Python, function is a group of related statements that perform a specific task.
#Function Declaration


def GreetMe(name):
    print("Good Morning"+name)
    #Function Call


def AddIntegers(a, b):
    return a+b


GreetMe("Rahul Shetty")

print(AddIntegers(2, 3))

# Local Variable
# Local variables are the variables that declared inside the function and have scope within the function.

def add():
    # Defining local variables. They has scope only within a function
    a=20
    b=30
    c=a+b
    print("The Sum is:",c)

add()

# A variable declared outside the function is the global variable by default.
# Python provides the global keyword to use global variable inside the function.
# If we don't use the global keyword, the function treats it as a local variable.

# Declare a variable and initialize it.
x = 101

# Global variable in function
def mainFunction():
    # printing a global variable
    global x
    #print(x)
    # modifying a global variable
    x = 'Welcome To Javatpoint'
    print(x)


mainFunction()
print(x)


# We can delete the variable using the del keyword. The syntax is given below.

x = 10
print(x)

del x
#print(x)


str1 = 'hello javatpoint' #string str1
str2 = ' how are you' #string str2
print (str1[0:2]) #printing first two character using slice operator
print (str1[4]) #printing 4th character of the string
print (str1*2) #printing the string twice
print (str1 + str2) #printing the concatenation of str1 and str2

# List

list1 = [1, "hi", "Python", 2]
# Checking type of given list
print(type(list1))

# Printing the list1
print(list1)

# List slicing
print(list1[3:])

# List slicing
print(list1[0:2])

# List Concatenation using + operator
print(list1 + list1)

# List repetation using * operator
print(list1 * 3)


# Tuple
tup = ("hi", "Python", 2)
# Checking type of tup
print(type(tup))

# Printing the tuple
print(tup)

# Tuple slicing
print(tup[1:])
print(tup[0:1])

# Tuple concatenation using + operator
print(tup + tup)

# Tuple repatation using * operator
print(tup * 3)

# Adding value to tup. It will throw an error.
# t[2] = "hi"

# Dictionary is an unordered set of a key-value pair of items. It is like an associative array or
# a hash table where each key stores a specific value. Key can hold any primitive data type, whereas value is an arbitrary Python object.

#The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}.

# Consider the following example.

d = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}

# Printing dictionary
print(d)

# Accesing value using keys
print("1st name is " + d[1])
print("2nd name is " + d[4])

print(d.keys())
print(d.values())


# Set

# Python Set is the unordered collection of the data type.
# It is iterable, mutable(can modify after creation), and has unique elements

# Creating Empty set
set1 = set()

set2 = {'James', 2, 3, 'Python'}

# Printing Set value
print(set2)

# Adding element to the set

set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)
