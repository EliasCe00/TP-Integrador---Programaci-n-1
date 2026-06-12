#Importacion modulo nativo csv para manipulacion de archivos
import csv

#Funcion para inciar el programa y visualizacion del menu
def iniciar_programa():

#Llamado de funcion obtener_datos() para tener disponible la informacion
    datos = obtener_datos()
    print(datos)
#Menu de opciones
    while True:
        print("---- Gestión de Datos de Países ----\n")
        print("1. Añadir país a la base de datos")
        print("2. Actualizar datos ( Población y Superficie )")
        print("3. Visualizar información sobre países")
        print("4. Filtrar países ( Continente, población o superficie )")
        print("5. Ordenar Países ")
        print("6. Ver estadísticas ")
        print("7. Salir\n")

#Pide al usuario que opte por una opcion
        opcion = input("Ingrese una opción ( 1 - 7 ): ")

#Valida la opcion elegida por el usuario
        try:
#Debe ser numero
            opcion = int(opcion)
#Debe estar entre 1 y 7
            if opcion not in range(1,8):
                raise ValueError("Opción invalida: debe ingresar un número entre 1 y 7 ")

        except ValueError as error:
            if "invalid literal" in str(error):
                print("Dato ingresado invalido: debe ingresar un número entre 1 y 7")
            else:
                print(error)

#Opcion 1 - Añadir pais a la base de datos
        if opcion == 1:
            print("opcion 1")

#Opcion 2 - Actualizar datos de 1 pais
        elif opcion == 2:
            print("opcion 2")

#Opcion 3 - Visualizar informacion sobre los paises ( muestra 1 o todos segun opte el usuario )
        elif opcion == 3:
            print("opcion 3")

#Opcion 4 - Filtrar paises segun continente, poblacion o superficie
        elif opcion == 4:

            #mini menu persistente? o vuelve a las opcines del menu?
            print("""\n
                1_Continente
                2_Poblacion
                3_Superficie
                """)
            try:
                filtro  = int(input("Ingrese el criterio de filtrado: (1 - 3)"))
                if filtro not in range(1,4):
                    raise ValueError("Fuera de rango. Ingrese 1, 2 o 3.")
            
                paises_filtrados = filtrar_paises(datos, filtro)
                mostrar_paises(paises_filtrados)

            except ValueError as error:
                print(error)


#Opcion 5 - Ordenar paises segun orden alfabetico, poblacion y superficie
        elif opcion == 5:

            #mini menu persistente? o vuelve a las opcines del menu?
            print("""\n
                1_Alfabetico
                2_Poblacion
                3_Superficie
                """)
            try:
                filtro = int(input("Ingrese el criterio de ordenamiento: (1 - 3)"))
                if filtro not in range(1,4):
                    raise ValueError("Fuera de rango. Ingrese 1, 2 o 3.")

                paises_ordenados = ordenar_paises(datos, filtro)
                mostrar_paises(paises_ordenados)

            except ValueError as error:
                print(error)
            


#Opcion 6 - Ver estadisticas: Pais con mayor y menor poblacion, promedio de poblacion total, promedio superficie total, cantidad de paises por continente
        elif opcion == 6:
            #mini menu persistente? o vuelve a las opcines del menu?
            print("""\n
                1_Pais con mayor y menor poblacion
                2_Promedio de poblacion total
                3_Promedio superficie total
                4_Cantidad de paises por continente
                """)
            try:
                estadistica = int(input("Ingrese el número de la estadistica a consultar: (1 - 4)"))
                if opcion not in range(1,5):
                    raise ValueError("Fuera de rango. Ingrese 1, 2, 3 o 4.")

                ver_estadisticas(datos, estadistica)

            except ValueError as error:
                print(error)

#Opcion 7 - Salir del programa
        elif opcion == 7:
            salir()
            break





#!Funcion para leer y obtener los datos del archivo .csv con los datos de los paises
def obtener_datos():
#Guarda ruta del archivo en variable dentro del scope de la funcion
    ruta_archivo = "data/paises.csv"

#Crea lista "datos" para almacenar la informacion en caso de exito
    datos = []

#Bloque try/except para abrir archivo y almacenar datos en caso de exito
    try:
        with open( ruta_archivo, "r", encoding="utf-8" ) as archivo:

            lector = csv.DictReader( archivo )

#Bucle for añade a la lista "datos" las filas en formato diccionario
            for fila in lector :
                datos.append(fila)
            
            return datos

#Excepciones para errores Comunes
    except FileNotFoundError:
        print("Error: Ruta del archivo incorrecta. No se pudo encontrar el archivo.")
        return []
    
    except PermissionError:
        print("Error: No posee permisos para leer el archivo. Asegurese de que el archivo no este abierto por otra apliacion.")
        return []
    
    except UnicodeDecodeError:
        print("Error: encoding del archivo erroneo.")
        return []

#Excepcion para errores no previstos
    except Exception as e:
        print(f"Error inesperado: { type(e).__name__ } = { e }.")
        return []


#!Funcion para escribir datos en el archivo .csv con los datos ingresados por el usuario
def grabar_datos_nuevo_pais(datos):
    print("Datos guardados")




def actualizar_datos_pais():
    print("Datos actualizados")

def buscar_pais_nombre():
#?Debe pedir nombre pais evaluarlo y mostrar por consola los datos para ese pais
#?Debe informar con claridad caso que no se encuentre el pais
#?Debe informar con claridad si el usuario no ingreso caracteres al hacer "enter"
    print("Pais unico")

def filtrar_paises(datos, filtro):
    
    resultados = []

    #filtrar por continente
    if filtro == 1:
        
        continente_ingresado = input("Ingrese un continente: ")
        for pais in datos:
            if continente_ingresado == pais["continente"]:
                resultados.append(pais)
        
        if len(resultados) == 0:
            print("No se econtraron paises que correspondan al criterio de busqueda")

    #filtrar por rango de poblacion
    elif filtro == 2:

        rango_minimo = int(input("Ingrese el rango minimo de poblacion: "))
        rango_maximo = int(input("Ingrese el rango maximo de poblacion: "))

        for pais in datos:
            if int(pais["poblacion"]) >= rango_minimo and int(pais["poblacion"]) <= rango_maximo:
                resultados.append(pais)
            
        if len(resultados) == 0:
            print("No se encontraron paises con la poblacion dentro del rango establecido.")

    #filtrar por rango de superficie
    elif filtro == 3:

        rango_minimo = int(input("Ingrese el rango minimo de superficie: "))
        rango_maximo = int(input("Ingrese el rango maximo de superficie: "))

        for pais in datos:
            if int(pais["superficie"]) >= rango_minimo and int(pais["superficie"]) <= rango_maximo:
                resultados.append(pais)

        if len(resultados) == 0:
            print("No se encontraron paises con la superficie dentro del rango establecido.")

    return resultados

#funcion para mostrar los paises en pantalla
def mostrar_paises(lista_paises):

    #si la lista esta vacia frena la ejecucion
    if len(lista_paises) == 0:
        return
    
    #imprime los elementos de la lista
    for pais in lista_paises:
        print("----------")
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente']}")
        print("----------")

#funcion para ordenar paises
def ordenar_paises(datos, filtro):
    if filtro == 1:
        #uso de sorted() para ordenar la lista
        #expresion lambda para pasar el criterio de ordenamiento
        paises_ordenados = sorted(datos, key=lambda x : x["nombre"])
        print("Paises ordenados alfabeticamente")

    elif filtro == 2:
        paises_ordenados = sorted(datos, key=lambda x : int(x["poblacion"]))
        print("Paises ordenados por poblacion")

    elif filtro == 3:
        paises_ordenados = sorted(datos, key=lambda x : int(x["superficie"]))
        print("Paises ordenados por superficie")

    return paises_ordenados


def ver_estadisticas(datos, opcion):
    
    print("Estadisticas")
    print("-" * 20)

    if opcion == 1:

        pais_menos_poblado = min(datos, key=lambda x : int(x["poblacion"]))
        pais_mas_poblado = max(datos, key=lambda x : int(x["poblacion"]))
    
        print("\nEstadisticas: pais con mayor y menor poblacion")
        print("-" * 20)
        print(f"\nPais con menor población: {pais_menos_poblado['nombre']} posee {pais_menos_poblado['poblacion']} habitantes.")
        print(f"Pais con mayor población: {pais_mas_poblado['nombre']} posee {pais_mas_poblado['poblacion']} habitantes.")
        return

    elif opcion == 2:

        print("\nEstadisticas: promedio de población")
        print("-" * 20)

        suma_poblacion = 0
        #suma todos los habitantes de todos los paises
        for pais in datos:
            suma_poblacion += int(pais["poblacion"])
        
        promedio_poblacion = suma_poblacion / len(datos)

        print(f"El promedio de poblacion es: {promedio_poblacion}")
        return
    
    elif opcion == 3:
        print("\nEstadisticas: promedio de superficie")
        print("-" * 20)
    
        suma_superficie = 0
        #suma todas las superficies de todos los paises
        for pais in datos:
            suma_superficie += int(pais["superficie"])
    
        promedio_superficie = suma_superficie / len(datos)

        print(f"El promedio de superficie es: {promedio_superficie}")
        return

    elif opcion == 4:
        print("Estadisticas: cantidad de paises por continente")
        print("-" * 20)

        #obtener continentes
        continentes = set()
        for pais in datos:
            continentes.add(pais["continente"])

        for continente in continentes:
            contador = 0
            for pais in datos:
                if pais["continente"] == continente:
                    contador += 1
            print(f"{continente} : {contador} paises")
        return


def ver_paises():
#?Debe mostrar los paises cargados en el archivo
    print("Paises")

def salir():
#?Cierra el programa
    print("Se cerro el programa")



















if __name__ == "__main__":
    iniciar_programa()

