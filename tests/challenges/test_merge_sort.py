from data_structures_and_algorithims_.challenges.merge_sort.merge_sort import mergeSort


def test_merge_empty():
    assert mergeSort([])==[]


def test_reversed_sorted():
    assert mergeSort([20,18,12,8,5,-2])==[-2,5,8,12,18,20]    


def test_merge_few_uniques():
    assert mergeSort([5,12,7,5,5,7])==[5,5,5,7,7,12]



def test_merge_nearly_sorted():
    assert mergeSort([2,3,5,7,13,11])==[2,3,5,7,11,13]

def test_merge_unsorted():
    assert mergeSort([8,4,23,42,16,15])  == [4,8,15,16,23,42]  
