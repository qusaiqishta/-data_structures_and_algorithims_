def quickSort(arr,left,right):
    if left<right:
        position=partition(arr,left,right)
        quickSort(arr,left,position-1)
        quickSort(arr,position+1,right)

      
def partition(arr,left,right):
    pivot=arr[right]
    low=left-1
    for i in range(left,right):
        if arr[i]<=pivot:
            low+=1
            swap(arr,i,low)
    swap(arr,right,low+1)

    return low+1

def swap(arr,i,low):
    temp=arr[i]     
    arr[i]=arr[low]
    arr[low]=temp


arr=[8,4,23,42,16,15]
quickSort(arr,0,len(arr)-1)
print(arr)



def quick_sort(sequence):
    if len(sequence)<=1:
        return sequence
    else:
        pivot=sequence.pop()
        items_greater=[]
        items_lower=[]

        for item in sequence:
            if item<pivot:
                items_lower.append(item)
            else:
                items_greater.append(item)
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)                

arr=[8,4,23,42,16,15]
print(quick_sort(arr))

