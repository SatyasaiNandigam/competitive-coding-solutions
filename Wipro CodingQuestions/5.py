'''
Print largest word from the sentence.

Input: 
    Sentence(string)

Output:     
    Largest word from the string.
'''




# output = max(input("Enter your sentence: ").split(sep=" "))
# print(output)

#using function

def largestword(sentence):
    words = sentence.split(sep=" ")
    stringlength = -1
    for word in words:
        if len(word) >stringlength:
            stringlength = len(word)
            output = word
    return output
print(largestword("Welcome world to the new world"))
