SIZE = 15

def validate():
    
    note = int(input("Introduce una nota entre 0 y 10: "))
    while note < 0 or note > 10:
        note = int(input("Introduce una nota entre 0 y 10: "))
    return note

def mitjana():
    
    lista2 = [x for x in range(31) if x % 2 == 0]
    
a = int(input("Introdueix a: "))
b = int(input("Introdueix b: "))

def intercambia():
    global a, b
    a, b = b, a
print(a, b)
    
def main():
    intercambia()
    print(a, b)


if __name__ == "__main__":
    main()