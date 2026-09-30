class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.cursor = self.homepage

        

    def visit(self, url: str) -> None:
        curr = self.cursor
        if curr.next:
            curr.next = None
        new_node = Node(url)
        curr.next = new_node
        new_node.prev = curr
        self.cursor = new_node
        
        

    def back(self, steps: int) -> str:

        while steps and self.cursor.prev:
            self.cursor = self.cursor.prev
            steps-=1
        return self.cursor.data
        

    def forward(self, steps: int) -> str:

        while steps and self.cursor.next:
            self.cursor = self.cursor.next
            steps-=1
        return self.cursor.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)