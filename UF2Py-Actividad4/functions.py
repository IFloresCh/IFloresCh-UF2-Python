def validate(num):
    num = int(input("Introduce un numero entre 10 y 5000: "))
    for i in range(2):
        if num < 10 or num > 5000:
            num = int(input("Introduce un numero entre 10 y 5000: "))
        i+=1
    return num