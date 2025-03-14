#Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el número primo de valor más cercano, en este caso menor o igual, al número leído.

numero=int((input("ingrese un numero entero (mayor que 2): ")))
i = numero
divisores=int(0)
if numero <=2:
    print( (numero), "no es mayor que 2")
else:
    for numero in range(numero,0,-1):
        i= numero
        while i>1:
            if numero%i==0:
                divisores=divisores+1
            else:
                divisores=divisores
            i=i-1
            
        if divisores==1:
            print("el primo mas cercano es",(numero))
            break
        else:
            divisores=0
        
