class Tree:
 
   
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        print("object is created")
 
def depthcounter(node):
    if node is None:
        return 0 ; 
    else :
       left = depthcounter(node.left)
       right =depthcounter(node.right)
 
      
       if (left > right):
           return left+1
       else:
           return right+1
 
 

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.left.right = Tree(6)
root.right.right=Tree(7)
 
 
print("The depth of the tree is  :: ", depthcounter(root))
