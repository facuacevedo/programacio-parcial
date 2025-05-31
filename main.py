# Importo todas las funciones del archivo de funciones
from funciones import *


# Creo un menu con las opciones
lista_opciones = [
    "------------- MENU DE OPCIONES -------------",
    "1 - Cargar las notas de los alumnos.",
    "2 - Obtener el porcentaje de las notas aprobadas y desaprobadas.",
    "3 - Buscar el mejor promedio de todos los alumnos cargados.",
    "4 - Buscar una nota especifica",
    "0 - Salir del menú."
]

# Creo una bandera para que siempre se muestre el menú con sus respectivas opciones
condicion_menu = True
# Creo una bandera para que primero carguen las notas de los alumnos
notas_cargadas = False
# Creo una lista para almacenar las notas de los alumnos y que siempre se mantengan las mismas para todas las funciones
notas = []

while condicion_menu:
    # Muestro el menu con las opciones
    for i in lista_opciones:
        print(i)

    ingreso_opcion = input("Por favor, ingrese una opción: \n")
    # Valido si el usuario ingresó un flotante o no es un digito, vuelva a solicitar la opción 
    while "." in ingreso_opcion or not ingreso_opcion.isdigit():
        ingreso_opcion = input("Error, por favor, ingrese una opción válida: ")
    
    # Acá valido que el usuario haya ingresado una opción entre las 5 que se imprimen
    while int(ingreso_opcion) < 0 or int(ingreso_opcion) > 4:
        ingreso_opcion = input("Error, por favor, ingrese una opción válida: ")
    # Por ultimo parseo la opción ingresada para el match/case
    ingreso_opcion = int(ingreso_opcion)

    match ingreso_opcion:
        case 1:
            # Reescribo la lista global para almacenar las notas 
            notas = cargar_matriz_notas()
            print("---------------------------------")
            # Recorro todaa la lista y muestro las notas de cada alumno
            for i in range(len(notas)):
                for j in range(len(notas[i])):
                    print(f"Alumno {i + 1} nota {j + 1} : {notas[i][j]} ")
            # Posterior a cargar las notas, cambio el estado de la bandera
            if not notas_cargadas: 
                notas_cargadas = True
        case 2:
            # Consulto la bandera si ya cargaron las notas
            if notas_cargadas:
                # Creo una lista para almacenar los porcentajes aprobados
                porcentajes = porcentaje_aprobados(notas)
                # Recorro la nueva lista con range y len para obtener los indices
                for i in range(len(porcentajes)):
                    # Muestro los porcentajes de materias aprobadas y desaprobadas de cada alumno, utilizo "i + 1" para mostrar cada alumno de la matriz
                    print(f"El alumno: {i+1} aprobo { porcentajes[i][0]} % y desaprobo {porcentajes[i][1]} %")
            # En caso de no estar cargadas las notas, muestro el mensaje para que lo hagan
            else: 
                print("Primero debe cargar las notas, seleccione la opción 1")
        case 3:
            # Consulto la bandera si ya cargaron las notas
            if notas_cargadas:
                # Creo una lista para almacenar los promedios de todos los alumnos
                promedios = lista_de_promedios(notas)
                print("---------------------------------")
                # Creo las 2 variables, indice y promedio, retornadas por la función "mejor_promedio"
                [indice, promedio] = mejor_promedio(promedios)
                # Muestro el alumno con el mejor promedio utilizando las 2 variables creadas anteriormente
                print(f"El mejor promedio es el alumno {indice} con un promedio de {promedio}")
            # En caso de no estar cargadas las notas, muestro el mensaje para que lo hagan
            else: 
                print("Primero debe cargar las notas, seleccione la opción 1")
        case 4:
            # Consulto la bandera si ya cargaron las notas
            if notas_cargadas: 
                # Le consulto al usuario queu nota quiere buscar
                nota_a_buscar = input("Ingrese la nota que desea buscar: ")
                # Valido que sea digito y que no sea un flotante
                while "." in nota_a_buscar or not nota_a_buscar.isdigit():
                    nota_a_buscar = print("Error, ingrese la nota que desea buscar de manera correcta (1 a 10): ")
                # Valido que sea un numero entero
                while int(nota_a_buscar) < 1 or int(nota_a_buscar) > 10:
                    nota_a_buscar = print("Error, ingrese la nota que desea buscar de manera correcta (1 a 10): ")
                # Parseo el número para pasarselo a la función correctamente
                nota_a_buscar = int(nota_a_buscar)
                # Creo una matriz con los alumnos que tengan esa nota a buscar
                notas_buscadas = buscar_nota(notas, nota_a_buscar)
                # Consulto si la función devuelve una cadena de caracteres, ya que la nota puede no estar entre los alumnos y la muestro
                if type(notas_buscadas) == str:
                    print(notas_buscadas)
                else:
                    # Recorro la matriz de notas buscadas con len para recorrer el resto de listas
                    for i in range(len(notas_buscadas)):
                        # Recorro cada alumno que tenga esa nota
                        for j in range(len(notas_buscadas[i])):
                            # Si el tipo de dato es entero, significa que es el número de un alumno que contenga esa nota buscada
                            if type(notas_buscadas[i][j]) == int:
                                # Imprimo el alumno que contenga esa nota
                                print(f"--------- El alumno {notas_buscadas[i][j]} ---------")
                            else:
                                # En caso de que el dato no sea tipo string, va a ser una lista por lo cual la recorro para que muestre el indice o examen que contenga esa nota buscada
                                for k in range(len(notas_buscadas[i][j])):
                                    # Imprimo cada indice que contenga dicha nota buscada
                                    print(f"Tiene el examen {notas_buscadas[i][j][k]} con la nota buscada {nota_a_buscar}")
                                # En caso de no estar cargadas las notas, muestro el mensaje para que lo hagan
            else: 
                print("Primero debe cargar las notas, seleccione la opción 1")

        case 0:
            salir_menu = input("Está seguro que desea salir del menú? (s/n): ").lower()
            if( salir_menu != "si" and salir_menu !="s"):
                continue
            else: 
                break
