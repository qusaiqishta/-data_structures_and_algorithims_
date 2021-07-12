def binary_search(array,num):
    start=0
    end=len(array)-1
    middle=0

    while(num in array):
        middle=(start+end)//2
        if num>array[middle]:
            start=middle+1

        elif num<array[middle]:
            end=middle-1
        else:
            return middle

    return -1

if __name__ == '__main__':

     print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 13))                    