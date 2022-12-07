# Write a Python Program to print full pyramid using '*' symbol. The pattern should be as shown below:

# *

# * * *

# * * * * *

# * * * * * * *

# * * * * * * * * *

n=5
for i in range(1,n+1):
    for j in range(1,2*i):
        print('*', end=' ')
    print()
    print()
# solution2
n=5
for i in range(0,n):
    print('* '*(2*i+1))
    print()