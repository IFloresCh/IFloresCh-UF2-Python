# Implementa un programa que demani dos valors enters per teclat i intercanviï els seus valors.
def aaa(a):
    a = int(input("Introduce a: "))
    return a
def bbb(b):
    b = int(input("Introduce b: "))
    return b
    
def intercambia():
    global a, b
    a, b = b, a
    print(a, b)