while True:
    try:
        edad = int(input('Ingrese su edad: '))
        print(f'Tu edad es: {edad}')
        break
    except:
        print('ingresaste un valor erroneo')
