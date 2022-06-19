class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, new_data):
        new_node = Node(data=new_data)

        new_node.prev = None
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if not prev_node:
            print('Previous node is None.')
            return
        
        new_node = Node(data=new_data)

        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = None

        if not self.head:
            new_node.prev = None
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def insertBefore(self, next_node, new_data):
        if not next_node:
            print('Next node is None')
            return

        new_node = Node(data=new_data)

        new_node.next = next_node
        new_node.prev = next_node.prev
        next_node.prev = new_node
        if new_node.prev:
            new_node.prev.next = new_node
        

    def printlist(self):
        last = self.head
        while last:
            print(last.data)
            last = last.next

DLL = DoublyLinkedList()
DLL.push(1)
DLL.append(3)
DLL.insertBefore(DLL.head.next, 2)
DLL.insertAfter(DLL.head.next.next, 4)
DLL.insertAfter(DLL.head.next.next, 'a')
DLL.printlist()
