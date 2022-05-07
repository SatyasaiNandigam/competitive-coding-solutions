n = int(input())
black = []
def gcd(a,b,memo={}):
    if (b==0): return a
    
    if (a,b) in memo:
        return memo[(a,b)]
    else:
        memo[(a,b)] = gcd(b,a%b)
    return memo[(a,b)]


for _ in range(n):
    a,b = map(int,input().split())
    lc = (a*b)//gcd(a,b)
    black.append(lc)

gc = 0
for i in range(n):
    gc = gcd(gc,black[i])
print(gc)4