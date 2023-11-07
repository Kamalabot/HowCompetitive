# Implementing to test queue know-how

class QueueNode:

    def __init__(self,val):
        self.val = val 
        self.next = None

# Queue must have methods to enqueue and dequeue the elements 


class Queue:

    def __init__(self) -> None:
        """Initialize the queue without any values, and size 0"""
        self.front = None
        self.back = None
        self.size = 0
 
    def enqueue(self, val: QueueNode):
        newNode = QueueNode(val)
        # If the queue is empty, then first element is going to be both front and back
        if self.size == 0:
            self.front = newNode 
            self.back = newNode 
        else:
            self.back = newNode
            self.back.next = newNode

        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return None
        remo = self.front
        self.front = self.front.next
        self.size -= 1
        return remo.val

    def print(self):
        # Output should start from front -> next back -> next back ...
        str = ""

        if self.size == 0:
            return str
        
        cur = self.front
        str += cur.val

        while cur.next is not None:
            cur = cur.next
            str += cur.val + " -> " 

        print(str)



trial = Queue()
trial.enqueue('a')
trial.enqueue('b')
trial.enqueue('c')

print(trial.size)

trial.print()