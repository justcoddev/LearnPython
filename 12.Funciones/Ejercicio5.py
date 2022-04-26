'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
'''

def areaCuadrado(base, altura):
    area = base * altura
    print(area)
    
areaCuadrado(10,4)

'''
def areaCirculo(radio):
    area = (radio**2)*3.14
    print(area)
   
''' 
# TODO:  mas optimo
def areaCirculo(radio):
    return pow(radio,2) * 3.14


print(areaCirculo(10))