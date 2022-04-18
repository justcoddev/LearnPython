'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

'''

tupla = ('enero', 'febrero', 'marzo', 'abri', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

numero = int(input('ingrese un numero para obener el mes: '))


print('el mes es: ',tupla[numero-1])


'''
if numero in tupla:
    print( tupla[numero])
else:
    print('El numero de mes no existe')

'''