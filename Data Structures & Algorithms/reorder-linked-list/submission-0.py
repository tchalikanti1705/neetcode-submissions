# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        pres = slow.next 
        slow.next = None 
        prev = None

        while pres:
            nxt_node = pres.next
            pres.next = prev
            prev = pres
            pres = nxt_node
        
        first = head
        second = prev 

        while second:
            first_next = first.next 
            second_next = second.next 

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next 
        
        