n=int(input("numero "))
b=int(input("base 2≤b>10 "))
residuo=""
conversion=""
if b<10:
    if b>1:
        while n>0:
            residuo=str(n%b)
            conversion= residuo + conversion
            n=n//b
        print(conversion)         
    else:
        print("base no permitida")
else:
    print("base no permitida")        

    
