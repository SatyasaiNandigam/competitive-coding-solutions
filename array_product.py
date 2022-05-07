arr = [1,2,3,4]
#      1,1,2,6
#       ,3,4,1

result = [1]
for i in range(1,len(arr)):
    result.append(result[i-1]*arr[i-1])

temp =1
for i in range(len(arr)-2,-1,-1):
    result[i] *= arr[i+1]*temp
    temp *= arr[i+1]


print(result)

