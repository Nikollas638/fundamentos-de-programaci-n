#Construir un programa que lea un número variable de valores enteros. El resultado que entregara el programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores pares dividida por el número de estos. 

sumapar=int(0)
cantidadpar=int(0)

numeros= int(input("ingrese la cantidad de enteros a leer: "))

#dentro de este for se va a ir pidiendo al usuario que ingrese cada numero, hasta la cantidad anunciada, inmediatamente despues de que ingrese el numero se evaua si es par y si lo es, se suma con los anteriores pares y aumenta el contador de la cantidad de numeros pares que hay

for i in range (numeros):
    numero = int(input(f"ingrese el entero {i+1}: "))
    if numero%2==0:
        sumapar= sumapar + numero
        cantidadpar=cantidadpar+1
 
print("la media de los numeros pares es", (sumapar/cantidadpar),": ")