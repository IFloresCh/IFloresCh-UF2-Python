# El projecte en que estàs treballant requereix que l’usuari introdueixi un valor natural entre 10 i 5000 (inclosos)
# i, en cas que no ho faci, li torni a demanar que introdueixi el nombre (fins a un màxim de 3 cops). Implementa aquesta funció de validació.

def validate():
    num = int(input("Introduce un numero entre 10 y 5000: "))
    for i in range(2):
        if num < 10 or num > 5000:
            num = int(input("Introduce un numero entre 10 y 5000: "))
        i+=1
    return num
