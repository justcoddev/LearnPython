'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''



def factorial1():
    num = int(input('Ingrese u numero etero positivo: '))
    if num > 0:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        print(factorial)
    else:
        print('El numero es negativo y no podemos proceder.')


factorial1()




#--------------------------optima---------------------------
def factorial2():
    from math import factorial
    num = int(input('Ingrese u numero etero positivo: '))
    if num > 0:
        print(factorial(num))
    else:
        print('El numero es negativo y no podemos proceder.')


factorial2()
