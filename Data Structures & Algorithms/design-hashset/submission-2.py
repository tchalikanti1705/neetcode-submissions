class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.hashset = [Node(0) for _ in range(self.size)]
    
    def hashing(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        curr = self.hashset[self.hashing(key)]

        while curr.nxt:
            if curr.nxt.val == key:
                return
            curr = curr.nxt
        curr.nxt = Node(key)
        

    def remove(self, key: int) -> None:
        curr = self.hashset[self.hashing(key)]

        while curr and curr.nxt:
            if curr.nxt.val == key:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt
        

    def contains(self, key: int) -> bool:
        curr = self.hashset[self.hashing(key)]

        while curr.nxt:
            if curr.nxt.val == key:
                return True
            curr = curr.nxt 
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)