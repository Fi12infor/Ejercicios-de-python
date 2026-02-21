# función para indicar que nota tienes
def notas(nombre, nota):
    if nota >= 0 and nota <= 4:
        print(f"El estudiante {nombre} ha sacado un insuficiente en el modulo de Python")
    elif nota == 5:
        print(f"El estudiante {nombre} ha sacado un suficiente en el modulo de Python")
    elif nota == 6:
        print(f"El estudiante {nombre} ha sacado un bien en el modulo de Python")
    elif nota >= 7 and nota <= 8:
        print(f"El estudiante {nombre} ha sacado un notable en el modulo de Python")
    elif nota >= 9 and nota <= 10:
        print(f"El estudiante {nombre} ha sacado un sobresaliente en el modulo de Python")
    else:
        print("ERROR: Debes indicar una nota valida: ")

# función para contar desde un numero hasta otro
def contar(ini, fin, salto):

    
    if ini < fin:
        fin += 1
        for i in range(ini,fin,salto):
            print(i)
    elif ini > fin:
        fin -= 1
        salto *= -1
        for i in range(ini,fin,salto):
            print(i)
    elif salto <= 0:
        print("No puede indicar un salto negativo")


# Menu principal
op = 0
while op != 3:
    print("1. Notas")
    print("2. Contar")
    print("3. Salir")
    op = int(input("Indique que opcion quiere: "))
    if op == 1:
        nombre = input("Indique el nombre del alumno: ")
        nota = int(input("Indique la nota del alumno: "))
        notas(nombre, nota)
    elif op == 2:
        ini = int(input("Indique en que numero quiere iniciar: "))
        fin = int(input("Indique en que numero quiere finalizar: "))
        salto = int(input("Indique de cuanto quiere el salto: "))
        contar(ini, fin, salto)
    elif op == 3:
        ops = 0
        while ops != "S" or ops != "N":
            ops = input("¿Esta seguro que desea salir? (S/N): ")
            if ops == "S":
                print("Saliendo...")
                break
            elif ops == "N":
                print("Volviendo al programa...")
                op = 0
                break
            else:
                print("ERROR: Opción invalida")
    else:
        print(f"{op} no es una opción valida")
