arr = [1,2,5,4,110]
N = len(arr)
output = [1]*N
for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            output[i] = output[j]+1

print("maximum" ,max(output))



