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

    def __init__(self,val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0 

    def push(self, val) -> None:
        if self.size == 0:
            self.top = StackNode(val)
        else:
            pushNode = StackNode(val)
            pushNode.next = self.top
            self.top = pushNode

        self.size += 1

    def getTop(self):
        return self.top.val

    def pop(self):
        if self.size == 0:
            return None
        
        popedNode = self.top
        self.top = self.top.next
        self.size -= 1
        return popedNode.val


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