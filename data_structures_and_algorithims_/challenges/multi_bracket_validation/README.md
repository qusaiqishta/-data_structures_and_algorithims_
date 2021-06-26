## Challenge Summary

Given an expression string, write a python program to find whether a given string has balanced parentheses or not(each open paren. has a similar closed one )


## Whiteboard Process

![](/images/multi_bracket_stack_solu.png)


## Approach & Efficiency

Big(O)->O(3*N)


## Solution
```
def multi_bracket_validation('{}')
stack=[]
brack_dict = {'}':'{', ']':'[', ')':'('}

for char  in '{}'  iteration1 targeted '{'
if '{' in  barck_dict.values()     YESS IT IS
stack.append({) => stack=['{']

iteration2 
if '}' in brack_dict.values()  NOOO

if '}' in brack_dict:   Yess
bracket=stack.pop()  => stack=[] , bracket=['{']

if brack_dict['}']!=bracket:  it is equal

if stack:  empty stack here
  return false

return True
```