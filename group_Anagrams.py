arr = ['eat','tea','tan','ate','nat','bat']
d = {}
for i in range(len(arr)):
    word = ''.join(sorted(arr[i]))
    if word in d:
        d[word].append(arr[i])
    else:
        d[word] = [arr[i]]
    
for i in d:
    print(d[i])

