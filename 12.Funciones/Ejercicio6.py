'''
Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

'''


'''
def medida(*tupla):
    print(len(tupla))


medida(2, 3, 4, 10, 20)


def medida2(*tupla):
    return len(tupla)


print(medida2(2, 3, 4, 10, 20))

'''

def medida3(*tupla):
    print(len(tupla))
    for i in tupla:
        print(i)
    return len(tupla)


print(medida3(2, 3, 4, 10, 20))
