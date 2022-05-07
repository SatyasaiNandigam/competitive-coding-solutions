sN = 100
isprime = [True]*N
lp,hp = [False]*N ,[False]*N

isprime[0]= isprime[1]=False
for i in range(2,N):
    if isprime[i]==True:
        lp[i]=hp[i]=i
        for j in range(2*i,N,i):
            isprime[j] = False
            hp[j] = i
            if lp[j]==0:
                lp[j] =i

for i in range(1,20):
    print(lp[i],hp[i],isprime[i],i)
