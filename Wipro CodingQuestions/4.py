'''
Print all the permutations of a given string.

Input:
T : number of test cases
T : number of strings

Output:
Permutated list of possible strings for each test case.

Sample Input:
3
ABC
MNZ
ZXC

Sample Output:

ABC ACB BAC BCA CAB CBA
...
...

'''

from itertools import permutations
t = int(input("Enter number of test case: "))
for i in range(t):
    stringinput = input()
    ans = list(' '.join(z) for z in permutations(stringinput))
    print(*ans)

# name = "satya"
# new_word = ""
# new_word = new_word.join(name[len(name)-1-i] for i in range(len(name)))
# print(new_word)