from data_structures_and_algorithims_.data_structure.trees.trees import Node , Tree


def fizz_buzz_tree(tree):
    if tree.root:
        output=[]
    def _rules(node):
        if node.value%3==0 and node.value%5==0:
            output.append('FizzBuzz')  
        elif node.value %3==0:
            output.append('Fizz')
        elif node.value%5==0:
            output.append('Buzz')
        elif node.value%3!=5 and node.value%3!=0:
            output.append(node.value)
        if node.left:
            _rules(node.left)
        if node.right:
            _rules(node.right)  
    _rules(tree.root)     
    return output                  

if __name__ == "__main__":
    b_tree = Tree()
    b_tree.root = Node(15)
    b_tree.root.left = Node(8)
    b_tree.root.left.left=Node(11)
    b_tree.root.right= Node(9)
   
   
    print(fizz_buzz_tree(b_tree))        


    




            