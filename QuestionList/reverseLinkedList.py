class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev