from data_structures_and_algorithims_.data_structure.stacks_and_queues.stacks_and_queues import Queue
from data_structures_and_algorithims_.data_structure.trees.trees import Node , Tree


          



def rules(node):
    if node.value%3==0 and node.value%5!=0:
        return 'Fizz'
    elif node.value%5==0 and node.value%3!=0:
        return "Buzz"
    elif node.value%3!=0 and node.value%5!=0:
        return str(node.value)
    else:
        return "FizzBuzz"  
def fizz_buzz_tree(tree):
    output=[]
    new_tree=tree
    if new_tree.root:
        output.append(rules(new_tree.root))

        if new_tree.root.left:
           output.append(rules(new_tree.root.left))

        if new_tree.root.right:
           output.append(rules(new_tree.root.right)) 
        return output   

    else:
        new_tree.root =Node('Empty Tree')
        return new_tree



if __name__ == "__main__":
    b_tree = Tree()
    b_tree.root = Node(15)
    b_tree.root.left = Node(8)
    b_tree.root.right= Node(9)
   
   
    print(fizz_buzz_tree(b_tree))        


    




            