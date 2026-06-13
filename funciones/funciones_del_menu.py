#importacion modulo nativo csv
import csv

#importacion funciones auxiliares
from .funciones_auxiliares import ( validar_nombre_pais, validar_poblacion_pais, validar_superficie_pais, validar_continente_pais, existe_pais_en_base_datos, filtrar_rango, mostrar_paises )

#!Funcion para leer y obtener los datos del archivo .csv con los datos de los paises ( inicio del programa )
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

#!Funcion para escribir datos en el archivo .csv con los datos ingresados por el usuario ( opcion 1 del menu )
def grabar_datos_nuevo_pais(datos):
    print("A continuación deberá ingresar: nombre, poblacion, superficie y continente al que pertenece el pais que desea añadir.\n")

#Llamado de funciones auxiliares y guardado de su valor de retorno en las variables pertinentes 
#La funcion validar_nombre_pais() recibe como 1er arg la lista con los dict de paises
# y como 2do argumento la bandera en True para que evalue la existencia del nombre del pais dentro de los dict
    nombre_nuevo_pais = validar_nombre_pais( datos, verificar_duplicado=True )
    poblacion_nuevo_pais = validar_poblacion_pais()
    superficie_nuevo_pais = validar_superficie_pais()
    continente_nuevo_pais = validar_continente_pais()

#Variable para almacenar la ruta del archivo a escribir
    ruta_archivo = "data/paises.csv"

#Bloque try/except. Almacena la logica para la escritura del archivo y manejo de posibles errores
    try:
#Bloque de escritura iniciado con with para cierre seguro y automatico del archivo una vez terminada la tarea
        with open( ruta_archivo, "a", newline="", encoding="utf-8") as archivo:

#Emplea DictWriter ya que se estan almacenando los datos de los distintos paises en diccionarios dentro de la lista general "datos"
            escritor = csv.DictWriter( archivo, fieldnames=["nombre","poblacion","superficie","continente"])

#Definicion de diccionario con los datos del pais a guardar
            nuevo_pais = {
                "nombre": nombre_nuevo_pais,
                "poblacion": poblacion_nuevo_pais,
                "superficie": superficie_nuevo_pais,
                "continente": continente_nuevo_pais
                } 
#Funcion writerow del objeto escritor que se creo en la linea anterior. Escribira los datos para el pais con la estructura de diccionario
#Añadira una fila al final del archivo
            escritor.writerow( nuevo_pais )
#Actualizamos la lista datos presente en la memoria RAM. Logramos que "datos" sea igual al archivo .csv recien modificado
            datos.append( nuevo_pais )

#Manejo de errores especificos y previsibles. Si se dispara un error, se realizara el return para frenar la ejecucion de la funcion.
#Manejo de error caso que no exista el archivo
    except FileNotFoundError:
        print("Error: no se encontro el archivo en la ruta especificada")
        return
#Manejo de error caso que no se tengan permisos para editar el archivo o este abierto por otra aplicacion
    except PermissionError:
        print("Error: no posee permisos para la escritura del archivo. Verifique que no este siendo utilizado por otra aplicacion.")
        return
#Manejo de error caso que falle la codificacion
    except UnicodeDecodeError:
        print("Error: el formato de codificacion de caracteres no es compatible.")
        return

#Manejo de error generico ( re de seguridad ). Se manifestara para todos aquellos errores no contemplados previamente en la funcion.
    except Exception as error:
        print(f"Ocurrio un error inesperado: { type( error ).__name__} = { error }")
        return

#Si se logro realizar la escritura correctamente imprimira mensaje de exito por consola
    print("")
    print(f"Se añadió con éxito el país '{ nombre_nuevo_pais }' con la siguiente información:\n")
    print(f"Poblacion: { poblacion_nuevo_pais }")
    print(f"Superficie en kilometros cuadrados: { superficie_nuevo_pais }")
    print(f"Continente: { continente_nuevo_pais }\n")

#!Funcion para actualizar la informacion de un pais seleccionado por el usuario ( opcion 2 del menu )
def actualizar_datos_pais( datos ):
    print("A continuación deberá ingresar: nombre, poblacion y superficie del país que desea modificar.\n")

#Valida y pide solo el nombre del país sin controlar duplicados ya que se hara mas adelante
    nombre_pais_a_modificar = validar_nombre_pais( datos, verificar_duplicado=False )

#Verifica que exista el pais que se quiere modificar
    if not existe_pais_en_base_datos( nombre_pais_a_modificar ,datos ):
        print("El país no se encuentra registrado. ")
        return

#Piden al usuario el dato por teclado y lo validan, guardan valor segun corresponda
    nueva_poblacion_pais = validar_poblacion_pais()
    nueva_superficie_pais = validar_superficie_pais()

#Bucle for, iterara sobre lista datas, buscando el diccionario correspondiente al pais a modificar y actualiza los valores
    for pais in datos:
        if pais["nombre"] == nombre_pais_a_modificar:
            pais["poblacion"] = nueva_poblacion_pais
            pais["superficie"] = nueva_superficie_pais
            break

#Variable para almacenar la ruta del archivo a reescribir
    ruta_archivo = "data/paises.csv"

#Bloque try/except. Almacena la logica para la escritura del archivo y manejo de posibles errores
    try:
#Bloque de escritura iniciado con with para cierre seguro y automatico del archivo una vez terminada la tarea
#Modo "w" para reescribir el archivo
        with open( ruta_archivo, "w", newline="", encoding="utf-8") as archivo:

#Emplea DictWriter ya que se estan almacenando los datos de los distintos paises en diccionarios dentro de la lista general "datos"
            escritor = csv.DictWriter( archivo, fieldnames=["nombre","poblacion","superficie","continente"])
#Volvemos aescribir los nombres de las columnas en el .csv
            escritor.writeheader()

#Funcion writerows del objeto escritor que se creo en lineas previas. Reescribira el archivo con los datos actualizados
            escritor.writerows( datos )

#Manejo de errores especificos y previsibles. Si se dispara un error, se realizara el return para frenar la ejecucion de la funcion.
#Manejo de error caso que no exista el archivo
    except FileNotFoundError:
        print("Error: no se encontro el archivo en la ruta especificada")
        return
#Manejo de error caso que no se tengan permisos para editar el archivo o este abierto por otra aplicacion
    except PermissionError:
        print("Error: no posee permisos para la escritura del archivo. Verifique que no este siendo utilizado por otra aplicacion.")
        return
#Manejo de error caso que falle la codificacion
    except UnicodeDecodeError:
        print("Error: el formato de codificacion de caracteres no es compatible.")
        return

#Manejo de error generico ( re de seguridad ). Se manifestara para todos aquellos errores no contemplados previamente en la funcion.
    except Exception as error:
        print(f"Ocurrio un error inesperado: { type( error ).__name__} = { error }")
        return
    
    print(f"Pais '{ nombre_pais_a_modificar }' actualizado correctamente.\n")

#!Funcion para buscar un pais por nombre y mostrar su informacion en pantalla ( opcion 3 del menu )
def buscar_pais_nombre( datos ):

    print("Buscar País:")

#Valida y pide solo el nombre del país. Bandera en false porque que exista en la base de datos no es un error para esta funcion

    nombre_pais_a_consultar = validar_nombre_pais( datos, verificar_duplicado=False )

#Verifica que exista el pais que se quiere mostrar
    if not existe_pais_en_base_datos( nombre_pais_a_consultar ,datos ):
        print("El país no se encuentra registrado. ")
        return

#Bucle for para recorrer la lista de diccionarios con la informacion de los paises. 
#Ubicar el seleccionado e imprimir sus valores por consola
    for pais in datos:
        if pais["nombre"] == nombre_pais_a_consultar:
            print("")
            print("País encontrado con éxito:\n")
            print(f"Nombre: { pais['nombre'] }")
            print(f"Poblacion: { pais['poblacion'] } ")
            print(f"Superficie: { pais['superficie'] } ")
            print(f"Continente: { pais['continente'] } \n")
            break


#funcion para filtar paises, recibe la lista datos como parametro y filtro que cumple la funcion de seleccionar el metodo de filtrado
def filtrar_paises(datos):
    while True:
        print("""\n
        1_Continente
        2_Poblacion
        3_Superficie
        """)

        try:
            filtro  = int(input("Ingrese el criterio de filtrado: (1 - 3): "))
            if filtro not in range(1,4):
                raise ValueError("Fuera de rango. Ingrese 1, 2 o 3.")
            break
        except ValueError as error:
            print(error)
    
    resultados = []

    #filtrar por continente
    if filtro == 1:
    
        continente_ingresado = validar_continente_pais()
    
        for pais in datos:
            if continente_ingresado == pais["continente"]:
                resultados.append(pais)
    
        if len(resultados) == 0:
            print("No se econtraron paises que correspondan al criterio de busqueda")

    #filtrar por rango de poblacion
    elif filtro == 2:

        resultados = filtrar_rango(datos, "poblacion")    
        if len(resultados) == 0:
            print("No se encontraron paises con la poblacion dentro del rango establecido.")

    #filtrar por rango de superficie
    elif filtro == 3:

        resultados = filtrar_rango(datos, "superficie")
        if len(resultados) == 0:
            print("No se encontraron paises con la superficie dentro del rango establecido.")

    mostrar_paises(resultados)
    return resultados


#funcion para ordenar paises
def ordenar_paises(datos):
    #imprime el menu de forma repetitiva hasta que se ingrese un valor que cumpla con el criterio indicado
    while True:
        print("""\n
            1_Alfabetico
            2_Poblacion
            3_Superficie
            """)
        #valida que la opcion ingresada este en el rango indicado
        try:
            filtro = int(input("Ingrese el criterio de ordenamiento: (1 - 3): "))
            if filtro not in range(1,4):
                raise ValueError("Fuera de rango. Ingrese 1, 2 o 3.")
            #detiene la ejecucion del bucle para continuar con las instrucciones de la funcion
            break
        except ValueError as error:
            print(error)

    #ordena los paises por nombre en orden alfabetico
    if filtro == 1:
        #uso de sorted() para ordenar la lista
        #expresion lambda para pasar el criterio de ordenamiento
        paises_ordenados = sorted(datos, key=lambda x : x["nombre"])
        print("Paises ordenados alfabeticamente")

    #ordena los paises por cantidad de habitantes en orden ascendente
    elif filtro == 2:
        paises_ordenados = sorted(datos, key=lambda x : int(x["poblacion"]))
        print("Paises ordenados por poblacion")

    #ordena los paises de menor a mayor por superficie
    elif filtro == 3:
        paises_ordenados = sorted(datos, key=lambda x : int(x["superficie"]))
        print("Paises ordenados por superficie")

        mostrar_paises(paises_ordenados)
        return paises_ordenados

#funcion que muestra distintas estadisticcas
def ver_estadisticas(datos):
    
    while True:
            
        print("""\n
            1_Pais con mayor y menor poblacion
            2_Promedio de poblacion total
            3_Promedio superficie total
            4_Cantidad de paises por continente
            """)
            
        try:
            opcion = int(input("Ingrese el número de la estadistica a consultar: (1 - 4): "))
            if opcion not in range(1,5):
                raise ValueError("Fuera de rango. Ingrese 1, 2, 3 o 4.")

            break
        except ValueError as error:
            print(error)

    if opcion == 1:
        #min() y max() recorren la lista datos buscando el menor y mayor valor de la clave "poblacion" (convertida a entero), devolviendo el diccionario del pais correspondiente
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
        #recorre la lista datos, obteniendo el valor de poblacion de cada pais y suma las poblaciones
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


def salir():
    print("Se cerro el programa")