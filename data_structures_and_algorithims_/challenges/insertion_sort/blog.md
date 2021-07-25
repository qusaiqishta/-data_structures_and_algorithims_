## Insertion Sort 

Insertion sort is the sorting mechanism where the sorted array is built having one item at a time. The array elements are compared with each other sequentially and then arranged simultaneously in some particular order.

## Pseudocode
```

func insertion_sort(array)

for i=1 to range array.length
k=array[i]
# insert array[i] into the sorted sequence array[1 ...i-1]
j=i-1
where j>0 and array[j]>k
    array[j+1]=array[j]
    j=j-1
array[j+1]=k

```

## Trace

Sample Array: [8,4,23,42,16,15]


![](/images/insertion_sort.jpg)


### Visualization 
![](/images/insertion_sort_vis.jpg)




## Efficency

Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.


Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).