from data_structures_and_algorithims_.challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_empty():
    assert insertion_sort([])==[]

def test_already_sorted():
    assert insertion_sort([1,2,3,])==[1,2,3]    


def test_reversed():
    assert insertion_sort([3,2,1])==[1,2,3]



def test_nearly_sorted():
    assert insertion_sort([1,2,3,5,9,7])==[1,2,3,5,7,9]


def test_insertion_unique():
    assert insertion_sort([5,12,7,5,5,7])==[5,5,5,7,7,12]

def test_insertion_normal():
    assert insertion_sort([8,4,23,42,16,15]) == [4,8,15,16,23,42]  


