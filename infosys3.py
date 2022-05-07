
import string
rev_d ={}
d={}
st = 'abcegklm'
for i,letter in enumerate(list(string.ascii_lowercase)):
    d[i] = letter
    rev_d[letter] = i

def convert(st,visited={}):
    for i in range(len(st)-1):
        if rev_d[st[i+1]] - rev_d[st[i]]==1:
            if [i,i+1] not in [x for x in visited.values()]:
                st = st.replace(st[i:i+2],d[rev_d[st[i+1]]+1])
                visited[d[rev_d[st[i+1]]]] = [i,i+1]
                print(visited)
                return convert(st,visited)
    return st 

answer = []
while(True):
    if convert(st) in answer: 
        break
    else:
        answer.append(convert(st))