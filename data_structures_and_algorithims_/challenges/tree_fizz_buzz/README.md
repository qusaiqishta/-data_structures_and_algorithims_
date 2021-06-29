## Challenge Summary

a function called fizz buzz tree
takes Arguments: k-ary tree
Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both

## Whiteboard Process

![](/images/fizz_buzz_tree.png)


## Approach & Efficiency

Big(O)->O(N)

## Solution

```
input :
  b_tree = Tree()
    b_tree.root = Node(15)
    b_tree.root.left = Node(8)
    b_tree.root.right= Node(9)

expected output:
['FizzBuzz', '8', 'Fizz']


fizz_buzz_tree(b_tree)
output=[]
new_tree=b_tree
new_tree.root=15

if 15:
output.append(rules(15))
GO TO RULES AND CHECK FOR 15
15 %3==0 and 15%5==0 so will return FizzBuzz
output=['FizzBuzz']
new_tree.root.left=8
if 8:
output.append(rules(8))
CHECK FOR 8 IN RULES

output=['FizzBuzz',8]


new_tree.right=9
if 9:
output.append(rules(9))
GO TO RULES AND CHECK FOR 9

FINALLY 

output=['FizzBuzz',8,'Fizz']
```