class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hmap = [Node(0, 0) for _ in range(self.size)]
    
    def hashing(self, key):
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        curr = self.hmap[self.hashing(key)]

        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt.val = value
                return
            curr = curr.nxt 
        curr.nxt = Node(key, value)
        

    def get(self, key: int) -> int:
        curr = self.hmap[self.hashing(key)]
        while curr.nxt:
            if curr.nxt.key == key:
                return curr.nxt.val
            curr = curr.nxt 
        return -1

        

    def remove(self, key: int) -> None:
        curr = self.hmap[self.hashing(key)]
        while curr and curr.nxt:
            if curr.nxt.key == key:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)