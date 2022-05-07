n = [8,4,5,3,2,6,9,1]
# 189 120 90 45 15 9 0 0


i=0
output = []
while(i<len(n)):
    min_count,max_count = 0,0
    k=i
    while(k<len(n)):
        if n[k] < n[i]:
            min_count += n[k]
        elif n[k] > n[i]:
            max_count += n[k]
        k+=1
    i+=1    
    val = min_count * max_count
    output.append(val)

print(output)