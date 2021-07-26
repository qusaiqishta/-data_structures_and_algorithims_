def first_repeated(r_str):
    dic={} # will store each char in r_str and how many times it is repeated

    r_str_as_list=r_str.split()
    for i in range(0,len(r_str_as_list)):
        r_str_as_list[i]=r_str_as_list[i].lower()

    for i in range(0,len(r_str_as_list)):
        key=r_str_as_list[i]
        if key not in dic:
            dic[key]=1
        else:
            dic[key]=dic[key]+1
            break
# at this point , i have dic containing keys(chars) and values(frequency)

    
    for index in range(0,len(r_str_as_list)):
        if dic[r_str_as_list[index]]>=2:
            return r_str_as_list[index]
                      

print(first_repeated("It was a queer, sultry summer , the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))               

