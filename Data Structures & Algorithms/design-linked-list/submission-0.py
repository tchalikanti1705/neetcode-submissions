class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)

        # Find the node immediately before the insertion point
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Deleting the head
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            # List became empty
            if self.size == 0:
                self.tail = None

            return

        # Find node immediately before the node to delete
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        # Node being deleted
        node_to_delete = curr.next

        curr.next = node_to_delete.next

        # Deleting the tail
        if node_to_delete is self.tail:
            self.tail = curr

        self.size -= 1
