class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

class Tree:
    
    def __init__(self):
         self.root=None

    def pre_order(self):

        output = ''
        if not self.root:
            return output

        # Define a closure function to be used internally
        def _traverse(node):
            nonlocal output # Because output is not accessible
            output = output + str(node.value) # Root

            if node.left:
                _traverse(node.left)

            if node.right:
                _traverse(node.right) 


            return output

        _traverse(self.root) 

        return output    

    def in_order(self):
        output = ''
        if not self.root:
            return output

        def _traverse(node):
            nonlocal output

            if node.left:
                _traverse(node.left)
            output=output + str(node.value)  

            if node.right:
                _traverse(node.right)    

            return output

        _traverse(self.root)

        return output           

    def post_order(self):
        output = ''
        if not self.root:
            return output

        def _traverse(node):
            nonlocal output

            if node.left:
                _traverse(node.left)

            if node.right:
                _traverse(node.right)

            output=output+str(node.value)

            return output

        _traverse(self.root)   

        return output               


class BST(Tree):
    
    def add(self,value):
        if not self.root:
            self.root=Node(value)
        

        else:
            def go_deep(root):
                
                if value < root.value: # search left
                    if not root.left: # in case there is no left branch
                        root.left=Node(value)  
                        return 

                    else:
                        go_deep(root.left)     # if there is a left branch keep going  

                elif value > root.value:
                    if not root.right:
                        root.right=Node(value)
                        return

                    else:
                        go_deep(root.right)                

            go_deep(self.root)        

    def contains(self,value):
        if not self.root:
            raise AttributeError('Empty Tree')

        current=self.root

        while current:
            if current.value==value:
                return True
            elif current.value>value:
                current=current.left
            elif current.value<value:
                current=current.right

        return False



if __name__ == '__main__':
    tree=Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')     
    print(tree.pre_order())     
    print(tree.in_order())                                 
    print(tree.post_order())

    trees=BST()
    trees.add(0)
    trees.add(1)
    print(trees.root.value)
    print(trees.root.right.value)