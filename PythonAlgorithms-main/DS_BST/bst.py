class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.val = val
        self.right = None

def insert(root, node):
    if not root:
        root = node
        return

    if node.val > root.val:
        if not root.right:
            root.right = node
        else:
            insert(root.right, node)
        
    if node.val < root.val:
        if not root.left:
            root.left = node
        else:
            insert(root.left, node)

def preorder(node):
    if node:
        print(node.val, end="-> ")
        preorder(node.left)
        preorder(node.right)

def search(root, key):
    if root:
        if root.val == key:
            print("found")
            return
        if root.val > key:
            search(root.left, key)
        if root.val < key:
            search(root.right, key)
    else:
        print("Not found")
        
def minimumValue(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left =  delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = minimumValue(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


if __name__== "__main__":
    root = Node(5)
    insert(root, Node(3))
    insert(root, Node(2))
    insert(root, Node(4))
    insert(root, Node(7))
    insert(root, Node(6))
    insert(root, Node(8))
    preorder(root)
    print("\n----------------")
    search(root, 20)
    print("\n----------------")
    delete(root, 7)
    preorder(root)