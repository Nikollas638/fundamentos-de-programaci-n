n = int(input("limite de la lista de numeros divisibles por 2, 3 o 5 "))
i= int(2)
coma="\n"
numero=""
lista=""
for i in range (n+1):
    if i!=0:
    
     if i%2==0:
         numero= str(i) 
         lista= lista + coma + numero
     else:
         if i%3==0:
             numero= str(i) 
             lista= lista + coma+ numero
         else:
             if i%5==0:
                 numero= str(i) 
                 lista= lista + coma+ numero
             else:
                 lista=lista
                
print(lista)            
        
        

