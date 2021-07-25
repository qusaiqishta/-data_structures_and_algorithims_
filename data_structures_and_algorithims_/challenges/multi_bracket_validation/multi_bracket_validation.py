def multi_bracket_validation(text):
   stack=[]
   bracket_dic={'}':'{',']':'[',')':'('}

   for char in text:
       if char in bracket_dic.values():
           stack.append(char)
       elif char in bracket_dic:
           bracket=stack.pop()
           if bracket_dic[char]!=bracket:
               return False
   if stack:
        return False 
   return True                


if __name__ == '__main__':
    print(multi_bracket_validation('{}'))                        