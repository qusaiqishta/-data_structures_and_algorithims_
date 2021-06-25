import pysnooper

@pysnooper.snoop('./snoop+logs.log') # just a tool to review the code line by line , all inside snoop+log.log file
def multi_bracket_validation(text): # text is n length
    stack = [] # as a stack
    brack_dict = {'}':'{', ']':'[', ')':'('}
    for char in text: # O(n)
        # if open
        if char in brack_dict.values(): # Hidden loop O(n) => Always size 3
            stack.append(char)
        # if closed
        if char in brack_dict: # ] => Always size 3
            bracket = stack.pop() # [
            if brack_dict[char] != bracket:
                return False
        #if other, do nothing
    if stack:
        return False
    return True
# O(n^2) but it's really O(3*n)

if __name__=='__main__':
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('{}{'))
