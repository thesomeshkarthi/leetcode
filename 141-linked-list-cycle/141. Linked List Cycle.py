# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
            
        curr1 = head
        curr2 = head.next

        while curr1 and curr2 and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
            if curr2:
                curr2 = curr2.next
        
        return curr1 == curr2
        