import functions as f

def main():
    register = f.cantidad()
    f.registros(register)
    libros = f.registros()
    f.headers()
    f.imprimir(libros)
    
    
    
if __name__ == '__main__':
    main()