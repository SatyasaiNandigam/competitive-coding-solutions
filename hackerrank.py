length= int(input())
M = []
answer = []
s=1
def number_sum(value):
    return sum([int(x) for x in value])
for _ in range(length):
    M.append(input().split())
for i in range(length-1):
    for j in range(length-1):
        if M[i][j]!='0' and M[i+1][j]!='0' and M[i][j+1]!='0' and M[i+1][j+1]!='0':
            if int(M[i][j])%number_sum(M[i][j])==0 and int(M[i+1][j])%number_sum(M[i+1][j])==0:
                s +=1
            if int(M[i+1][j+1])%number_sum(M[i+1][j+1])==0 and int(M[i][j+1])%number_sum(M[i][j+1])==0:
                s+=1
            if s==3:
                answer.append([[M[i][j],M[i][j+1]],[M[i+1][j],M[i+1][j+1]]])
            s=1
if len(answer)!=0:
    for i in answer:
        for j in i:
            print(*j)
else:
    print(-1)