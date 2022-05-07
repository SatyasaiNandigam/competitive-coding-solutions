s = int(input())
l = []
for i in range(s):
    l.append(input().split(','))
for i in l:
    i[1] = int(i[1])
length = len(l)

arr = input().split(',')

for i in range(length):
    k = l[i]
    le = abs(k[1])
    if len(arr[i])<k[1]:
        r = le-len(arr[i])
        t = r%2
        s = int(r/2)+t
        arr[i] = arr[i]*(s+1)

    if k[1]>0:
        k[0] = k[0][le:]
        arr[i] = arr[i][:le] + k[0]
    
    if k[1]<0:
        lengt = len(k[0])
        sliced =  lengt-le
        k[0] = k[0][:sliced]
        arr[i] = k[0] + arr[i][-le:]


middle = []
for i in range(length):
    middle.append(len(arr[i]))
middle = sorted(middle,reverse=True)
result = []
for i in middle:
    if i not in result:
        result.append(i)
d = {}
for i in range(length):
    element = arr[i]
    if len(element) in d:
        d[len(element)].append(element)
        d[len(element)] = sorted(d[len(element)])
    else:
        d[len(element)] = [element]

output = []
for i in result:
    if len(d[i])>1:
        for j in d[i]:
            if j not in output:
                output.append(j)
    else:
        if d[i][0] not in output:
            output.append(d[i][0])

for i in range(len(output)):
    j = output[i]
    if i== len(output)-1:
        print(j,end='')
    else:
        print(j,end=',')



        
        


