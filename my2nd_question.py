n= 5
m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
arr = list(map(int,input().split(',')))
for i in range(n):
    for j in range(n):
        if m[i][j] in arr:
            m[i][j] = 'X'
        else:
            m[i][j] = 'O'

def column_check(j):
    o=0
    x=0
    for i in range(n):
        if m[i][j]=='X':
            x+=1
        else:
            o+=1
    if x==5:
        return 1
    elif o==5:
        return 2
    else:
        return 0
    
def row_check(i):
    x = 0
    o=0
    for j in range(n):
        if m[i][j] == 'X':
            x+=1
        else:
            o+=1
    if x==5:
        return 1
    elif o==5:
        return 2
    else:
        return 0

def diagonal_check():
    x=0
    o=0
    for i in range(n):
        if m[i][i] == 'X':
            x+=1
        else:
            o+=1
    if x==5:
        return 1
    elif o==5:
        return 2
    else:
        return 0

def other_diagonal():
    x=0
    o=0
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                if m[i][j]=='X':
                    x+=1
                else:
                    o+=1
    if x==5:
        return 1
    elif o==5:
        return 2
    else:
        return 0

count = 0
for i in range(n):
    if row_check(i) in [1,2]:
        print(row_check(i))
        count = 1
        break
    elif column_check(i) in [1,2]:
        count = 1
        print(column_check(i))
        break

if count !=1:
    s = diagonal_check()
    if s in [1,2]:
        count = 2
        print(s)


if count ==0:
    r = other_diagonal()
    if r in [0,1,2]:
        print(r)
for i in range(n):
    print(m[i])


    



