class Solution:
    def findCommonNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        return None
        
    def detectCycle(self, head: ListNode) -> ListNode:
        commonNode = self.findCommonNode(head)
        if not commonNode:
            return None
        current = head
        while current != commonNode:
            current = current.next
            commonNode = commonNode.next
        return current