from data_structures_and_algorithims_.challenges.quick_sort.quick_sort import quickSort



def test_quick_sorted():
    assert quickSort([20,18,12,8,5,-2],0,5)==[-2,5,8,12,18,20]    


def test_quick_few_uniques():
    assert quickSort([5,12,7,5,5,7],0,5)==[5,5,5,7,7,12]



def test_quick_nearly_sorted():
    assert quickSort([2,3,5,7,13,11],0,5)==[2,3,5,7,11,13]

def test_quick_unsorted():
    assert quickSort([8,4,23,42,16,15],0,5)  == [4,8,15,16,23,42]  
