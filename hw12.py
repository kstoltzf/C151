#!/usr/bin/python

from random import *

def makeArray(n):
    a = []
    
    for i in range (1,n+1):
        a.append(i)

    return a

def shuffleArray(a):
    Len = len(a)
    
    for i in range (0,Len-1):
        x = randint(i,Len-1)
        
        if i != x:
            temp = a[i]
            a[i] = a[x]
            a[x] = temp
   
    return a
            
if __name__=='__main__':
    print "Enter the size of the array"
    size = input()

    result = makeArray(size)
    print result

    newResult = shuffleArray(result)
    print newResult
    print "The function shuffleArray shuffles the array into a random order as shown above"

#[kstoltzf@cs136 week13]$ hw12.py
#Enter the size of the array
#7
#[1, 2, 3, 4, 5, 6, 7]
#[5, 3, 4, 1, 6, 2, 7]
#The function shuffleArray shuffles the array into a random order as shown above
