a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

def intercambia():
    global a, b
    a, b = b, a
    print(a, b)

    
def main():
    intercambia()
    print(a, b)


if __name__ == "__main__":
	main()
