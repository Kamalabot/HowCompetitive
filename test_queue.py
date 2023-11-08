class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        # self.bottom = None
        self.size = 0

    def push(self, val):
        if self.size == 0:
            self.top = Node(val)
            # self.bottom = Node(val)
        else:
            pushNode = Node(val)
            pushNode.next = self.top
            self.top = pushNode
        self.size += 1
    
    def getTop(self):
        return self.top.val
    
    def pop(self):
        if self.size == 0:
            return None
        else:
            curr = self.top
            self.top = self.top.next
            self.size -= 1
            return curr.val

    def __str__(self):
        str = ""
        curr = self.top
        #print(curr.val)
        str += f"{curr.val} ->"
        while curr.next is not None:
            curr = curr.next
            str += f"{curr.val} ->"
        return str


# x = Node(1)
# y = Node(2)
# z = Node(3)
# No need to create the node, the values can be pushed directly

newStack = Stack()
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(0.5)
newStack.push('its awesome')

print(newStack.size)

print(newStack)

print(newStack.pop())
print(newStack.pop())

print(newStack.size)
