# Challenge

takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list






# Whiteboard process

![](/images/zip.png)




# Efficiency
Big(O)
Time , space ->O(N)


# Solution

```

list1: [1,2,3]
list2: [4,5,6]
expected output=[1,4,2,5,3,6]
list1.head=1
list2.hrad=4
current1=1
current2=4


while 1
list1.insertafter(1,4)
current1=3
current2=5
current1==none  NOO
list1=[1,4,2,3]
while 3
list1.insertafter(3,5)
current1=none
current2=6
list1=[1,3,2,5]

last loop
list1.insertafter(3,6)

list1=[1,3,2,4,5,6]



```




