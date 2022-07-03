class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        has_cycle = False
        while head and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None
        else:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
