def dibujar(ancho,altura,caracter):
    for i in range(1,altura+1):
        for j in range(1,ancho+1):
            print(caracter,end="")
        print()

ancho = int(input("Indica la anchura del rectángulo: "))
altura = int(input("Indica la altura del rectángulo: "))
caracter = input("Indica el caracter que quiere utilizar: ")

dibujar(ancho,altura,caracter)