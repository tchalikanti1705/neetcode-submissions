"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        tail = dummy
        curr = head

        while curr:
            tail.next = Node(curr.val)
            tail = tail.next 
            curr = curr.next 
        
        curr = head
        copied = dummy.next 

        hmap = {}

        while curr:
            hmap[curr] = copied
            curr = curr.next 
            copied = copied.next 
        
        curr = head
        copied = dummy.next 

        while curr:
            copied.random = hmap.get(curr.random)
            curr = curr.next 
            copied = copied.next 
        
        return dummy.next 
        