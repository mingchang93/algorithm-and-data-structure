# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
NeetCode's solution
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

'''
Easy solution, don't need to handle the addition operation
Just iterate through both lists, store the integers and add them
Then convert the sum back to a singly-linked list
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        s = str(num1 + num2)
        s = s[::-1]
        dummy = ListNode('NULL')
        head = ListNode(s[0])
        dummy.next = head
        for n in s[1:]:
            head.next = ListNode(n)
            head = head.next
        return dummy.next

    def getNum(self, l):
        num = ''
        while l:
            num += str(l.val)
            l = l.next
        return int(num[::-1])