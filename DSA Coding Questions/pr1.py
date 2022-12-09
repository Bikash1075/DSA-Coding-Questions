# Write a Python Program to print half pyramid using alphabets. 
# The pattern should be as shown below:

# A

# B B

# C C C

# D D D D

# E E E E E

def triangle(s,n):
    for i in range(n):
        for j in range(1,i+2):
            print(s[i],end=' ')
        print()
        print()
s='ABCDE'
n=len(s)
triangle(s,n)


def triangle(n):
    k=65
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(i+k),end=' ')
        print()
        print()
triangle(5)

def triangle(n):
    k=65
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(i+k),end=' ')
        print()
        print()
triangle(5)