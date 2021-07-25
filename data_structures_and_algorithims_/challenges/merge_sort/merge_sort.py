def mergeSort(arr):

    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]
        mergeSort(left_arr)
        mergeSort(right_arr)

        i=0 # left_arr idx
        j=0 # right_arr idx
        k=0 # merged arr idx

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
                k+=1
            else:
                arr[k]=right_arr[j]
                j+=1
                k+=1

        while i<len(left_arr):
            arr[k]=left_arr[i]
            
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1


if __name__ == '__main__':
        arr = [12, 11, 13, 5, 6, 7]
        mergeSort(arr)
        print(arr)

    