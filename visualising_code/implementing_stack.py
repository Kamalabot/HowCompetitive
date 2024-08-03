# Implementing the stack using a simple array

stack = []

# Pushing new element has to be done from the front or top in this case 
stack.insert(0, 'a')
stack.insert(0, 'b')
stack.insert(0, 'c')
# print(stack)

# Poping existing element from the front 

# print(stack.pop(0))
# print(stack.pop(0))
# print(stack.pop(0))
# 
# print(stack)

# Issue with push and pop is, each operation will be O(n) as each element has to be updated
# Maximally efficient Stack has to operate with Time complexity of O(1)


class StackNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, value):
        # if stack is empty
        if self.size == 0:
            # make the value as top node
            self.top = StackNode(value)
        # else take top node and assign to next of value 
        else:
            # create a new node
            newNode = StackNode(value)
            newNode.next = self.top
            # assign newNode as top
            self.top = newNode
 
        # increase the size by 1
        self.size += 1
    
    def getTop(self):
        return self.top.val

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
 
    def __str__(self) -> str:
        if self.size == 0:
            return "Stack Empty"
        curr = self.top
        string = ""
        while curr is not None:
            string += "->" + str(curr.val)
            curr = curr.next
        return string


stk = Stack()
stk.push('a')
stk.push('b')


print("first size check", stk.size)
print(stk.top.val)
print(stk.top.next.val)

popednode = stk.pop()
print(popednode)

print(stk.top.val)
print("last size check", stk.size)