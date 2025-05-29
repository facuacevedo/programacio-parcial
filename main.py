def cargar_matriz_notas():
    matriz_notas = []
    n = input("Ingrese la cantidad de alumnos: ")
    # Creo el bucle while para que en caso de que el string ingresado en "n" que debe ser solo un digito entero tenga un "." vuelva a pedir que ingrese el mismo dato
    # Luego lo parseo a entero una vez que salga del bucle
    while "." in n:
        n = input("Ingrese la cantidad de alumnos en numeros enteros: ")
    n = int(n)

    m = input("Ingrese la cantidad de notas: ")
    while "." in m:
        m = input("Ingrese la cantidad de notas en numeros enteros: ")
    m = int(m)

    # Creo una lista de n x m que n son los alumnos y m las notas, luego la relleno con datos 0 para luego recorrerla y llenarla 
    for i in range(n):
        matriz_notas.append([0] * m)
    
    # Recorro el largo de la matriz para obtener sus indices
    for i in range(len(matriz_notas)):
        print("i",i)
        # Denetro de cada indice que representa a un alumno recorro cada nota
        for j in range(len(matriz_notas[i])):
            # Consulto por cada nota que desea ingresar por cada alumno 
            notas = input(f"Ingrese la nota {j + 1} del alumno {i + 1}: ")
            # Valido si el tip de dato de la nota no es digito y entra en el bucle while hasta que ingresa un tipo de dato correcto
            while notas.isdigit() != True:
                notas = input(f"Ingrese la nota {j + 1} del alumno {i + 1} (ingrese un valor numerico): ")
            # Luego valido si la nota se encuentra entre el rango de 1 y 10 inclusives
            while int(notas) <= 0 or int(notas) >= 11:
                notas = input(f"Ingrese la nota {j + 1} del alumno {i + 1} entre 1 y 10: ")
            # Parseo cada nota ingresada
            notas = int(notas)
            # Ubico cada nota ingresada en base a su indice j que sería cada lista de notas de los alumnos en el indice i que corresponde a cada alumno
            matriz_notas[i][j] = notas
    # Retorno la lista completa con todas las notas cargadas y todos los alumnos creados
    return matriz_notas


def porcentaje_aprobados(matriz_alumnos_notas: list):
    # Creo una lista para almacenar todos los porcentajes de las notas aprobadas por cada alumno de la fila recibida por parametro
    matriz_porcentajes_aprobados = []
    # Creo una lista para almacenar en el primer indice de cada alumno el porcentaje de notas aprobadas y el segundo el porcentaje de notas desaprobadas
    resumen_por_alumno = []
    # Utilizo el for para recorrer los indices de las 2 matrices
    for i in range(len(matriz_alumnos_notas)):
        # Creo un acumulador y un contador de las materias aprobadas
        acumulador_notas_aprobadas = 0
        contador_notas = 0
        for j in range(len(matriz_alumnos_notas[i])):
            if matriz_alumnos_notas[i][j] >= 6:
                # Acumulo la cantidad de notas aprobadas 
                acumulador_notas_aprobadas += 1
            # Cuento la cantidad de notas de examen que tiene cada alumno
            contador_notas += 1
            print("acumulador",acumulador_notas_aprobadas)
        # Creo una variable para hacer el calculo del porcentaje de las notas aprobadas 
        porcentaje_aprobados = (acumulador_notas_aprobadas / contador_notas) * 100
        # Luego cargo cada porcentaje de las notas de cada alumno a una nueva lista con todos los porcentajes
        matriz_porcentajes_aprobados.append( porcentaje_aprobados )

    # Creo otro for para recorrer los porcenajes de las notas aprobadas y recorro los indices que referncian a los alumnos 
    for i in range(len(matriz_porcentajes_aprobados)):
        # Creo una variable local para almacenar el porcentaje de notas desaprobadas por cada alumno
        porcentaje_desaprobado_por_alumno = 100 - matriz_porcentajes_aprobados[i] 
        # Por ultimo almaceno en la matriz de resumen por cada alumno el una nueva lista con el porcentaje de materias aprobadas y desaprobadas
        resumen_por_alumno.append([matriz_porcentajes_aprobados[i], porcentaje_desaprobado_por_alumno])
        print(f"EL alumno {i + 1} aprobo el {matriz_porcentajes_aprobados[i]} y desaprobo el {porcentaje_desaprobado_por_alumno}")
    
    return resumen_por_alumno

notas = cargar_matriz_notas()

porcentaje_aprobados(notas)