cars = ['bmw', 'audi', 'toyotta']
cars.sort()
print(cars)

# ordenar la lista de manera ordenada en reversa
cars.sort(reverse=True)
print(cars)

"""
    Función built-in sorted
    
    Ordena la lista de manera temporal 

"""
cars = ['bmw', 'audi', 'toyotta']
print("Lista Original")
print(cars)
print("Lista Ordenada")
print(sorted(cars))
print("Lista Original")
print(cars)

"""
    Método reverse
    
    El método reverse de las listas
    invierte la lista de manera permanente

"""
cars.reverse()
print(cars)

"""

    Función built-in len

    Longitud de las listas
    
    El método len nos dice la cantidad
    de elementos que hay en una lista
    
"""

print(len(cars))