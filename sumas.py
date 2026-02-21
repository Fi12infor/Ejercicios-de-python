def suma_susesiva(num):
    f = 0
    for i in range(1,numero+1):
        f = f+i
    return f


numero = int(input("Indica el numero a calcular su factorial: "))
print(f"El resultado es: {suma_susesiva(numero)}")