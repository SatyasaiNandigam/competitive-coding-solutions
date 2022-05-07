n,m = map(int,input().split())
cost = list(map(int,input().split()))
pages = list(map(int,input().split()))

weigths = []
d = {}
for i in range(n):
    val = pages[i]/cost[i]
    weigths.append(val)
    if val in d:
        d[val].append(i)
    else:
        d[val] = [i]

weigths = sorted(weigths,reverse=True)

# 4 10
# 4 8 5 3
# 5 12 8 1
ans =0
s= 0
for i in weigths:
    for j in range(len(d[i])):
        ele = d[i][j]
        val_cost = cost[ele]
        if (s+val_cost) <m:
            s = s+val_cost
            ans += pages[ele]

print(ans)