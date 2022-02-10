def validate():
    num = int(input("Ingrese un número entre 1 y 50 a registrar: "))
    while num < 1 or num > 50:
        num = int(input("Ingrese cuantos vas a registrar: "))
    return num        
def lists(num):
    list = [int(input("Ingrese un número: ")) for x in range(num)]
    return list
