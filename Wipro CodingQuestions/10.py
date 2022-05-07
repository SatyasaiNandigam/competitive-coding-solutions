name = "SaTYa"
upper = 0
lower = 0
for letter in name:
    if letter.isupper():
        upper +=1
    else:
        lower +=1

if lower> upper:
    print(name.upper())
else:
    print(name.lower())
