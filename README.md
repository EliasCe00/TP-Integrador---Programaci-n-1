# Sistema de Gestión de Países

## Descripción

Sistema desarrollado en Python para la gestión de información de países mediante una interfaz de consola.

La aplicación permite registrar nuevos países, actualizar información existente, buscar registros, aplicar filtros, ordenar resultados y obtener estadísticas sobre los datos almacenados.

La información se almacena de forma persistente en un archivo CSV y se carga en memoria RAM al iniciar el programa para facilitar su manipulación.

---

## Link a video explicativo en Youtube

www.youtube.com

## Funcionalidades

- Añadir países a la base de datos.
- Actualizar población y superficie de países existentes.
- Buscar países por nombre.
- Filtrar países por continente.
- Filtrar países por rango de población.
- Filtrar países por rango de superficie.
- Ordenar países alfabéticamente.
- Ordenar países por población.
- Ordenar países por superficie.
- Consultar estadísticas generales.

---

## Estructura del directorio del proyecto

```text
TP-Integrador---Programacion-1

main.py

data/
    paises.csv

funciones/
    __init__.py
    funciones_del_menu.py
    funciones_auxiliares.py
```

---

## Requisitos

- Python 3.10 o superior.
- No se requieren librerías externas.

El proyecto utiliza únicamente módulos incluidos en la biblioteca estándar de Python.

---

## Instrucciones de uso

1. Abrir una terminal en la carpeta raíz del proyecto.
2. Ejecutar el siguiente comando:

        python main.py

3. Seleccionar una opción del menú principal.
4. Seguir las instrucciones mostradas en pantalla.

---

## Menú principal

```text
---- Gestión de Datos de Países ----

1. Añadir país a la base de datos.
2. Actualizar datos (Población y Superficie).
3. Visualizar información sobre países.
4. Filtrar países (Continente, población o superficie).
5. Ordenar países.
6. Ver estadísticas.
7. Salir
```

---

## Ejemplos de uso

### Ejemplo 1: Añadir un país

**Entrada**

```text
Ingrese nombre del país: Argentina
Ingrese la población del país: 47000000
Ingrese la superficie en kilometros cuadrados del país: 2780400
Ingrese nombre del continente en el cual se encuentra el país que desea añadir: America
```

**Salida**

```text
Se añadió con éxito el país 'Argentina' con la siguiente información:

Poblacion: 47000000
Superficie en kilometros cuadrados: 2780400
Continente: America
```

---

### Ejemplo 2: Buscar un país

**Entrada**

```text
Ingrese nombre del país: Argentina
```

**Salida**

```text
País encontrado con éxito:

Nombre: Argentina
Poblacion: 47000000
Superficie: 2780400
Continente: America
```

---

### Ejemplo 3: Validación de datos

**Entrada**

```text
Ingrese la población del país: abc
```

**Salida**

```text
Dato ingresado inválido. Debe ingresar un número entero mayor o igual a 1.
```

---

## Formato del archivo CSV

El archivo `paises.csv` debe respetar la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,47000000,2780400,America
Brasil,215000000,8515767,America
Chile,19600000,756102,America
```

---

## Validaciones implementadas

### Nombre del país

- No puede estar vacío.
- Debe contener entre 3 y 60 caracteres.
- No puede contener números.
- No puede contener caracteres especiales no permitidos.
- No se permiten países duplicados.

### Población

- Debe ser un número entero.
- Debe ser mayor o igual a 1.
- No puede superar los 2.000.000.000 habitantes.

### Superficie

- Debe ser un valor numérico.
- Puede contener decimales.
- Debe ser mayor que cero.

### Continente

- Debe coincidir con uno de los continentes válidos definidos por el sistema.

---

## Participación de los integrantes

### Jeremías Juárez

- Desarrollo del sistema
- Diseño inicial del programa
- Documentación del proyecto
- Modularización

### Elías Ceballos

- Creacion de repositorio
- Desarrollo del sistema
- Documentación del proyecto
- Modularización

## Tecnologías utilizadas

- Python 3
- Módulo CSV de la biblioteca estándar de Python
