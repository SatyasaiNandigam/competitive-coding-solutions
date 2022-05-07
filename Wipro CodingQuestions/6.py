'''
Q) Print the Pythogorean triplet for the given numbers

Input:
    T: Number of test cases
    Two numbers a and b

Output:
    a b c (which form a Pythogorean triplet)

Sample Input: 
    3
    5 12
    14 16
    8 6

Sample Output: 
    5 12 13
    14 16 21
    8 6 10
'''
# import math as m
# test_cases=int(input("Enter no of test cases: "))
# cases =[]
# for i in range(test_cases):
#     numbers= map(int,input("Enter numbers for 1st case: "))
#     cases.append(numbers)
# for case in cases:
#     for i in range(len(case)):
        


import math as m
cases = []
for i in range(int(input("Enter number of test cases : "))):
    a,b= map(int, input(f"Enter 2 numbers for case {i+1}: ").split(" "))
    l = [a,b,int(m.sqrt(a**2+ b**2))]
    cases.append(l)
for i in range(len(cases)):
    print(*cases[i])