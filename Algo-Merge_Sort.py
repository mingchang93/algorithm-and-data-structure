'''
Merge sort, time complexity O(nlog(n))

Implemented recursively: breaks the array into half, sort left half, sort right half, then merge.
Number of levels of recursions: log(n)
Amount of work done per level: n

https://www.geeksforgeeks.org/merge-sort/
'''

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        # the following is the merge step
        # when mergeSort is called on the left and right sub-array, they came back sorted
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [8, 4, 2, 7, 9, 10, 0, 1, 6, 3, 5]
print('Given array: \n', arr)
mergeSort(arr)
print('Sorted array: \n', arr)
