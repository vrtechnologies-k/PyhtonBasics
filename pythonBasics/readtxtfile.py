
fs = open(r"D:\Projects\pythonBasics\normalfile.txt",'r')

# It will read the entire file
con2 = fs.read()

# It will read the 4 characters from the text file
con = fs.read(4)
# It will read the 10 characters from the text file
con1 = fs.read(10)

print(con)
print(con1)
print(con2)
# It will read the entire file
fs.close()
