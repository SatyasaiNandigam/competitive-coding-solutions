# 4
# 0 0 0 0
# 0 1 0 0 
# 0 0 0 1
# 1 0 0 0

grid = []
rows = int(input())
for _ in range(rows):
    grid.append(list(map(int,input().split())))

dp = [[0]*rows]*rows

n = rows-1

for i in range(n,-1,-1):
    for j in range(n,-1,-1):
        if (i==j and i==n):
            dp[i][j] = 1
        else:
            option1 = 0 if i==n else dp[i+1][j]
            option2 = 0 if j==n <rows else dp[i][j+1]
            dp[i][j] = option1+option2
            if grid[i][j]==1:
                dp[i][j]=0
if grid[n][n]==1:
    print(0)
else:
    print(dp[0][0])


