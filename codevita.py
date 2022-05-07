n = int(input())
grid = []
for _ in range(n):
    s = input()
    grid.append(list(s))


def dfs(grid,r,c,coins=0):
    grid[r][c]='N'
    coins +=1
    lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
    for row,col in lst:
        if row>=0 and col >=0 and row<len(grid) and col<len(grid[row]) and grid[row][col]=='C':
            coins +=dfs(grid,row,col,coins=0)
    return coins
player1 = 0
player2 = 0
val = 0
cot = 0
past = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if cot%2==0:
            if grid[r][c]=='C':
                val = dfs(grid,r,c,coins=val)

            if val !=0:
                player1 += val
                cot +=1
            val = 0 
            
        else:
            if grid[r][c]=='C':
                val = dfs(grid,r,c,coins=val)

            if val !=0:
                player2 += val
                cot +=1
            val = 0
            

        
print(player1,player2)
