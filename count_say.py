n = input()
m = int(input())
def count_say(n):
    count = 1
    flag = 0
    comp = n[0]
    output = ''
    for i in range(1,len(n)):
        if n[i] == comp:
            flag = 0
            count +=1
        else:
            output += ''.join(str(count)+n[i-1])
            flag = 1
            count = 1
            comp = n[i]
    last_element = len(n)-1
        
    if flag==0:
        output += ''.join(str(count)+n[last_element])
    else:
        output += ''.join(str(count)+n[last_element])
        
    return output

for i in range(m):
    print(n)
    val = count_say(n)
    n = val