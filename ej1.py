# Funcion que devuelva el maximo de dos números
def max_num(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

num1 = int(input("Indica el primer numero: "))
num2 = int(input("Indica el segundo numero: "))
x = max_num(num1,num2)

print(f"El es mayor es {x}")
