'''
Wipro Coding: ||
-----------------------------
Problem 2:

First of all you need to take input a whole scentance in the string,
the you need to enter the target 'word'. As an input you need to find
the number of times that particular target word is repeated in the scentence.

Sample Input:
Welcome world to the new world
world

Sample Output:
2

'''


def wordcount(targetword, sentence):
    words = sentence.split(sep=" ")
    return words.count(targetword)

print(wordcount("world","Welcome world to the new world"))
