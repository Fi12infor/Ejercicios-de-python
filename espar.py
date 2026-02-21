def es_par(n):
    return n % 2 == 0

x = int(input("Indica un numero: "))
if es_par(x):
    print(f"{x} es par")
else:
    print(f"{x} es impar")