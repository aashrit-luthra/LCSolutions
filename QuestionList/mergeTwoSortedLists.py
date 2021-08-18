class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(-1)
        outputHead = output
        while l1 and l2:
            if l1.val < l2.val:
                outputHead.next = l1
                l1 = l1.next
            else:
                outputHead.next = l2
                l2 = l2.next
            outputHead = outputHead.next
        if l1:
            outputHead.next = l1
        elif l2:
            outputHead.next = l2
        return output.next