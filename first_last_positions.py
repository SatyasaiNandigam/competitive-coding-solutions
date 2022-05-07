arr = [2,4,5,5,5,5,5,7,9,9]
key = 5

def find_start(arr,target):
    if arr[0]==target:
        return 0
    left,right = 0,len(arr)-1
    while(left<=right):
        mid = (left+right)//2
        if arr[mid]== target and arr[mid-1]<target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

def find_end(arr,target):
    if arr[-1] == target:
        return len(arr)-1
    left,right = 0,len(arr)-1
    while(left<=right):
        mid = (left+right)//2
        if arr[mid]==target and arr[mid+1]>key:
            return mid
        elif arr[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return -1

def find_positions(arr,key):
    if arr[0]>key or arr[-1]<key or len(arr)==0:
        return [-1,-1]
    start = find_start(arr,key)
    end = find_end(arr,key)
    return [start,end]

print(find_positions(arr,5))

    


