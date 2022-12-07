# Given an array, cyclically rotate the array clockwise by one. 

# Examples:  

# Input: arr[] = {1, 2, 3, 4, 5}

# Output: arr[] = {5, 1, 2, 3, 4}

def rotate(arr,n):
    x=arr[n-1]
    for i in range (n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x
arr={1,2,3,4,5}
n=len(arr)
rotate(arr,n)
print(arr)

