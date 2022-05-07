amount = int(input())
no_faces = int(input())
coins = [x for x in range(1,no_faces+1)]

dp = [0]* (amount +1)
dp[0] =1

for i in range(len(coins)-1,-1,-1):
    nextDP = [0] * (amount+1)
    nextDP[0] =1

    for a in range(1,amount+1):
        nextDP[a] = dp[a]
        if a-coins[i] >=0:
            nextDP[a] += nextDP[a-coins[i]]
    dp = nextDP
print(dp[amount])



# def subsetsUtil(A, subset, index,amount):
#     print(*subset)
#     for i in range(index, len(A)):
         
#         # include the A[i] in subset.
#         if amount -A[i]:
#             subset.append(A[i])
         
#         # move onto the next element.
#             subsetsUtil(A, subset, i + 1,amount-A[i])
         
#         # exclude the A[i] from subset and
#         # triggers backtracking.
#         subset.pop(-1)
#     return
 
# # below function returns the subsets of vector A.
# def subsets(A):
#     global res
#     subset = []
     
#     # keeps track of current element in vector A
#     index = 0
#     subsetsUtil(A, subset, index,amount)
     
# # Driver Code
 
# # find the subsets of below vector.
# amount = 5
# array = [1, 2]
 
# # res will store all subsets.
# # O(2 ^ (number of elements inside array))
# # because at every step we have two choices
# # either include or ignore.
# subsets(array)
 
