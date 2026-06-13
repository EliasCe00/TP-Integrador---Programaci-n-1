#--Funciones auxiliares

#**Funciones de validacion de inputs
#Validacion de nombre de pais. La funcion recibe 2 argumentos:
#datos: es la lista que contiene los diccionarios con la informacion de los paises
#verificar_duplicado: argumento a modo de bandera para determinar si se evalua o no la existencia del nombre del pais dentro de datos
def validar_nombre_pais( datos, verificar_duplicado ):
#Ciclo while para pedir el dato al usuario hasta que ingrese uno valido
    while True:
        try:
            nuevo_pais = input("Ingrese nombre del país: ").strip().title()
#Valida que se hay ingresado algo por teclado
            if len(nuevo_pais) == 0:
                raise ValueError("Debe ingresar el nombre del país.\n")
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
#Busca en la lista "datos" la existencia del pais y genera el error si la encuentra
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
            continue

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

