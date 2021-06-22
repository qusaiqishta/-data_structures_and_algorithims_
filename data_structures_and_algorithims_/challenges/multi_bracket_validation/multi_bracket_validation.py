open_list = ["[","{","("]
close_list = ["]","}",")"]
  
def multi_bracket_validation(input):
    stack = []
    for i in input:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"





if __name__ == '__main__':
    print(multi_bracket_validation('{[]{()}}'))
    print(multi_bracket_validation('{[]{()}})'))
