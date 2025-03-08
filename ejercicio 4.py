opcion=0
while opcion !=5:
 print(" ")
 print("---------------calculadora aritmetica---------------")
 print("1. suma")
 print("2. resta")
 print("3. multiplicacion")
 print("4. division")
 print("5. salir")
 opcion = int(input("ingrese la opcion deseada: "))
 if opcion == 1:
    print(" ")
    print("---------------suma---------------")
    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))
    print("la suma es: ", a + b) 
 elif opcion == 2:
     print(" ")
     print("---------------resta---------------")
     a = int(input("ingrese el primer numero: "))
     b = int(input("ingrese el segundo numero: "))
     print("la resta es: ", a - b)
 elif opcion == 3:
     print(" ")
     print("---------------multiplicacion---------------")
     a = int(input("ingrese el primer numero: "))
     b = int(input("ingrese el segundo numero: "))
     print("la multiplicacion es: ", a * b)
 elif opcion == 4:
     print(" ")
     print("---------------division---------------")
     a = int(input("ingrese el primer numero: "))
     b = int(input("ingrese el segundo numero: "))
     print("la division es: ", a / b)
 elif opcion == 5:
     print("----------adiós----------")
 else:
     print(" ")
     print("          *******opcion inválida*******")
     print(" ")