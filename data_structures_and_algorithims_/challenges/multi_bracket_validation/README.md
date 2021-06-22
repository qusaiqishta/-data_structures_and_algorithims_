## Challenge Summary

Given an expression string, write a python program to find whether a given string has balanced parentheses or not(each open paren. has a similar closed one )


## Whiteboard Process

![](/images/multi_bracket_validation.png)


## Approach & Efficiency

Big(O)->O(N)


## Solution
```
open_list = ["[","{","("]
close_list = ["]","}",")"]

def multi_bracket_validation('{}')
stack=[]

for i in '{}'
if i in open_list -> '{' is it is in open_list
stack.append('{') -> stack=['{']

=>then check another bracket '}'
elif i in closed_list => yes '}' is in 
pos=close_list.index('}')=1
if (1>0) and (open_list[1]==stack[0])  => True and True 
stack.pop()
stack=[]

if len(stack)==0 yess
return True 
```