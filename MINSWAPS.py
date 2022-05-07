arr = input().split()
i,j = 0,len(arr)-1
count =0
while(i<j):
    if arr[i]=='B':
        if arr[i] !=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            count +=1
    else:
        i+=1
    
    if arr[j]=='A':
        if arr[i] !=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            count +=1
    else:
        j-=1

        

if count==0:
    print(-1)
else:
    print(count)