#Escribir un programa que determine si un número entero es positivo, negativo o cero. Después, modificar el programa para que reciba entradas de números enteros hasta que el número introducido sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.
n=1
positivos = 0
negativos = 0
suma_positivos = 0
suma_negativos = 0

while n != 0:
    n = int(input("Introduce un número entero: "))
    if n > 0:
        print(f"{n} es positivo.")
        positivos = positivos + 1
        suma_positivos = suma_positivos + n
    elif n < 0:
        print(f"{n} es negativo.")
        negativos = negativos + 1
        suma_negativos = suma_negativos + n
    else:

        break

print("------------------------------------")

if positivos == 0:
    print("No se introdujeron números positivos.")
else:
    print(f"Se introdujeron {positivos} números positivos.")
    print(f"El promedio de los números positivos es {suma_positivos/positivos}.")

if negativos == 0:
    print("No se introdujeron números negativos.")
else:
    print(f"Se introdujeron {negativos} números negativos.")
    print(f"El promedio de los números negativos es {suma_negativos/negativos}.")
    