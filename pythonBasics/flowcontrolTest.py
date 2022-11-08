
a=10
b=20

if a == 10:
    print("condition satisfied")

if a == 30:
    print("condition not satisfied")
else:
    print("condition satisfied")

#if elif else

c = 100

if c<50:
    print("low value")
elif c<70:
    print("medium value")
elif c<90:
    print("nearest value")
else:
    print("exact value")

# for loop

seq_characters = "welcome to automation"

for characters in seq_characters:
    print(characters)

for i in range(len(seq_characters)):
    print(i)

for i in range(3):
    print(i)

for i in range(0,3):
    print(i)


while a <= 10:
    print("while loop satisfied")
    break;