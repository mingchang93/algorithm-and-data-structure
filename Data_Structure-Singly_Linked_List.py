#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:40:18 2021

@author: liumingchang
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        
class LinkedList:
    def __init__(self):
        self.headval = None
        
    def printlist(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if not self.headval:
            self.headval = NewNode

        cur = self.headval
        while cur.nextval:
            cur = cur.nextval
        cur.nextval = NewNode

    def InBetween(self, middle_node, newdata):
        if not middle_node:
            pass

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, remove_data):
        HeadNode = self.headval

        if HeadNode:
            if HeadNode.dataval == remove_data:
                self.headval = HeadNode.nextval
                HeadNode = None
                return

        while HeadNode:
            if HeadNode.dataval == remove_data:
                break
            prev = HeadNode
            HeadNode = HeadNode.nextval

        if not HeadNode:
            return

        prev.nextval = HeadNode.nextval
        HeadNode = None

n1 = Node()
n1.dataval = 1

n2 = Node()
n2.dataval = 2

n3 = Node()
n3.dataval = 3

linked_list = LinkedList()
linked_list.headval = n1

n1.nextval = n2
n2.nextval = n3

linked_list.AtBeginning(0)
linked_list.AtEnd(4)
linked_list.InBetween(n1.nextval, 'a')
linked_list.printlist()

linked_list.RemoveNode('a')
linked_list.printlist()
