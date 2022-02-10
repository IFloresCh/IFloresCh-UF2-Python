MSG_1 = "Ingrese un número: "
MSG_2 = "Debe ser numero natural\nIngrese un número: "


def validate():
    num = int(input(MSG_1))
    while num < 1:
        num = int(input(MSG_2))
    return num  

def suma(num):
    a, i = [], 0
    while i < num:
        a.append(i)
    print(a)
    return num