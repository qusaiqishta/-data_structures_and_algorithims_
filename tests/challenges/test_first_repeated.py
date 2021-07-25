def first_repeated(r_str):
    dic={} 
    r_str_as_list=r_str.split()
    for i in range(0,len(r_str_as_list)):
        r_str_as_list[i]=r_str_as_list[i].lower()

    for i in range(0,len(r_str_as_list)):
        key=r_str_as_list[i]
        if key not in dic:
            dic[key]=1
        else:
            dic[key]=dic[key]+1
    print(dic)     

    
    for index in range(0,len(r_str_as_list)):
        if dic[r_str_as_list[index]]>=2:
            return r_str_as_list[index]

# I can not import the function for some reasons            
def test_text_one():
    actual=first_repeated("Once upon a time, there was a brave princess who...")
    expected='a'
    assert actual==expected

def test_text_two():
    actual=first_repeated("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected='it'
    assert actual==expected    


def test_text_three():
    actual=first_repeated("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected='was'
    assert actual==expected    
