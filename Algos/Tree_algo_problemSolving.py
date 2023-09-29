""" File System Navigation using a Tree:

In this example, we can represent a file system as a tree structure. We'll write a Python program to navigate the file system and list all files and directories using a tree traversal algorithm.
 """
import os

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_file_tree(path):
    root = TreeNode(path)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            root.children.append(build_file_tree(item_path))
        else:
            root.children.append(TreeNode(item))
    return root

def list_files_and_directories(node, indent=0):
    print(' ' * indent + node.name)
    for child in node.children:
        list_files_and_directories(child, indent + 2)

root_node = build_file_tree('/path/to/your/directory')
list_files_and_directories(root_node)
""" 
Decision Trees for Classification:

Decision trees are used in machine learning for classification tasks. In this example, we'll use the scikit-learn library to create a decision tree classifier and train it on a dataset.
 """
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset as an example
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

""" Binary Search Tree (BST) for Searching and Insertion:

Binary Search Trees are used for efficient searching and insertion of elements. In this example, we'll implement a simple binary search tree in Python and perform insertion and search operations.
 """
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

result = bst.search(30)
if result:
    print(f'Key 30 found in BST')
else:
    print(f'Key 30 not found in BST')