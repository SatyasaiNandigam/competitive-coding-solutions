arr = list(map(int,input().split()))
n = len(arr)
output =[]
i=0
k=1
while(i<n):
    if i==0:
        output.append(k)
    elif arr[i] >arr[i-1]:
        k+=1
        output.append(k)
    elif arr[i] == arr[i-1]:
        k=1
        output.append(k)
    else:
        k=1
        output.append(k)

    i+= 1

print(output)

    

    
    