# Take a number as input from the user. Print the number in reversed order. 
# For example, for input 567, output should be: 765

n = 567
rev=0
for i in range(len(str(n))):
    rem = n%10
    rev=rev*10+rem
    n=n//10
print(rev)

# 2nd solution
n=567
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)