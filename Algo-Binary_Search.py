'''Binary Search

https://www.geeksforgeeks.org/binary-search/

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
'''


def binarySearchRecursive(arr, x):
    '''
    Recursive version

    Compare x with the middle element.
    If x matches with the middle element, we return the mid index.
    Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recurse on the right half.
    Else (x is smaller) recurse on the left half.
    '''
    def search(arr, l, r, x):
        # base case: if the array only has one element, i.e., l = r = 0, check if arr[l] == x, return l if true -1 otherwise
        # if not base case, go in recursive loop
        if r >= 1: 
            midpoint = 1 + (r - l) // 2
            if x == arr[midpoint]:
                return midpoint
            elif x < arr[midpoint]:
                return search(arr, l, midpoint-1, x)
            else:
                return search(arr, midpoint+1, r, x)
        return -1
    
    return search(arr, 0, len(arr)-1, x)

arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearchRecursive(arr, x)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")



def binarySearchIterative(arr, x):
    def search(arr, l, r, x):
        while l <= r:
            midpoint = 1 + (r - l) // 2
            if x == arr[midpoint]:
                return midpoint
            elif x < arr[midpoint]:
                r = midpoint - 1
            else:
                l = midpoint + 1            
        return -1
    
    return search(arr, 0, len(arr)-1, x)

arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearchIterative(arr, x)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
