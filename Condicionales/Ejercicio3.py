# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
print('RIMANDO PALABRAS')
palabra = input("Escriba una palabra:")
palabra2 = input("Escriba una palabra:")

if len(palabra) < 3 or len(palabra2) < 3:
    print('No riman, porque no tienen mas de 3 caracteres')
elif palabra[-3:] == palabra2[-3:]:
    print(f'Las palabras "{palabra} y {palabra2}" tienen rima.')
elif palabra[-2:] == palabra2[-2:]:
    print(f'Las palabras "{palabra} y {palabra2}" tienen un poco de rima.')

else:
    print('no tienen rima')
