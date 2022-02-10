def evenNumbers():
    i, a_list = 2, []
    
    while len(a_list) < 101:
        a_list.append(i)
        i += 2
    
    for x in a_list:
        print(x)
        