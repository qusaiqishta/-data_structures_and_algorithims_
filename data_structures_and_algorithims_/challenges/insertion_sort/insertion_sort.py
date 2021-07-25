def insertion_sort(list):
<<<<<<< HEAD
    for index in range(1,len(list)):
        value=list[index] 
        
        i =index-1
        while i>=0:
            if value<list[i]:
                list[i+1]=list[i]
                list[i]=value
                i=i-1
            else:
                break        
        


if __name__ == '__main__':
    list=[8,4,23,42,16,15]
    insertion_sort(list)
    print(list)
=======
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
>>>>>>> 82c4a39ec20e4c5c83290074d8af81992c468636
