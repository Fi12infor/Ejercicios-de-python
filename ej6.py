'''
realizar un programa que calcule la media de un conjunto de elementos
- la media se realiza en una función que se le pasa el numero de elementos que lee y calcula la media devuelve el resultado
excepcion -> controlar que el usuario pase un numero
'''
# Declaración de funciones

def calcular_media(numeros):
    sum = 0
    for i in range(numeros):
        try:
            num = int(input("Indique un número: "))
            sum = sum + num
        except ValueError:
            print("No es un valor válido")
    return sum / numeros
    

# Programa principal

cantidad_nums = int(input("Indica cuantos números indicaras: "))
try:
    print(f"La media de los números es: {calcular_media(cantidad_nums)}")
except ValueError:
        print("No es un valor válido")  
