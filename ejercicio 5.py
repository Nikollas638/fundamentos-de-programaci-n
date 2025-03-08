print("-------conversor de palabras a pig latin-------")
print("")
palabra= str(input("ingrese una palabra: "))
i=len(palabra)
piglatin = ""
if palabra[0] == "a" or palabra[0] == "e" or palabra[0] == "i" or palabra[0] == "o" or palabra[0] == "u":
     for i in range(i):
         piglatin = piglatin+palabra[i]
else: 
    for i in range(i-1):
     piglatin=piglatin+palabra[i+1]
    piglatin=piglatin+palabra[0]

piglatin = piglatin+"ay"
print(piglatin)