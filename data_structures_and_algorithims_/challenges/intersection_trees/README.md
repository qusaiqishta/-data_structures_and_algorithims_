# Challenge Summary

find the common nodes between two binary trees

## Whiteboard Process
![](/images/trees_intersection.png)

## Approach & Efficiency

- Time complixity : O(3n)
- space complixity: O(2n)
---

## Solution
```
tree1=[1,2]
tree2=[1,0]
expected output:
[1]
_______________
tree_intersection(tree1,tree2)
tree1=tree1.pre_order() ->tree1=12
 tree2=tree2.pre_order() -> tree2=10

tree1_list=[]
 tree2_list=[]
common=[]
    for char in tree1: # this will store t1 elements into a list form
        tree1_]list.append(char)
# tree_list=[1,2]
    for char in tree2:
        tree2_list.append(char)   
# tree2_list=[1,0]

for char in tree1_list:
        if char in tree2_list: 
            common.append(char)    
# common=[1]
    return list(set(common))
# set here for returning only the unique values 

```