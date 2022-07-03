# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        return self.merge_sort(head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    def find_mid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, head1, head2):
        dummy = ListNode()
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

s = Solution()
print_list(s.sortList(head))
