def validate(n):
    num = int(input("Introduce un número natural "))
    while num < 1:
        num = int(input("Introduce un número natural "))
    return num

def decimaltobinary(n):
    count=1
    rem=1
    bin=0
    
    while(n != 0):
        rem = n % 2
        n //= 2
        bin = bin+rem*count 
        count*=10
    return bin
