'''stack: last in first out (LIFO)

https://www.geeksforgeeks.org/stack-in-python/

operations:
- empty() – Returns whether the stack is empty – Time Complexity : O(1)
- size() – Returns the size of the stack – Time Complexity : O(1)
- top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
- push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
- pop() – Deletes the top most element of the stack – Time Complexity : O(1)
'''
print('------------using list------------')
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print(f'Initial stack: {stack}')
print('Start popping...')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(f'Stack after popping: {stack}')

print('------------using collections.deque------------')
from collections import deque
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(f'Initial stack: {stack}')
print('Start popping...')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(f'Stack after popping: {stack}')


print('------------using singly linked list------------')
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value) + ' -> '
            cur = cur.next
        return out[:-4]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('Peeking an empty stack')
        else:
            return self.head.next.value

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Poping from an empty stack')
        else:
            cur_first = self.head.next
            self.head.next = cur_first.next
            cur_first.next = None
            self.size -= 1
            return cur_first.value

    
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    print(f"Number of elements in stack: {stack.getSize()}")

    for _ in range(1, 6):
       remove = stack.pop()
       print(f"Pop: {remove}")
    print(f"Stack: {stack}")