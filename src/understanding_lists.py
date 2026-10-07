"""
    
    Las listas nos permiten almacenar información en un lugar, 
    la cantidad que tengas: ya sean pocos elementos o millones
    de elementos.
    
    Una lista es una colección de items (elementos) que tienen
    un orden particular. Se pueden crear listas que incluyan
    strings, números, los nombres de las personas de tu familia, 
    etc. podemos almacenar (los tipos de datos permitidos en 
    Python) lo que queramos en una lista.
    
    Se recomienda nombrar una variable en plural, si la variable 
    es una lista.
    
    En Python, los corchetes [] indican una lista, sus elementos 
    se separan por comas.
    
    Ejemplo de una lista.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""

    Accessando a los elementos de una lista.
    
"""
# Para acceder al primer elemento de una lista
print(bicycles[0])

# Los índices comienzan en 0, no en 1.
print(bicycles[1]) # imprime cannondale
print(bicycles[3]) # imprime specialized

# Accesando al último elemento
print(bicycles[-1]) # specialized

#Accesando al penúltimo
print(bicycles[-2]) # imprime redline

# Utilizando valores individuales de una lista
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Utilizando f-strings
message_f = f"My first biclycle was a {bicycles[0].title()}"
print(message_f)

