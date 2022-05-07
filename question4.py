n,m = map(int,input().split())
arr = []
c=0
for i in range(n):
    a = int(input())
    arr.append(a)


count = [0]*(m+1)

for i in range(n):
    count[arr[i]] +=1
    val = count[arr[i]]
    if val%3 ==0 and val!=0:
        c += int(val/3)
print(count)
i,j,k=0,1,2

while(k<m+1):
    if count[i]!=0  and count[j]!=0  and count[k]!=0:
        
        print(i,j,k)
        c += min(count[i],count[j],count[k])

    i+=1
    j+=1
    k+=1

print(c)