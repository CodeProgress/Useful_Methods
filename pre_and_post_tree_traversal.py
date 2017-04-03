# pre and post order tree traversal
# python 3

def preOrder(root):
    print(str(root.data) + " ", end="") # prints output on same line
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(str(root.data) + " ", end="") # prints output on same line