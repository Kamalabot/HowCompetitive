class Tree:
  def __init__(self, data, children = None):
    if children is None:
      children = []
    self.data = data
    self.children = children
    
def dfs(root):
  if root is None:
    return
  else:
    print(root.data)
    for children in root.children:
      dfs(children)
    
# Time complexity:  O(n) where n is the number of nodes in the tree
#                   because we are just traversing n nodes
# Space complexity: O(h) where h is the height of the tree 
#                   the additional space comes from the maximum call stack size