n = int(input())
dp = [0]*(n+1)

# dp[0] =0
for i in range(1,n+1):
    minimal_steps = 100000002
    temp = i
    while(temp>0):
        di = temp%10
        temp  = temp//10
        if di==0:
            continue
        minimal_steps = min(minimal_steps,1+dp[i-di])
    dp[i] = minimal_steps
    print(dp[i])

print(dp[n])


        
