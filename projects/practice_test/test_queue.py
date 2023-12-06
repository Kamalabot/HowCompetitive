# implementing Nodes and Queue to practice TDD and Mocking
from typing import List, Dict, Any

class Nodes:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self, node: Nodes) -> None:
        self.head = node
        self.size = 1

    def enqueue(self, value: Any):
        # create node
        add_node = Nodes(value)
        # point the next of head to add_node
        self.head.next = add_node
        # increase size by 1
        self.size += 1

    def dequeue(self):
        # assign head to current node
        curr = self.head
        # assign next of head as head
        self.head = self.head.next
        # decrement size by 1
        self.size -= 1
        # return curr
        return curr.value

    def contains(self, value: Any):
        # assign head to observer
        observer = self.head
        # loop over the queue
        while observer is not None:
            # check if observer has the searched value
            if observer.value == value:
                return True
            # make the next node as observer
            observer = observer.next
        # after loop, return False
        return False

