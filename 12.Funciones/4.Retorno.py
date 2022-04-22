'''
def <nombre de la funcion> ().
    <sentencias>
    return
'''


def entero():
    print('Este es un dato entero: ')
    return 10


def decimal():
    print('Este es un dato decimal: ')
    return 90.99


def frase():
    return 'Mi nombre es Teddy Summers'


def asignacion():
    return 1, 2, 3, 4, 5


print(entero())
print(decimal())
print(frase())

print(asignacion())
a, b, c, d, e = asignacion()
print(a)
print(b)
print(c)
print(d)
print(e+2)