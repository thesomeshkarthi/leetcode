# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #Find Middle Using Tortoise and Hare pointer Technique
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHead = slow.next
        slow.next = None

        #Reverse secondList
        prev = None 
        while secondHead != None:
            tmp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = tmp
        
        #Splice both lists together
        secondHead = prev 
        firstHead = head

        while secondHead:
            firstTmp = firstHead.next
            secondTmp = secondHead.next
            firstHead.next = secondHead
            secondHead.next = firstTmp
            firstHead = firstTmp
            secondHead = secondTmp
    
        


         
