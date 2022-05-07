'''
Wipro Coding: ||
-----------------------------
Problem 1:

YOu are given a number and you have to extract the key by finding difference b/w the sum of the even and odd numbers of 
the input.

Sample INput:
24319587

Sample Output:
11

Logic: --
-----------
even --> 2+4+8 = 14
odd --> 3+1+9+5+7

odd - even is the output
'''
number = input("Enter a number: ")
even = 0
odd = 0
for i in number:
    if int(i)%2 == 0:
        even += int(i)
    else:
        odd += int(i)

output = even - odd

print(abs(output))


# Using Functions solution

# def difference(n):
#     Even,Odd = 0,0
#     for i in str(n):
#         if int(i)%2 == 0:
#             Even += int(i)
#         else:
#             Odd += int(i)
#     return abs(Even-Odd)

# print(difference(24319587))