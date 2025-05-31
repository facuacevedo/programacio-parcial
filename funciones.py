# Creo una función para crear la matriz de cantidad de alumnos y cantidad de notas de examen
def crear_matiz_notas():
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
    return matriz_notas

# Creo la función para cargar las notas de los examenes por cada alumno
def cargar_matriz_notas():
    matriz_notas = crear_matiz_notas()

    for i in range(len(matriz_notas)):
        # Denetro de cada indice que representa a un alumno recorro cada nota
        for j in range(len(matriz_notas[i])):
            # Consulto por cada nota que desea ingresar por cada alumno 
            notas = input(f"Ingrese la nota {j + 1} del alumno {i + 1}: ")
            # Valido si el tip de dato de la nota no es digito y entra en el bucle while hasta que ingresa un tipo de dato correcto
            while "." in notas or not notas.isdigit():
                notas = input(f"Ingrese la nota {j + 1} del alumno {i + 1} (ingrese un valor numerico y entero): ")
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
    
    return resumen_por_alumno

# PUNTO 3 

def calcular_promedio(lista: list):
    """
        Esta función recibe una lista con números y retorna una variable con el promedio
    """
    # Creo 2 variables locales, una para acumular todos los valores que contenga la lista y otro para contar cuantos valores hay dentro de esa lista
    contador_promedio = 0
    acumulador_promedio = 0
    # Creo una variable para almacenar el valor del promedio
    promedio = 0
    # Recorro la lista pasada por parametro 
    for i in lista:
        # Acumulo el/los valores que se encuentren en la lista
        acumulador_promedio += i
        # Voy sumando al contador 1 por cada valor que haya dentro de esa lista
        contador_promedio += 1
    # Realizo el calculo para saber el promedio de los valores que se encuentren en la lista, es decir, la suma total de los valores dividido la cantidad total de valores que haya
    promedio = acumulador_promedio / contador_promedio
    # Retorno la variable con promedio de los valores de la lista
    return promedio

def lista_de_promedios(matriz_numeros: list):
    """
        Esta función recibe una matriz bidimensional de numeros, calcula el promedio de cada sublista y retorna una nueva lista con el promedio de esas sublistas 
    """
    # Creo una lista para almacenar todos los promedios
    promedios = []
    # Recorro la lista bidimensional para obtener cada sublista
    for i in matriz_numeros:
        # Por cada subista creo una variable local para almacenar ese promedio en base a la función creada anteriormente, la cual le paso una lista y me calcula el promedio 
        promedio_por_sublista = calcular_promedio(i)
        # Cargo por orden de iteración el promedio de cada sublista a la lista de promedios creada
        promedios.append(promedio_por_sublista)
    # Retorno la nueva lista con los promedios de cada sublista
    return promedios


def mejor_promedio(lista_promedios: list):
    """
        Esta función recibe una lista con promedios, encuentra el mejor promedio y retorna una variable con el indice del mayor promedio y el mayor promedio 
    """
    # Creo 2 variables, una para almacenar el valor del mejor promedio o el mayor y en la segunda para almacenar el indice de ese mejor promedio 
    mejor_promedio = 0
    indice_mejor_promedio = 0
    # Recorro la lista de promedios para obtener su indice
    for i in range(len(lista_promedios)):
        # Consulto por cada valor si es mayor al mejor promedio y en caso de serlo, lo almaceno en la variable mejor_promedio
        if lista_promedios[i] > mejor_promedio:
            mejor_promedio = lista_promedios[i]
            # Cargo el indice nuevo mejor promedio
            indice_mejor_promedio = i + 1

    # Retorno primero el indice y luego el mejor promedio, (esto lo probe y funciona, pero se hacerlo por react, por ejemplo con useState que retorna 1 variable y su funcion setter o cuando creo un custom hooks)
    # Para acceder a su valor o sus valores se puede hacer de la siguiente forma [indice, promedio] = mejor_promedio(lista) y de esta forma acceder
    return indice_mejor_promedio, mejor_promedio 
    
# PUNTO 4
# Creo una función para buscar un numero y retornar una lista con los indices donde aparece dicho numero dentro de la lista pasada por parametro
def buscar_numero(lista:list, numero_buscar: int):
    """
        Esta función recibe una lista con números y un número entero que se desea buscar en la lista, busca en que posición se encuentra ese número y retorna una nueva lista con el indice donde se encuentra ese numero, en base a la lista pasada por parametro. 
    """
    # Creo una lista para almacenar los indices encontrados
    lista_numero_buscado = []
    # Recorro la lista con range y len para obtener el indice 
    for i in range(len(lista)):
        # Consulto si el valor es igual al numero que estoy buscando
        if lista[i] == numero_buscar:
            # Almaceno ese indice en caso de que el valor de lista sea igual al numero buscado y luego guardo ese valor en la lista creada anteriormente
            lista_numero_buscado.append( i + 1 )
    # Retorno la nueva lista con todos los indices donde aparece ese numero buscado
    return lista_numero_buscado

def buscar_nota(matriz_alumnos_notas: list, nota_buscar: int):
    """
        Esta función recibe una matriz de n alumnos y m notas, también recibe un número entero(la nota a buscar) y retorna una nueva matriz con:
        Indice de alumno con esa nota y una lista con el indice donde aparece esa nota. 
        Ejemplo: [1, [2, 10]] -> Alumno 1, tiene 1 sola nota de 10 en el indice 2, que representa a la 3er nota de la lista
    """
    # Creo una matriz para almacenar el indice del alumno que contenga esa nota a buscar y la cantidad de veces que se repita esa nota con su respectivo indice
    matriz_nota_buscada = []
    # Creo una variable local para almacenar un mensaje y retornarlo en ncaso de que no encuentre esa nota
    mensaje = "No hay ninguna nota con ese valor!"
    # Recorro la matriz con en para obtener los indices de los alumnos
    for i in range(len(matriz_alumnos_notas)):
        # Busco esa nota y la almaceno en una nueva lista, utilizando la funcion previamente creada
        indice_notas_por_alumno = buscar_numero(matriz_alumnos_notas[i], nota_buscar)
        # Consulto si la matriz tiene algun valor
        if len(indice_notas_por_alumno) > 0 :
            # En caso de tenerlo, guardo los valorers en la matriz creada previamente, es decir, el indice del alumno y la cantidad de veces que se repita esa nota buscada
            matriz_nota_buscada.append([i + 1, indice_notas_por_alumno])
    # Consulto si en todos los alumnos encontro esa nota y en caso de no hacerlo, retorne el mensaje previamente creado
    if len(matriz_nota_buscada) < 1:
        return mensaje 
    # En caso de que haya algun alumno con esa nota buscada, lo retorno en la nueva matriz
    else:
        return matriz_nota_buscada
