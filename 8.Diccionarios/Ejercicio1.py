'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

'''
diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras", "Nicaragua": "Managua",
             "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Ingrese nombre del pais para concoer su capital: ')

#letra = pais.capitalize() in diccionario # TODO: comprueba si se encuntra en el diccionario, para resolver el espacio en las llaves se usa el metodo title()(se encuentra en la seccion de Strings)

#if letra:
if pais.title() in diccionario: # TODO:  al pasar estos parametros directo al if se optimiza el codigo
    print(diccionario[pais.title()])
else:
    print('El pais no se encuentra ne le diccionario')
