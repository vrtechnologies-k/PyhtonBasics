tup = ("hello", "Kandula", 2)
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
tup[2] = "hi"


# Tuple - Same as LIST Data type but immutable
# we cannot change the values inside a tuple

val = (1, 2, 2, "venkat", 4.5)

print(val[1])

#val[2] = "Venkat"

print(val)

 # length
print(len(val))

# Index of element in the tuple
print(val.index('venkat'))

# repetitive count of the elements in the tuple
print(val.count(2))
