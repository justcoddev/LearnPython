# Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

vocal = input('Ingrese una vocal en minuscula: ')
consonante = input('Ingrese una consonante en mayuscula: ')

# o se podria colocar asi y luego concatenar
# vocal = vocal.upper()
#consonante =  consonante.lower()

print(vocal.upper(), consonante.lower())
