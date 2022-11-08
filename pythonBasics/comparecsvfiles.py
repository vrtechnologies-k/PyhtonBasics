import csv

with open('D:\Projects\pythonBasics\TransactionDetails.csv', 'r') as t1, open('D:\Projects\pythonBasics\TransactionDetails - Copy.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('../update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)


with open('D:\Projects\pythonBasics\TransactionDetails.csv', 'r') as t1:
    file = t1.readline()
    print(file)


