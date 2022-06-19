'''
Heap

https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

Operations on heap :
    - heapify(iterable): This function is used to convert the iterable into a heap data structure. i.e. in heap order.
    - heappush(heap, ele): This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
    - heappop(heap): This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
    - heappushpop(heap, ele): This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.
    - heapreplace(heap, ele): This function also inserts and pops element in one statement, but it is different from above function. In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().
    - nlargest(k, iterable, key = fun): This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.
    - nsmallest(k, iterable, key = fun): This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.
'''

import heapq
  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print("The created heap is : ",end="")
print(list(li))
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)
  
# printing modified heap
print("The modified heap after push is : ",end="")
print(list(li))
  
# using heappop() to pop smallest element
print("The popped and smallest element is : ",end="")
print(heapq.heappop(li))


# initializing list 1
li1 = [5, 7, 9, 4, 3]
  
# initializing list 2
li2 = [5, 7, 9, 4, 3]
  
# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)
  
# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ",end="")
print(heapq.heappushpop(li1, 2))
  
# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ",end="")
print(heapq.heapreplace(li2, 2))


# initializing list 
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
  
# using heapify() to convert list into heap
heapq.heapify(li1)
  
# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))
  
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))

