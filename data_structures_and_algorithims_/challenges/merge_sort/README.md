# Challenge Summary

Write a function that implements the Merge sort algorithm, where the input is a list and the output is the sorted list.

## WhiteBoard process

![](/images/merge_sort_vis.png)

## Approach & Efficiency

time : O(n*Log n)

space : O(N)


## Solution

```
def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
 
        i = j = k = 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
    return arr

```