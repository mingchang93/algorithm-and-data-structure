'''
Quick sort

https://www.geeksforgeeks.org/quick-sort/

It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways:
    1. Always pick first element as pivot.
    2. Always pick last element as pivot (implemented below)
    3. Pick a random element as pivot.
    4. Pick median as pivot.

Worst runtime: if pivot is always chosen as the smallest or largest element in the given array, O(n^2)
Best runtime: always choose median as pivot, O(nlog(n))
'''

def partition(arr, low, high):
    i = j = low
    pivot = arr[high]

    while j < high:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

array = [ 10, 7, 8, 9, 1, 5 ]
quickSort(array, 0, len(array) - 1)
 
print(f'Sorted array: {array}')
