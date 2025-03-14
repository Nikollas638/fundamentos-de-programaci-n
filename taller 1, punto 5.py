#Escribir un programa que permita convertir un entero dado en base 2, 4, 8, 16
n=int(input("inserte numero a convertir: "))
i=n
residuo=""
conversion=""

while n>0:
    residuo=str(n%2)
    conversion= residuo + conversion
    n=n//2
print("en base 2: ",conversion)         
n=i
residuo=""
conversion=""

while n>0:
    residuo=str(n%4)
    conversion= residuo + conversion
    n=n//4
print("en base 4: ",conversion)         
n=i
residuo=""
conversion=""

while n>0:
    residuo=str(n%8)
    conversion= residuo + conversion
    n=n//8
print("en base 8: ",conversion)         
n=i
residuo=""
conversion=""

while n>0:
    residuo=str(n%16)
    if residuo=="10":
        residuo="A"
    elif residuo=="11":
        residuo="B"
    elif residuo=="12":
        residuo="C"
    elif residuo=="13":
        residuo="D"
    elif residuo=="14":
        residuo="E"
    elif residuo=="15":
        residuo="F"

    conversion= residuo + conversion
    n=n//16

print("en base 16: ",conversion)
  




