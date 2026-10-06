class Node:
    def __init__(self, val, min_ele):
        self.val = val
        self.min_ele = min_ele
        self.next = None
        self.prev = None


class MinStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value: int) -> None:
        if self.size == 0:
            new_node = Node(value, value)
            self.head = new_node
            self.tail = new_node
        else:
            min_ele = min(value, self.tail.min_ele)
            new_node = Node(value, min_ele)

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def top(self) -> int:
        if self.size:
            return self.tail.val
        return None

    def getMin(self) -> int:
        if self.size:
            return self.tail.min_ele
        return None

#cleaner approch 

# class MinStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         if len(self.stack) == 0:
#             # First element
#             min_val = value
#         else:
#             # Compare current value with previous minimum
#             previous_min = self.stack[-1][1]
#             min_val = min(value, previous_min)

#         self.stack.append((value, min_val))

#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1][0]

#     def getMin(self):
#         return self.stack[-1][1]
