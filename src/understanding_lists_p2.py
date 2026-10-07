# Agregando elementos elementos a una lista.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Método append - Agrega elementos al final
# de la lista
motorcycles.append('ducati')
motorcycles.append('bmw')
print(motorcycles)

# Método insert - Agrega elementos en un lugar
# específico
motorcycles.insert(0, 'Italika')
motorcycles.insert(3, 'kawasaki')


"""
    Eliminar elementos a una lista
"""
# Método del - si conocemos el índice del elemento que deseamos eliminar
del motorcycles[0]
print(motorcycles)

# Método pop() -> Elimina el último elemento 
# de la lista, pero nos permite utilizar el 
# elemento después de eliminarlo
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Método pop(índice) -> Se puede utilizar también 
# para eliminar un elemento específico
element_to_delete = motorcycles.pop(0)
print(motorcycles)
print(element_to_delete)

"""
    Si vas a utilizar el elemento que vas a eliminar
    después de eliminarlo, utiliza pop() sino utiliza
    del.
"""

# Método remove() -> Permite eliminar elementos 
# por su valor
motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expesive for me. ")
print(f"I can buy {motorcycles}")
