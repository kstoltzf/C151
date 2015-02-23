#!/usr/bin/python
#Kyle Stoltzfus
#Homework 13

from random import *
from sys import *
from string import *

def generateNumbers(filename, size, limit):
    fout = open(filename, "w")

    fout.writelines("%d\n" %(size))

    strOut = ""

    for i in range(0, size-1):
        n = randint(0, limit)
        
        if strOut == "":
             strOut = "%d" %(n)
        
        else:
             strOut = "%s %d" %(strOut, n)

        if (i+1) % 20 == 0:
            fout.writelines("%s\n" %(strOut))
            strOut = ""

    fout.writelines("%s\n" %(strOut))
    fout.close()

def readFile(filename):
    fin = open(filename, "r")
    line = fin.readline()
    size = int(line)
    result = []

    while len(result) < size:
        line = fin.readline()
        line = split(line, "\n")[0]
        numbers = split(line, " ")

        for n in numbers:
            result.append(int(n))

    fin.close()
    return result

if __name__ == '__main__':
    if len(argv) != 4:
        print "Please call this script with the file name, the count of the numbers in the file, and the limit for the random numbers."

    else:
        filename = argv[1]
        size = int(argv[2])
        limit = int(argv[3])

        generateNumbers(filename, size, limit)
        print readFile(filename)

