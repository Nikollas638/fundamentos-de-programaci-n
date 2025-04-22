n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

def busqueda_binario(n, lista, inicio=0):

    mitad = len(lista) // 2

    print(f"Lista: {lista}, Mitad: {mitad}, Inicio: {inicio}")

    if len(lista) == 0:
        return "El valor no se encuentra en la lista."

    if lista[mitad] == n:
        return f"El valor {n} se encuentra en la lista, en la posición {inicio + mitad}."
    
    elif lista[mitad] < n:
        # Buscar en la mitad superior
        return busqueda_binario(n, lista[mitad + 1:], inicio + mitad + 1)
    
    else:
        # Buscar en la mitad inferior
        return busqueda_binario(n, lista[:mitad], inicio)

valor = int(input("Inserte el valor a buscar: "))
print(busqueda_binario(valor, n))