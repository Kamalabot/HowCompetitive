# Script is used for practicing queue, stack, graph and linkedlist 
# implementation. The methods like, print, contains, 
# delete element and reverse list functions 

# implementing logging
import logging
# Use a create a logger 
logger = logging.getLogger(__name__)
# assign level to logger
logger.setLevel(logging.INFO)
# create a streamhandler 
handler = logging.StreamHandler()
# setLevel for handler
handler.setLevel(logging.INFO)
# create a formatter
newfmt = logging.Formatter(fmt='%(message)s - %(levelname)s - %(asctime)s',
                           datefmt='%d-%b %H:%M')
# attach formatter to handler
handler.setFormatter(newfmt)
# attach handler to logger
logger.addHandler(handler)
# start using the logger

# implementing Queue with Node objects


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


A = Node('a')
B = Node('b')
C = Node('c')
D = Node('d')

# print(A)

# implementing Queue Class


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, node):
        # if queue is empty
        if self.size == 0:
            # enqueueed node will be front & back
            self.front = node
            self.back = node
        # in other cases node is assigned to current back node's next
        self.back.next = node
        # also the back node will be the new node
        self.back = node
        # size of queue will be extended by 1
        self.size += 1
    
    def dequeue(self):
        # if queue is empty
        if self.size == 0:
            # return empty queue
            return 'empty queue'
        # in other cases assign front node to outnode
        outNode = self.front
        # check if outNode's next attribute has value
        if outNode.next is not None:
            # make the next node in the next attr as front node
            self.front = outNode.next
        # in other cases reduce the size of queue by 1
        self.size -= 1
        # return the outnode
        return str(outNode.value)

    def contains(self, search):
        # if queue is empty
        if self.size == 0:
            return False
        # In other cases, start from first node 
        curr = self.front
        # loop while next node of observed node is not None
        while curr.next is not None:
            # check if value is same as search node
            if curr.value == search:
                return True 
            # other cases assign the next node to current
            curr = curr.next
        # after checking all values, if not found return false
        return False

    def printQueue(self):
        # if queue is empty
        if self.size == 0:
            # print 'empty queue'
            print('empty queue')
        # create a variable to hold the value to be printed
        string = ""
        # assign the front node to curr
        curr = self.front
        # take the front node and add the value to string
        string += str(curr.value)
        # look for next nodes in queue until there is no nodes
        while curr.next is not None:
            # assign the next to current 
            curr = curr.next
            # add its value to string
            string += ' -> ' + str(curr.value)
        # print the string
        print(string)
    
    def __len__(self):
        "Access queue via its size attributes"
        return self.size


# queue = Queue()
# queue.enqueue(A)
# queue.enqueue(B)

# print(len(queue))

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.size)

# queue.enqueue(A)
# queue.enqueue(C)
# queue.enqueue(B)
# queue.enqueue(D)

# print(queue.contains('a'))  # True
# print(queue.contains('t'))  # False

# queue.printQueue()

# implementing Stack with the same Node class above

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        # if stack is empty
        if self.size == 0:
            # make the value as top node
            self.top = Node(value)
        # else take top node and assign to next of value 
        else:
            # create a new node
            newNode = Node(value)
            newNode.next = self.top
            # assign newNode as top
            self.top = newNode
        
        # increase the size by 1
        self.size += 1

    def pop(self):
        # if the stack is empty
        if self.size == 0:
            # just return
            return None
        # other cases, take the top node
        popnode = self.top
        # assign the top.next as top node
        self.top = self.top.next
        # reduce the stack size
        self.size -= 1
        # return top value
        return popnode.value
            
    def contains(self, search):
        logger.warning(f'Search is {search}')
        # if stack is empty
        if self.size == 0:
            return False
        # assign top node to curr
        curr = self.top
        # start looping while curr.next is not None 
        while curr is not None: 
            logger.warning(f'inside contains {curr.value}')
            # check if curr.value = search
            if curr.value == search:
                logger.info('entering if')
                # return True & finish
                return True
            # or assign curr as curr.next
            curr = curr.next
        # after looping not found return False
        return False
        
    def printStack(self):
        pass


stk = Stack()
# logger.error(stk.size)
stk.push(A)
# logger.warning(stk.size)
stk.push(B)

logger.info(stk.contains('a'))  # True
# logger.info(stk.contains('t'))  # False
# 
# logger.info(stk.size)  # 2
# stk.printStack()  # a -> b
# 
# logger.info(stk.pop())  # a
# logger.info(stk.pop())  # b
# logger.info(stk.size)  # 0
# stk.printStack()  # empty stack
