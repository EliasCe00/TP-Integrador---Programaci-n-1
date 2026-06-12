#Importacion modulo nativo csv para manipulacion de archivos
import csv
#Importacion modulo nativo os para manipulacion de archivos
import os

#--Funcion inicializacion del programa y funciones del menu
#Funcion para inciar el programa y visualizacion del menu
def iniciar_programa():

#Llamado de funcion obtener_datos() para tener disponible la informacion
    datos = obtener_datos()
#Menu de opciones
    while True:
        print("---- Gestión de Datos de Países ----\n")
        print("1. Añadir país a la base de datos.")
        print("2. Actualizar datos ( Población y Superficie ).")
        print("3. Visualizar información sobre países.")
        print("4. Filtrar países ( Continente, población o superficie ).")
        print("5. Ordenar Países.")
        print("6. Ver estadísticas.")
        print("7. Salir\n")

#Pide al usuario que opte por una opcion
        opcion = input("Ingrese una opción ( 1 - 7 ): ")

#Valida la opcion elegida por el usuario
        try:
#Debe ser numero
            validar_opcion = int(opcion)
#Debe estar entre 1 y 7
            if validar_opcion not in range( 1,8 ):
                raise ValueError("Opción invalida: debe ingresar un número entre 1 y 7 ")
            opcion = validar_opcion

        except ValueError as error:
            if "invalid literal" in str( error ):
                print("Dato ingresado invalido: debe ingresar un número entre 1 y 7")
            else:
                print(error)
            continue

#Opcion 1 - Añadir pais a la base de datos
        if opcion == 1:
            grabar_datos_nuevo_pais( datos )

#Opcion 2 - Actualizar datos de 1 pais
        elif opcion == 2:
            actualizar_datos_pais( datos )

#Opcion 3 - Visualizar informacion sobre los paises ( muestra 1 o todos segun opte el usuario )
        elif opcion == 3:
            print("opcion 3")

#Opcion 4 - Filtrar paises segun continente, poblacion o superficie
        elif opcion == 4:
            print("opcion 4")

#Opcion 5 - Ordenar paises segun orden alfabetico, poblacion y superficie
        elif opcion == 5:
            print("opcion 5")

#Opcion 6 - Ver estadisticas: Pais con mayor y menor poblacion, promedio de poblacion total, promedio superficie total, cantidad de paises por continente
        elif opcion == 6:
            print("opcion 6")

#Opcion 7 - Salir del programa
        elif opcion == 7:
            print("opcion 7")
        

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
        print("Error: el formato de codificacion de caracteres no es compatible. No se pudo leer el archivo.")
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

#!Funcion para actualizar la informacion de un pais seleccionado por el usuario
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
        print("Error: el formato de codificacion de caracteres no es compatible. No se pudo leer el archivo.")
        return

#Manejo de error generico ( re de seguridad ). Se manifestara para todos aquellos errores no contemplados previamente en la funcion.
    except Exception as error:
        print(f"Ocurrio un error inesperado: { type( error ).__name__} = { error }")
        return
    
    print(f"Pais '{ nombre_pais_a_modificar }' actualizado correctamente.\n")

def buscar_pais_nombre():
#?Debe pedir nombre pais evaluarlo y mostrar por consola los datos para ese pais
#?Debe informar con claridad caso que no se encuentre el pais
#?Debe informar con claridad si el usuario no ingreso caracteres al hacer "enter"
    print("Pais unico")

def ordenar_paises():
#?Debe comparar valor de strings y ordenarlas de menor a mayor para orden alfabetico
    print("Paises ordenados alfabeticamente")

#?Debe comparar poblacion y ordenarlos de menor a mayor
    print("Paises ordenados por poblacion")

#?Debe comparar superficie de paises y ordenar de menor a mayor
    print("Paises ordenados por superficie")

def ver_estadisticas():
    print("Estadisticas")
#?Debe comparar poblacion de paises y mostrar los dos extremos [0] y [-1]
    print("Estadisticas: pais con mayor y menor poblacion")
#?Debe sumar la superficie de todos los paises y realizar promedio
    print("Estadisticas: promedio de superficie")
#?Debe verificar cuantos paises comparten continente y mostrarlo
    print("Estadisticas: cantidad de paises por continente")

def ver_paises():
#?Debe mostrar los paises cargados en el archivo
    print("Paises")

def salir():
#?Cierra el programa
    print("Se cerro el programa")


#--Funciones auxiliares

#**Funciones de validacion de inputs
#Validacion de nombre de pais. La funcion recibe 2 argumentos:
#datos: es la lista que contiene los diccionarios con la informacion de los paises
#verificar_duplicado: argumento a modo de bandera para determinar si se evalua o no la existencia del nombre del pais dentro de datos
def validar_nombre_pais( datos, verificar_duplicado ):
#Ciclo while para pedir el dato al usuario hasta que ingrese uno valido
    while True:
        try:
            nuevo_pais = input("Ingrese nombre del país que desea añadir: ").strip().title()
#Valida que se hay ingresado algo por teclado
            if len(nuevo_pais) == 0:
                raise ValueError("Debe ingresar el nombre del país que desea añadir.\n")
#Impone un minimo de caracteres para el nombre del pais
            elif len(nuevo_pais) < 3:
                raise ValueError("El largo del nombre del nuevo país no puede ser inferior a 3 caracteres\n")
#Impone un maximo de caracteres para el nombre
            elif len(nuevo_pais) > 60:
                raise ValueError("El largo del nombre del país no puede superar los 60 caracteres\n")
#Emite error en caso de que se hayan incluido numeros en el nombre
            elif any(caracter.isdigit() for caracter in nuevo_pais):
                raise ValueError("El nombre del país no puede contener números.\n")

#La funcion all() evalua caracter por caracter. Si un caracter incumple una de las condiciones dentro de all(),
#retornara False y el operador not, invertira el valor booleano a True,
#haciendo que se ingrese al bloque elif y dispare el error personalizado.
            elif not all( caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in nuevo_pais ):
                raise ValueError("El nombre del país no acepta caracteres especiales ( $, #, &, etc ).\n")
#Busca en archivo cvs la existencia del pais y genera el error si la encuentra
#Utiliza el valor del argumento "verificar_duplicado" solo si el flujo de ejecucion proviene de la invocacion de la funcion en la opcion 1
#Para la opcion 2, "verificar_duplicado" sera False, por lo que no realizara esta evaluacion
            elif verificar_duplicado and existe_pais_en_base_datos( nuevo_pais, datos ):
                raise ValueError("El país ya existe en la base de datos. No se permiten duplicados.\n")

            return nuevo_pais

        except ValueError as error:
            print(error)
            continue

#Validacion de la poblacion
def validar_poblacion_pais():
#Ciclo while para pedir el dato al usuario hasta que ingrese uno valido
    while True:
        try:

            poblacion_pais = input("Ingrese la población del país: ").strip()
#Valida que se hay ingresado algo por teclado
            if len(poblacion_pais) == 0:
                raise ValueError("Debe ingresar un dato numerico válido para la población del país.\n")
#Verifica que se este ingresando un numero entero
            elif not poblacion_pais.isdigit():
                raise ValueError("Dato ingresado inválido. Debe ingresar un número entero mayor o igual a 1.\n")
#Verifica que la poblacion sea al menos 1
            elif int(poblacion_pais) < 1:
                raise ValueError("La población de un país no puede ser un número inferior a uno\n")
#Impone limite de poblacion para el pais. evita que se ingresen numeros excesivos o absurdos )
            elif int(poblacion_pais) > 2000000000:
                raise ValueError("La población del país no puede superar los dos mil millones de habitantes\n")

            return poblacion_pais
        
        except ValueError as error:
            print(error)
            continue

#Validacion de la superficie
def validar_superficie_pais():
#Ciclo while para pedir el dato al usuario hasta que ingrese uno valido
    while True:
        try:

            superficie_pais = input("Ingrese la superficie en kilometros cuadrados del país: ").strip()
#Verifica que se haya ingresado algo por teclado
            if len(superficie_pais) == 0:
                raise ValueError("Debe ingresar un dato numerico válido para la superficie del país.\n")

#Verifica que la superficie en km2 sea un numero. 
#Implementa float porque puede ser un numero con decimales ( ej: Ciudad del Vaticano 0.44 mk2 )
            try:
                numero = float(superficie_pais)
            except ValueError:
                raise ValueError("Dato ingresado inválido. Debe ingresar un número para este campo.\n")
            if numero <= 0:
                raise ValueError("La superficie en kilometros cuadrados del país debe ser un valor mayor a cero\n")
#La superficie en km2 no puede ser menor o igual a cero. Emite error

            return superficie_pais
        
        except ValueError as error:
            print( error )
            continue

#Validacion del continente
def validar_continente_pais():
#Lista con los nombres de los continentes validos
    continentes_validos = [ "America", "Europa", "Asia", "Africa", "Oceania", "Antartida", "América", "África", "Antártida", "Oceanía" ]

#Ciclo while para pedir el dato al usuario hasta que ingrese uno valido
    while True:
        try:
            nuevo_continente = input("Ingrese nombre del continente en el cual se encuentra el país que desea añadir: ").strip().capitalize()

            if len( nuevo_continente ) == 0:
                raise ValueError("Debe ingresar el nombre del contintente al que pertenece el país.\n")

#La funcion all() evalua caracter por caracter. Si un caracter incumple una de las condiciones dentro de all(),
#retornara False y el operador not, invertira el valor booleano a True,
#haciendo que se ingrese al bloque elif y dispare el error personalizado.
            elif not all( caracter.isalpha() or caracter.isspace() or caracter in "'-" for caracter in nuevo_continente ):
                raise ValueError("El nombre del continente no acepta números ni caracteres especiales ( $, #, &, etc ).\n")

            elif nuevo_continente not in continentes_validos:
                raise ValueError(f"No se encontraron coincidencias para '{ nuevo_continente }'. Ingrese un continente válido.\n")

            return nuevo_continente

        except ValueError as error :
            print( error )

#Verifica si existen coincidencias de nombres en el archivo csv. Recibe 2 argumentos
#pais: es el nombre del pais que ingreso el usuario
#datos: es la lista que contiene los diccionarios con la info de los paises
def existe_pais_en_base_datos( pais, datos ):

#Variable bandera, si se encuentra coincidencia entre nombres de paises cambia a true y se retorna al final de la funcion
    existe_pais = False

#Bucle for recorrera la lista datos que almacena los diccionarios que guardan los datos de los paises
#Comparara los valores de las llaves "nombre" dentro de los diccionarios hasta encontrar coincidencia o terminar de recorrer la lista 
    for pais_en_base_datos in datos:
#Si encuentra coincidencia significa que el nombre ya existe en el archivo csv. Cambia la bandera a true y rompe el bucle
        if pais_en_base_datos["nombre"] == pais:
            existe_pais = True
            break

#Retorna False si no se encontraron coincidencias, retorna True si ya existe el nombre
    return existe_pais

















if __name__ == "__main__":
    iniciar_programa()

