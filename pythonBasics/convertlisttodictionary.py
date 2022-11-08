
# We can convert the list into dictionary using the dictionary comprehension

student = ["James", "Abhinay", "Peter", "Bicky"]

student_dictionary = {stu : "passed" for stu in student}
print(student_dictionary)