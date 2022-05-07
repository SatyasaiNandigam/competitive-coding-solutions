
n = int(input())
dp = [0]*(n+1)

def steps(number,memo={}):
    if number ==0 or number ==1:
        return 1
    if number in memo:
        return memo[number]
    else:
        dp[number] = steps(number-1,memo)+steps(number-2,memo)
        memo[number] = dp[number]
        return memo[number]

print(steps(n))
 