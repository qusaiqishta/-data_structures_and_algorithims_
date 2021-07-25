# Challenge Summary
first_repeated is a function that returns the first world/char repeated in a text



## White board process

![](/images/first_repeated.png)



## Approach & Efficiency

- Time Complixity : O(2n)

- space complixity : O(n)

## Solution 

```
input: "Qusai omar fathi qishta qusai"

expected output: 'qusai'
___________________________________
dic={}
r_str_as_list=['Qusai','omar','fathi','qishta','qusai']

for i in range(len(r_str_as_list)):
r_str_as_list[i]=r_str_as_list[i].lower() -> this will take every word and convert it to lower case

=> r_str_as_list=['qusai','omar','fathi','qishta','qusai']


for i in range(0,len(r_str_as_list)):
        key=r_str_as_list[i] # the first key will be 'qusai'
        if key not in dic: #  if 'qusai' in dic ? NOO
            dic[key]=1 # put 'qusai' inside the dic with value=1
        else:
            dic[key]=dic[key]+1 # when i reach the second 'qusai' will check if it is exit in dic , if yes it will increase the value by 1

=> dic={'qusai': 2, 'omar': 1, 'fathi': 1, 'qishta': 1}


for index in range(0,len(r_str_as_list)):
        if dic[r_str_as_list[index]]>=2: # this if will go inside the dic and check for first key the has value more than or equal 2
            return r_str_as_list[index]

'qusai' will be return

```