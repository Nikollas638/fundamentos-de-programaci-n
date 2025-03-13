#Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común múltiplo.
n1 =int(input("ingrese el primer numero: "))
n2 =int(input("ingrese el segundo numero: "))
mc=int(1)
i=1

if n1<n2:
    menor=n1
else:
    menor=n2
    
if n1%2 ==0 and n2%2 ==0 or n1%2 ==1 and n2%2 ==1:
    for i in range(1,menor+1,1):
        r1=n1%i
        r2=n2%i
        if r1==0 and r2==0:
            mc=i
            
    print("el maximo comun divisor es", mc)
else:
    while mc<2:
        r1=i%n1
        r2=i%n2
        if r1==0 and r2==0:
            mc=i
        else:
            i=i+1
            
    print("el minimo comun multiplo es", mc)    


