class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while head and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
