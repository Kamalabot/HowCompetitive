# Implementing queue with just array

queue = []

# Enqueue Operation: queue takes elements from the back, very much like list

queue.append(6)
queue.append(8)
queue.append(96)

# print(queue)

# Dequeue Operation: queue elements remove from front

# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
 
# print(queue)

# Reason for implementing queue is the time complexity of efficient queue has to be O(1) 


class QueueNode:

    def __init__(self, val):
        self.val = val
        self.next = None 


class Queue:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, val):

        newNode = QueueNode(val=val) # The node has to be initiated
        # The next node can be assigned to the newNode inside the memory
        if self.size == 0:
            # then front and back node are same
            self.front = newNode
            self.back = newNode
        else:
            # enqueue will be done from the back, so back & 
            # next node are same
            self.back.next = newNode # Even the assignment order matters  
            self.back = newNode

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        removeNode = self.front
        self.front = self.front.next
        self.size -= 1
        return removeNode

    def __str__(self):
        string = ""
        node_ref = self.front
        if self.size == 0:
            return "No Elements yet"
        while True:
            if node_ref == self.back:  # check if node is back node
                string += node_ref.val
                break
            else:
                string += node_ref.val + "->"

            node_ref = node_ref.next  # here the raw node needs to be 
            # visualised, not front or back variables 

        return string

    def print(self):
        if self.size == 0:
            print("No Elements")
        string = ""
        curr = self.front
        while curr.next is not None:
            string += str(curr.val) + "->"
            curr = curr.next
        string += str(curr.val)

        print(string)

que1 = Queue()
que1.enqueue('a')
que1.enqueue('b')
que1.enqueue('c')
que1.enqueue('d')
que1.enqueue('e')

print(que1.size)

print(que1)

que1.dequeue()
que1.dequeue()

que1.enqueue('ei')

print(que1)

que2 = Queue()

print(que2)