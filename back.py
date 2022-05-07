num = list(map(int,input().split()))

def subsets(nums):
    res = []
    backtrack(res,[],nums,0)
    return res

def backtrack(res,temp,nums,start):
    if len(temp)>1:
        res.append(temp[:])
    for i in range(start,len(nums)):
        temp.append(nums[i])
        if len(temp)>1:
            if temp[-1]==2*temp[-2] or temp[-1] == 3*temp[-2] or temp[-1]==temp[-2]+1 or temp[-1]==temp[-2]-1 or temp[-1]== temp[-2]//2 or temp[-1]==temp[-2]//3:
                backtrack(res,temp,nums,i+1)
        else:
            backtrack(res,temp,nums,i+1)
        temp.pop()
    
answers= subsets(num)


def divisors_count(num):
    count = 0
    for i in range(1,num//2+1):
        if num%i==0:
            count +=1
    return count+1
se = {}
count =0
max =0
for subset in answers:
    for i in subset:
        if i not in se:
            se[i] = divisors_count(i)
            count += se[i]
        else:
            count += se[i]    
    if max<count:
        max = count
        ans = subset
    count = 0
print(max,ans)
    
    

        

        

