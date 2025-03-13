#Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro entero, o sea, que tiene raíz cuadrada entera.
n=int(input("ingrese el entero positivo: "))

if (n**0.5)%1==0:
    print(n,"es el cuadrado de", (n**0.5),)
else:
    print(n,"no tiene raiz cuadrada entera :(")


