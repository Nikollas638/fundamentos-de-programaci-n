#Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0. 

numero=str(input("Ingrese un número entero positivo: "))
i=len(numero)
reescrito=""

for i in range(i):
    if numero[i]=="9":
        reescrito=reescrito+str(0)
    else:
        reescrito=reescrito+str(int(numero[i])+1)

print(reescrito)