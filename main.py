# Importo todas las funciones del archivo de funciones
from funciones import *

# Creo la matriz de notas y las cargo 
notas = cargar_matriz_notas()

# Muestro todas las notas por cada alumno
for i in range(len(notas)):
    for j in range(len(notas[i])):
        print(f"Las nota {j + 1 } del alumno {i + 1} es: {notas[i][j]}")

# Llamo a la función que muestre el porcentaje de los aprobados en base a las notas cargadas previamente y la guardo en una nueva matriz
porcentaje_notas = porcentaje_aprobados(notas)

# Nuestro el resumen de cada alumno, porcentaje de notas aprobadas y desaprobadas
for i in range(len(porcentaje_notas)):
    print(f"El alumno {i + 1} aprobó {porcentaje_notas[i][0]} y desaprobo {porcentaje_notas[i][1]}")
