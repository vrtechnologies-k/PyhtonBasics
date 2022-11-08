# Read CSV file example
#Importing the csv module
import csv

# open file by passing the file path.
with open(r'D:\Projects\pythonBasics\TransactionDetails.csv') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')  # Delimeter is comma
    count_line = 0
    # Iterate the file object or each row of the file
    for row in csv_read:
        if count_line == 0:
            print(f'Column names are {", ".join(row)}')
            count_line += 1
        else:
            print(f'\t Row values :  {row}')
            count_line += 1
    print(f'Processed {count_line} lines.')  # This line will print number of line fro the file