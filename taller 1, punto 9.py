#Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a un valor entero dado por el usuario.
ultimo = 1
penultimo = 0
n = int(input("Introduce un número entero: "))
print(0)
while ultimo <= n:
    print(ultimo)
    ultimo = ultimo + penultimo 
    penultimo = ultimo - penultimo
