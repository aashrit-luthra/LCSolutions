# O(n) space and O(n) time
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seenNodes = set()
        current = head
        while current:
            if current in seenNodes:
                return True
            seenNodes.add(current)
            current = current.next
        return False

# Fast and Slow Pointer
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False