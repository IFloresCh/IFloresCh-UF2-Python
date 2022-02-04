def evenNumbers():
    a_list = []
    i = 2

    while len(a_list) < 101:
        a_list.append(i)
        i += 2
    
    for x in a_list:
        print(x)
        