n = int(input())
res=[]

def generate(res,s,open,close,number):
    if len(s)==2*number:
        res.append(s)
    
    if open< number:
        generate(res,s+'(',open+1,close,number)

    if close<open:
        generate(res,s+')',open,close+1,number)

generate(res,"",0,0,n)
print(res)