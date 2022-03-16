'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.
'''
payasoPeso = 112
munecaPeso = 75

clienteFrecuenteP = 23
clienteFrecuenteM = 54
pesoTotal = (payasoPeso * clienteFrecuenteP) + (munecaPeso * clienteFrecuenteM)
print(pesoTotal)
print('El peso total es de',pesoTotal,'g')
