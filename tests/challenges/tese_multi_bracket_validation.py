from data_structures_and_algorithims_.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation
import pytest


def test_single_brackets():
    actual=multi_bracket_validation('{}')
    expected='True'
    assert actual == expected


def test_two_brackets_two_para():
    actual=multi_bracket_validation('{}(){}')
    expected='True'
    assert actual == expected
    
def test_two_square_brackets_one_para_with_extra_char():
    actual=multi_bracket_validation('()[[Extra Characters]]')
    expected='True'
    assert actual == expected     

def test_two_square_brackets_one_para():
    actual=multi_bracket_validation('()[[]]')
    expected='True'
    assert actual == expected     

# test for {}{Code}[Fellows](())

def test_multible_para_with_text():
    actual=multi_bracket_validation('{}{Code}[Fellows](())')  
    expected='True'

# test for [({}]

def test_unbalanced():
    actual=multi_bracket_validation('[({}]')  
    expected='False'


# test for (](

def test_unbalanced_1():
    actual=multi_bracket_validation('(](')  
    expected='False'
        

# test for {(})

def test_unbalanced_2():
    actual=multi_bracket_validation('{(})')  
    expected='False'
                


    