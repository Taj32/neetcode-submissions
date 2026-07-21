# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempList = []

        prev = None
        current = head

        while current:
            #save the next node before we cahnge the pointer
            next_node = current.next

            #reverse the pointer
            current.next = prev

            #Move prev and current one step forward
            prev = current
            current = next_node

        return prev

        