import math
n = [7,3,1,1,4,5,4,9]
dic = {}
a = []
for i in range(len(n)):
    if n[i] not in dic:
        dic[n[i]] = [i]
    else:
        dic[n[i]].append(i)


for key,value in dic.items():
    dic[key] = dic[key][:math.ceil(len(dic[key])/key)]


n = sorted(dic)
for i in range(len(n)):
    n[i] = [n[i]]* len(dic[n[i]])
for i in n:
    for j in i:
        a.append(j)

sum = 0
count = 0
for i in range(len(a)):
    sum += a[i]
    count +=1
    if sum >= len(a):
        break
print(count)
