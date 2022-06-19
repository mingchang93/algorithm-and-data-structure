# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Two-pointer approach: a slow and a fast pointer move together
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        
        dummy = ListNode()
        dummy.next = head
        pre, cur, next = dummy, slow, slow.next
        while fast:
            pre, cur, next = cur, next, next.next
            fast = fast.next
        pre.next = next

        return dummy.next


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

# sol = Solution()
# head = sol.removeNthFromEnd(head, 2)
# while head:
#     print(head.val)
#     head = head.next