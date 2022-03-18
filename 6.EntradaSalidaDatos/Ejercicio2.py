# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
# Considere:

# PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

# Donde: P1, P2, P3 : Practicas

# PP: promedio de práctica

# PROM: promedio

# EP: examen parcial

# EF: examen final

p1 = int(input("P1: "))
p2 = int(input("P2: "))
p3 = int(input("P3: "))
exaP = int(input("Examen Parcial: "))
exaF = int(input("Examen Final: "))
promedioPractica = (p1+p2+p3)/3
promedioFinal = (promedioPractica + (2*exaP)+(3*exaF))/6
print(F"El promedio final es {promedioFinal}")
