def multi_bracket_validation(text): # text is n length
    stack = [] # as a stack
    brack_dict = {'}':'{', ']':'[', ')':'('}
    for char in text: # O(n)
        # if open
        if char in brack_dict.values(): # Hidden loop O(n) => Always size 3 / this will search for values only (open brackets)
            stack.append(char)
        # if closed
        if char in brack_dict: # ] => Always size 3 / like : if char in brack_dict.keys(closed brackets)
            bracket = stack.pop() # [
            if brack_dict[char] != bracket:
                return False
       
    if stack:
        return False
    return True


if __name__=='__main__':
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('{}{'))
    print(multi_bracket_validation('{}{}'))