#Importacion de funciones del menu
from funciones.funciones_del_menu import obtener_datos, grabar_datos_nuevo_pais, actualizar_datos_pais, buscar_pais_nombre, filtrar_paises, ordenar_paises, ver_estadisticas, salir

#Funcion para inciar el programa y visualizacion del menu
def iniciar_programa():

#Llamado de funcion obtener_datos() para tener disponible la informacion
    datos = obtener_datos()
#Menu de opciones
    while True:
        print("\n---- Gestión de Datos de Países ----\n")
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

#Opcion 2 - Actualizar datos de un pais
        elif opcion == 2:
            actualizar_datos_pais( datos )

#Opcion 3 - Visualizar informacion sobre un pais
        elif opcion == 3:
            buscar_pais_nombre( datos )

#Opcion 4 - Filtrar paises segun continente, poblacion o superficie
        elif opcion == 4:
            filtrar_paises(datos)

#Opcion 5 - Ordenar paises segun orden alfabetico, poblacion y superficie
        elif opcion == 5:
            ordenar_paises(datos)

#Opcion 6 - Ver estadisticas: Pais con mayor y menor poblacion, promedio de poblacion total, promedio superficie total, cantidad de paises por continente
        elif opcion == 6:
            ver_estadisticas(datos)

#Opcion 7 - Salir del programa
        elif opcion == 7:
            salir()
            break

#condicion para que sse llame a la funcion solo si se ejecuta directamente el archivo
if __name__ == "__main__":
    iniciar_programa()

