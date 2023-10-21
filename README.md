
# T2-02 Proyecto colaborativo de Git: Calculadora Básica

### Docente: Francisco Cervantes Zambrano

### Integrantes:

  Bazán Figueroa José María
  
  Calvario Martinez Missael de Jesús
  
  García Ramírez Fatima Guadalupe
  
  Partida Contreras Luis Emilio

## Introducción

Desarrollar una aplicación de calculadora simple que permita a los usuarios realizar operaciones matemáticas básicas, como suma, resta, multiplicación y división. La aplicación debe ser ejecutable desde la terminal de línea de comandos. Los usuarios deben poder ingresar dos números y seleccionar la operación que desean realizar mediante comandos simples

## Requisitos

-La aplicación debe aceptar dos números como entrada del usuario.

-Debe permitir al usuario elegir la operación deseada (suma, resta, multiplicación o división) utilizando comandos o argumentos en la línea de comandos.

-La aplicación debe realizar la operación seleccionada y mostrar el resultado en la terminal.

-Asegurarse de manejar casos de error, como la división por cero.

-La aplicación debe ser eficiente y proporcionar un código limpio y bien estructurado.

-Incluir un contenedor que permita ejecutar la aplicación en un entorno de ejecución seguro y controlado.

## CREACIÓN Y DESARROLLO DE CALCULADORA BÁSICA EN PYTHON

1. Nos organizamos en base a que lenguaje utilizariamos, nos decidimos por Python
2. Cada uno de los integrantes agarro una de las operaciones básicas de la calculadora:
   -Emilio: multiplicación
   -Misael: división
   -José María: suma
   -Fatima: resta
3. Emilio creó la base de la calculadora donde se juntará todos los metodós y códigos que vayamos creando y compartiendo cada uno
4. Emilio creó la rama dev para que ahí todos la bajaran y partieramos de ahí para poder cada uno empezar a programar con su operación
5. Cada uno bajó esa rama y tambien creó su propia rama
6. Cada uno dentro de su repectiva rama creo un metodo
7. Método el cual subimos mediante commit y ya que el proyecto estaba listo realizamos  el pull
8. Ya realizados y subidos cada método, Emilio realizo el merge desde el main para añadir nuestros metodos y terminó la calculadora
9. Para finalizar se creó un contenedor que permita ejecutar la aplicación de la calculadora

## Intrucciones de instalación, configuración y ejecución para poder utilizar el programa

1. para instalar ewl programa primero debemos bajar la imagen de docker
```sh
docker pull tdtxle/py_caluladora
```
3. Ejecutamos la imagen con el comando
```sh
docker run -it tdtxle/py_caluladora:2
```
