import string
letters = list(string.ascii_uppercase)
for i in list(string.ascii_lowercase):
    letters.append(i)

def binary_conversion(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1]
    while len(x)<8:
        x+='0'
    bnr = x[::-1]
    return bnr

string_input = 'ABC123+'
sequence = ''
for i in string_input:
    order = ord(i)
    bits= binary_conversion(order)
    sequence += ''.join(bits)
if len(sequence)%6!=0:
    sequence +=''.join('0'*(6-len(sequence)%6))

results =[]
for i in range(0,len(sequence),6):
    results.append(sequence[i:i+6])
    
output =''
for i in results:
    output +=''.join(letters[int(i,2)])

print(output)