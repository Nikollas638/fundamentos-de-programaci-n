print("separar las palabras de una frase dada por el ususario, por los espacios")
frase= input("Ingrese una frase: ")
i= len(frase)
palabra= ""
for i in range(i):
    if frase[i] == " ":
        print(palabra)
        palabra= ""
    else:
        palabra= palabra + frase[i]

print(palabra)
