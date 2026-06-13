#Importacion de funciones del menu
from funciones.funciones_del_menu import obtener_datos, grabar_datos_nuevo_pais, actualizar_datos_pais, buscar_pais_nombre, ordenar_paises, ver_estadisticas, ver_paises, salir

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

#Opcion 2 - Actualizar datos de un pais
        elif opcion == 2:
            actualizar_datos_pais( datos )

#Opcion 3 - Visualizar informacion sobre un pais
        elif opcion == 3:
            buscar_pais_nombre( datos )

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

#condicion para que sse llame a la funcion solo si se ejecuta directamente el archivo
if __name__ == "__main__":
    iniciar_programa()

