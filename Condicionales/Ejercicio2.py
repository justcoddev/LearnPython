# Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

numero = int(input('Ingrese un numero entero para determinar su valor absoluto: '))

numero2 = numero * (-1)

if numero > 0:
    print(f'El valor absoluto de {numero} es {numero}')

else:
    print(f'El valor absoluto de {numero} es {numero2}')
#tambien se puede colocar el valor absoluto de un numero así 
#---> abs(numero)