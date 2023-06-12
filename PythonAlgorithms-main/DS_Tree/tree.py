class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.val = val
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end="->")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.val, end="->")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end="->")
    

root = Node(4)
root.right = Node(5)
root.left = Node(6)
root.left.left = Node(7)
print ("\n==============")
inorder(root)
print ("\n==============")
preorder(root)
print ("\n==============")
postorder(root)
print ("\n==============")
