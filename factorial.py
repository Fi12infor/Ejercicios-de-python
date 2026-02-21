def calculo_factorial(num):
    f = 1
    for i in range(1,numero+1):
        f = f*i
    return f


numero = int(input("Indica el numero a calcular su factorial: "))
print(f"El resultado es: {calculo_factorial(numero)}")