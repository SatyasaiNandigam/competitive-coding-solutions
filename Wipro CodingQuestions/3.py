'''
Print the sorted and non-redundant occurences of elements from the given input

Sample Input:
1,3,5,6,3,2,3,5,5,4,3,2

Sample Output:
1 2 3 4 5 6
'''

arr = list(map(int,input("Enter numbers: ").split(',')))
arr= set(arr)
print(*arr)

    