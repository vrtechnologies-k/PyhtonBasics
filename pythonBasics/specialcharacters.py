
string = "venkat123*&%^#&)sdfhhhfdsjhe588"
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

print("\nTotal Number of Alphabets in this String:  ", alphabets)
print("Total Number of Digits in this String:  ", digits)
print("Total Number of Special Characters in this String:  ", special)