results = []
def generate(s,opening,closing):
    if opening==0 and closing ==0:
        results.append(s)
        return
    if(opening>0):
        s += ''.join('(')
        generate(s,opening-1,closing)
        s = s[:-1]
    if(closing >0):
        if (opening < closing):
            s += ''.join(')')
            generate(s,opening ,closing-1)
            s = s[:-1]

generate("",3,3)
for i in results:
    print(i)