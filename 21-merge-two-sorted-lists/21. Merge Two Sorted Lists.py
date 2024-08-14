# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode()
        mergedList = node

        while list1 and list2:
            if list1.val > list2.val:
                #Append node 2 to new list and iterate node 2
                node.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                #Append node 1 to new list and iterate node 1
                node.next = list1
                list1 = list1.next
            node = node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return mergedList.next                        
        



        