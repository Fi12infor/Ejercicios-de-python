def dibujar(ancho,altura):
    for i in range(1,altura+1):
        for j in range(1,ancho+1):
            print("*",end="")
        print()

ancho = int(input("Indica la anchura del rectángulo: "))
altura = int(input("Indica la altura del rectángulo: "))

dibujar(ancho,altura)