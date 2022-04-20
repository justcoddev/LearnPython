'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

'''
lista = []
num = 0


def pedir():
    i = 0
    while i <= 5:
        num = float(input('Ingrese un numero: '))
        lista.append(num)
        i += 1


pedir()
print(lista)
'''


def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)


pedir()
print(lista)
ordenar()

'''
