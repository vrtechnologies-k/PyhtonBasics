
import keyword

#A common way to manage dependencies for a python project is via a file in root of the project
# named "requirements.txt". An easy way to make this is:

    #Setup a python virtualenv for your project
   # Manually install the required modules via pip
    #Execute pip freeze > requirements.txt to generate the requirements file

#You can then install all the dependencies in other locations using pip install -r requirements.txt.

# If you want dependencies to be installed automatically when other people pip install your package,

# you can use install_requires() in your setup.py.

#The best way I know is, create a file requirements.txt list out all the packages name in it
#
# and install it using pip

#pip install -r requirements.txt




# Difference between tuple and list

#list is a datatype that allows multiple values and can be different data types
# list is a mutable and we can change the values inside the list
# Tuple is same as list data type but immutable
# we cannot the change the values inside a tuple

#Difference between list and array

#list is a datatype that allows multiple values and can be different data types

# little trickyto handle arthematic operations in list

#array is a datatype that allows multiple values and can be same data type

# directly handled arthematic operations in array

#Difference between list and set

#List is mutable    						   Set immutable

#it is ordered collection of items		   it is unordered collection of items

#Items in list can be replaced or changed   Items in list cannot be replaced or changed

# Creating Empty set
set1 = set()

set1.add('Venkat')

print(set1)

set2 = {'James', 2, 3, 'Python'}

# Printing Set value
print(set2)

# Adding element to the set

set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)

# a = set()
print(type(set2))

print(keyword.kwlist)