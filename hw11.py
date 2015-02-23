#!/usr/bin/python

def maxArray(a):
    max = a[0]

    for element in a:
        if element > max:
            max = element

    return max

def reverseArray(a):
    n = len(a) - 1
    
    for i in range(0,n/2):
        temp = a[i]
        a[i] = a[n-i]
        a[n-i] = temp

if __name__=='__main__':
    Numbers = [3,1,6,2,4,9,0]

    print maxArray(Numbers)
    reverseArray(Numbers)
    print Numbers

#[kstoltzf@cs136 week12]$ hw11.py
#9
#[0, 9, 4, 2, 6, 1, 3]

