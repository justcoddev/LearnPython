# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: < solucion >”

from math import sqrt
print("Formula General")
# a = int(input("Ingrese 'a': "))
# b = int(input("Ingrese 'b': "))
# c = int(input("Ingrese 'c': "))

# formulaGeneral = (((-b) + - (((b**2)-(4*a*c))**2)) / (2*a))
# print(f"El resultado es {formulaGeneral}")


# solucion2

a = int(input("Ingrese 'a': "))
b = int(input("Ingrese 'b': "))
c = int(input("Ingrese 'c': "))
x1 = 0
x2 = 0

if((b**2)-(4*a*c)) < 0:
    print("no se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print("la solucion es: \nx1=",x1,"\nx2=",x2)