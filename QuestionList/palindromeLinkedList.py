# O(n) space
class Solution:
    def isPalindromeArray(self, values):
        left = 0
        right = len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return self.isPalindromeArray(values)

# O(1) Space
class Solution:
    def getMiddleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseLinkedList(self, head):
        current = head
        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middleNodeReversed = self.reverseLinkedList(self.getMiddleNode(head))
        currentA = head
        currentB = middleNodeReversed
        while currentB:
            if currentA.val != currentB.val:
                return False
            currentA = currentA.next
            currentB = currentB.next
        return True