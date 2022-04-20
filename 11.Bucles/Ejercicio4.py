'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

'''

n1 = int(input('Ingrese primer numero: '))
n2 = int(input('Ingrese segundo numero: '))

'''
for i in range(n1, n2):
    
    if i % 2:
        print(i)
'''
for i in range(n1, n2+1):
    if i % 2 ==0:
        continue
    print(i)