MSG_1 = "Cuantos libros quiere registrar?: "
MSG_2 = "Ingrese un numero natural\nCuantos libros quiere registrar?: "
TITT = "Ingrese el titulo: "
AUTO = "Ingrese el autor: "
EDIT = "Ingrese la editorial: "
YEAR = "Ingrese el año de publicación: "
DISP = "Ingrese la cantidad disponible: "
CURR = "Usuario actual en prestamo: "
BRRW = "Dias de prestamo: "


def cantidad():
    registres = int(input(MSG_1))
    while registres < 1:
         registres = int(input(MSG_2))
    return registres

       
         
def registros(register, **dictionary):
    cantidad = register
    tittle, autor, editorial, year, disp, current_user, brrwd_time  = list(), list(), list(), list(), list(), list(), list()
    for x in range(cantidad):
        tittle.append(input(TITT))
        autor.append(input(AUTO))
        editorial.append(input(EDIT))
        year.append(int(input(YEAR)))
        disp.append(int(input(DISP)))
        current_user.append(input(CURR))
        brrwd_time.append(input(BRRW))
    dictionary = {
        'titulo': tittle,
        'autor': autor,
        'editorial':editorial,
        'Año': year,
        'Disponibles': disp,
        'Usuario': current_user,
        'Dias Prestados': brrwd_time      
    }
    return dictionary    
def headers():
    print("{:<20}| {:<20}| {:<20}| {:<20}| {:<20}| {:<20}| {:<20}|".format('Titulo', 'Autor', 'Editorial', 'Año', 'Disponibles', 'Usuario', 'Dias prestados'))

def imprimir(libros):
    registres = cantidad()
    for x in range(registres):
        print("{:<20}| {:<20}| {:<20}| {:<20}| {:<20}| {:<20}| {:<20}|".format(libros.tittle[x]))