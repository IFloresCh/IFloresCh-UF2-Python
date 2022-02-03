# Implementa una solució per a un algoritme que demani a l’usuari que introdueixi per teclat un valor natural  que correspondrà al total de segons, 
# i l’algoritme haurà de retornar el total de dies, hores, minuts i segons. 
#

def validate():
    num = int(input("Introduce el tiempo en segundos: "))
    if num < 1:
        num = int(input("Introduce el tiempo en segundos: "))
    return num


def secsTo():
    days = 0
    hours = 0
    mins = 0

    time = num   
    days = time / 1440     
    leftover_minutes = time % 1440
    hours = leftover_minutes / 60
    mins = time - (days*1440) - (hours*60)
    print(str(days) + " days, " + str(hours) + " hours, " + str(mins) +  " mins. ")