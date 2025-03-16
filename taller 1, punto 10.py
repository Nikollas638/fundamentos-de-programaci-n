#Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor entero dado por el usuario.
ultimo = 1
penultimo = 0
n = int(input("Introduce un número entero: "))

while ultimo <= n:

    ultimo = ultimo + penultimo 
    penultimo = ultimo - penultimo

print(ultimo)