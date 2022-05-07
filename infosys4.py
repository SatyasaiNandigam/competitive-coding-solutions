
r = 3
m = [[1,2,-2,0],[5,-3,2,7],[0,1,0,1]]
c= len(m[1])
temp =[]
result = []

def counterclock(r,c,m):
    k,l = 0,0
    count = 0
    total = r*c

    while(k<r and l<c):
        if count == total:
            break

        for i in range(k,r):
            print(m[i][l])
        l+=1

        if count == total:
            break

        for i in range(l,c):
            print(m[r-1][i])
            count +=1
        
        r-=1
        
        if count == total:
            break

        if k<r:
            for i in range(r-1,k-1,-1):
                print(m[i][c-1])
                count +=1
            c-=1
        if count == total:
            break

        if (l<c):
            for i in range(c-1,l-1,-1):
                print(m[k][i])
                count +=1
            k+=1
    
counterclock(r,c,m)







