def dibujar_mitad(anchura):
    for i in range(1,anchura+1):
        for j in range(1,i+1):
            print("*",end="")
        print()


anchura = int(input("Indica la anchura: "))
dibujar_mitad(anchura)