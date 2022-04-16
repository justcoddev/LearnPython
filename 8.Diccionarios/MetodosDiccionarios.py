diccionario = {1: 2, 2: 3, 3: 4}
print(diccionario)
# TODO: Elimina la llave
diccionario.pop(3)
print(diccionario)

# TODO: Nos permite limpiar todo el diccionario
diccionario = {1: 2, 2: 3, 3: 4}
print(diccionario)
diccionario.clear()
print(diccionario)

# TODO: nos devuelve el valor que colocamos en dicha llave
diccionario = {1: 2, 2: 3, 3: 4}
print(diccionario)
print(diccionario.get(2))

# TODO:  agragar nuevo valor a continuación
diccionario = {1: 2, 2: 3, 3: 4}
print(diccionario)
diccionario.setdefault(4, 5)
print(diccionario)

# TODO: Se actualizan lso diccionarios(juntan, si esta repetida solo mantiene una)
diccionario = {1: 2, 2: 3, 3: 4}
diccionario2 = {4: 5, 6: 7}
print(diccionario)
print(diccionario2)
diccionario.update(diccionario2)
print(diccionario)

# TODO: genera copia de diccionario
diccionario = {1: 2, 2: 3, 3: 4}
print(diccionario)
diccionario.copy()
print(diccionario)