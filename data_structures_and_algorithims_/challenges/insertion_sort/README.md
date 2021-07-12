# Challenge Summary

function called insertionsort that sorted an input 
array using insertion method 


## Whiteboard Process

![](/images/insertion_sort.png)



## Approach & Efficiency


Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

## Solution


```
def insertion_sort(list):
    for i in range(1,len(list)):
        j=i-1
        temp=list[i]
        while j>=0 and temp<list[j]:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp
    return list


if __name__ == '__main__':
    print(insertion_sort([8,4,23,42,16,15]))


```