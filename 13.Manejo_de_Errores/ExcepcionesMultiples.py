while True:
    try:
        num1 = int(input('Ingrese un numero: '))
        resultado = 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print('No se puede dividir entre cero')


while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print(f'Tu edad es: {edad}')
        break
    except ValueError:
        print('ingresaste un valor erroneo')

while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print(f'Tu edad es: {edad}')
        break
    except KeyboardInterrupt:
        print('\nHas cancelado la ejecucion')
