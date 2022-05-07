numbers = list(map(int,input().split(',')))
max_number = max(numbers)
a,b=1,1
ab=[]
fa_numbers = [1,1]
c=0
while(c<=max_number):
    c = a+b
    fa_numbers.append(c)
    a=b
    b=c

for i in fa_numbers:
    if i in numbers:
        ab.append(i)

if len(ab)>2:
    print(len(ab),ab)
else:
    print(-1)

# print(len(ab),*ab)