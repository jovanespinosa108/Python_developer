"""JSON es JavaScript Object Notation, Es un formato de texto simple 
que permite el intercambio de datos entre servicios y aplicaciones. 
no depende de ningún lenguaje de programación. 
Ventajas: sencillo, legible y fácil de entender tanto para el usuario 
como para los servicios que lo usan como comunicación, no requiere ser codificado 
para ser enviado o recibido entre servicios y su contenido representa uno o varios objetos. 
Se manejan diferentes tipos de datos, entre ellos encontramos:
cadenas de texto, datos numéricos tanto enteros como decimales, 
booleanos, valores de verdad verdadero y falso, datos nulos, 
arreglos o listas y objetos. 
Estructura: Una llaves {} que inicia y termina el contenido del objeto 
Dentro encontramos los elementos o características del objeto. 
Cada elemento tiene una llave y un valor definida entre comillas. 
Podemos tener valores de tipo cadena o string definidos entre comillas; 
valores numéricos enteros o decimal, 
valores booleanos, true o false, sin comillas y en minúscula; 
valores nulos, estos los escribimos como «null», indican que ningún valor se asignó a esa llave; 
valores de tipo lista, se definen entre corchetes y pueden contener elementos cuyo tipo sea soportado por el formato JSON. 
Este formato de texto lo usamos para el envío de datos entre servicios, 
pueden ser aplicaciones, servicios web, servidores, entre otros. 
Nos permiten almacenar datos de manera temporal. 
Se usa este formato para almacenar datos persistentes como variables de configuración de los programas que desarrollamos."""

"""//por convencion las llaves se escriben con doble ""
// las llaves se puden escribir en camell o snake format
// los arrays son como las listas en python
// el JSON complejo tambien se llaman listas o arreglos, y en estas cada elemento es un objeto
// Los Objetos son similares a los diccionarios en python que tiene una llave: valor"""


"""JSON como arreglo de elementos o de objetos que se guardan en una lista
[
    {
        "nombre": "Emilio"
    },
    {
        "entero": 56
    }
]"""

"""las llaves no deben repetirse, si se repiten cuando se corre JSON tomara el ultimo valor de llave definida

// Serializar y Deserializar
// Son para almacenar datos temporales o enviar y recibir información a través de servicios o servidores web.
// Serializar: Codificar JSON, Transforma los datos en bytes para ser enviados
// en Python se usa la funcion json.dumps()
// Deserializar: Decodifica un JSON, transforma los datos JSON recibidos al programa que se este usando
// en Python se usa la funcion json.loads()
// Tipos de datos python vs JSON:
// diccionario - objeto, lista/tupla - array, cadena de texto - string
// entero/decimal - number, True/False - true/false, none - null"""

