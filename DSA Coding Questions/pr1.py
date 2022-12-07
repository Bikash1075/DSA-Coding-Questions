# Write a Python Program to print half pyramid using alphabets. 
# The pattern should be as shown below:

# A

# B B

# C C C

# D D D D

# E E E E E

s='ABCDE'
for i in range(len(s)):
    for j in range(1,i+2):
        print(s[i],end=' ')
    print()
    print()