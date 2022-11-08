number = 12345

rev_num = 0

while number > 0:
    reminder = number % 10
    rev_num = rev_num * 10 + reminder
    number = number//10 #(// - floor (remove float) and / - float)

print(rev_num)