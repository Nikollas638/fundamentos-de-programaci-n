# Escribir un programa que reciba una entrada n, que es un número entero. El programa devolverá una lista de números enteros hasta n, incluyéndolo, y especificando si el número es divisible por 2, 3 o por 5, o si es divisible por ambos.

n = int(input("Ingrese un número entero: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(f"{i}. es divisible por 2, 3 y 5")
    elif i % 2 == 0 and i % 3 == 0:
        print(f"{i}. es divisible por 2 y 3")
    elif i % 2 == 0 and i % 5 == 0:
        print(f"{i}. es divisible por 2 y 5")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i}. es divisible por 3 y 5")
    elif i % 2 == 0:
        print(f"{i}. es divisible por 2")
    elif i % 3 == 0:
        print(f"{i}. es divisible por 3")
    elif i % 5 == 0:
        print(f"{i}. es divisible por 5")
    else:
        print(f"{i}.")
 
 