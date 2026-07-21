# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to make it easier to build the result
        dummy = ListNode(0)
        current = dummy
        
        # While both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (one list will be empty)
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the next of dummy (the actual head)
        return dummy.next