
class Tree:
 
 #init function : is going to initialize each  node with data and every time it will print "object is created" so that we know init is executed
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        print("object is created")
       
#function which takes node as input and checks   the following conditions : 
def depthcounter(node.left)
       right =depthcounter(node.right):
    if node is None:       # if node is not present return 0
        return 0 ; 
    else :
#recursive  call to both left and right part of tree     
       left = depthcounter(node.left)
       right =depthcounter(node.right)
 
#After obtaining value from  depthcounter(node.left)and depthcounter(node.right) ,check which one is greater
# and add 1 as every child node is 1 step below the parent node
       if (left > right):
           return left+1
       else:
           return right+1
 
 
#starting of program, call class tree and initialize values for every node defined below  
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.left.right = Tree(6)
root.right.right=Tree(7)
 
 function calling :  depthcounter()
print("The depth of the tree is  :: ", depthcounter(root))
