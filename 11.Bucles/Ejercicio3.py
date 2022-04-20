'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

'''
for i in range(1, 10):
    print(i)
    
n1 = int(input('Ingrese primer numero: '))
n2 = int(input('Ingrese segundo numero: '))

for i in range(n1, n2+1):
    print(i)
