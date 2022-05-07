'''
 1
 2 3
 4 5 6
 7 8 9 10

'''

'''
* * * *
* * * * 
* * * * 
* * * * 

'''
j = 1
for i in range(1, 5):
    for i in range(i):
        print(j, end=" ")
        j += 1
    print()
    
print()

for i in range(1, 4):
    print("*" * 4)
