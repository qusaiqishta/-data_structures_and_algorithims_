def reverse_array_1(array):
    return array[::-1]


print(reverse_array_1([1,2,3]))


def reverse_array_2(array):
    new_array=[]
    for i in array:
        new_array.insert(0,i)

    return new_array


print(reverse_array_2([1,2,3]))


def reverse_array_3(array):
    new_array=[]
    for i in range(len(array)-1,-1,-1):
        new_array.append(array[i])

    return new_array


print(reverse_array_3([1,7,3]))




