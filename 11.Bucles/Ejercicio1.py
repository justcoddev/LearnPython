'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

numero = int(input('Ingrese un numero que desea la tabla de multiplicar: '))
i = 0  # TODO: iterador
while i <= 12:
    tabla = numero * i
    print(f'{numero} * {i} = {tabla} ')
    i += 1
