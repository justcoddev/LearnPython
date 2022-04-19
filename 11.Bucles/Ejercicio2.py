'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad).

'''

edad = int(input('Ingrese su edad: '))
i = 0

while i != edad:
    i +=1
    print(f'ha festejado su cumpleaños numero: {i}')