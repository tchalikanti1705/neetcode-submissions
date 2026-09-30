class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
    
    def length(self) -> int:
        res = 0
        curr = self.head

        while curr:
            curr = curr.nxt
            res += 1
        
        return res
        

    def enQueue(self, value: int) -> bool:
        if self.length() >= self.k:
            return False
        
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return True
        curr = self.head

        while curr and curr.nxt:
            curr = curr.nxt
        
        curr.nxt = new_node
        self.tail = new_node
        return True

        
        

    def deQueue(self) -> bool:
        if self.length() <= 0:
            return False
        
        if self.length() == 1:
            self.head = self.head.nxt
            self.tail = self.tail.nxt

            return True
        
        self.head = self.head.nxt
        return True

        

    def Front(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.length() == 0
        

    def isFull(self) -> bool:
        return self.length() == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()