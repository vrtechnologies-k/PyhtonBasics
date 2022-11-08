# Upper and Lower case characters count in python
s = "Welcome To AutomatioN"

l, u = 0, 0

for i in s:

    if (i >= 'a' and i <= 'z'):
        l = l + 1

    elif (i >= 'A' and i <= 'Z'):
        u = u + 1

print("\nLower case characters are:", l)
print("Upper case characters are:", u)