# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

lista = [20, 50, "Curso", 'Python', 3.14]
print(f'Lista original {lista}')
nombre = input('Ingrese su nombre: ')
lista[0] = nombre
edad = int(input('Ingrese su edad: '))
lista[1] = int(edad)

print(lista)