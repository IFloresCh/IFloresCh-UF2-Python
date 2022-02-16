def validate():
    num = int(input("Ingrese un número entre 1 y 50 a registrar: "))
    while num not in range(1, 50):
        num = int(input("Ingrese un número entre 1 y 50 a registrar: "))
    return num        
def lists(num):
    list = [int(input("Ingrese un número: ")) for x in range(num)]
    return list
