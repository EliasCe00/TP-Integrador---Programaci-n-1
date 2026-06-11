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
    print("Datos guardados")




def actualizar_datos_pais():
    print("Datos actualizados")

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



















if __name__ == "__main__":
    iniciar_programa()

