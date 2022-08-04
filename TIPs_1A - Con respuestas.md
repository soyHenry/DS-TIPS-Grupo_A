# TIPs - Grupo A - Entrevista n°1

Recuerden que esto es una herramienta para practicar como seria una entrevista real<br>
Bajo ningun punto de vista queremos su compañero pase un mal momento, es simplemente guiarlo a traves de las preguntas<br>
Esto tampoco quiere decir que hay que darle las respuestas facilmente, se lo puede aconsejar, se lo puede guiar o incluso darle pistas

## Preguntas teoricas:
### 1)¿Qué es un diccionario en Python? ¿Cómo podemos acceder a su contenido?

Es uno de los distintos tipos de datos nativos en Python. Definen la relación uno a uno entre una clave (en inglés "key") y un valor asociado (en inglés "value"). El diccionario contiene los pares
asociados de claves y valores correspondientes. Están indexados por las claves.
Para obtener sus contenidos, podemos acceder a ellos utilizando métodos asociados a diccionarios,
el método .keys() devuelve todas las claves del diccionario, el método .values() devuelve todos 
los valores del diccionario y el método .items() devuelve tuplas con la estructura ("llave","valor").

### 2)¿Con qué métodos puedo agregar nuevos elementos a una lista en Python?

Para agregar elementos a una lista en Python es posible utilizar el método .append(), el cual agrega elementos al final de la lista, o bien utilizar el método .insert() que agrega un elemento en un 
índice espeficificado, por ejemplo lista.insert(1, 'manzana') insertaría en el índice 1, el elemento 'manzana' sin reemplazar ningún valor original. Por último, el método .extend() une cualquier 
iterable u otra lista a la lista original, desde el final de la lista original

### 3)¿Si la lista_1 es [9, 7, 2, 4, 5, 6], que seria la lista_1 [-6]?
Con números negativos, el valor del índice refiere desde el último índice de la lista, el -1 sería el último valor, "6", por lo tanto la respuesta seria "9".


## Practico: 
Crea un traductor simple que cambie las palabras masculinas de una frase por su versión neutra. Debe ser simple, rústico, se puede realizar completando el siguiente código para reemplazar todas 
las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e', 'x' o bien un @ (sólo 1 opción). Por ejemplo 'todos somos Henry' pasaría a ser 'todes somes Henry' 
o bien 'tod@s som@s Henry' o 'todxs somxs Henry.:<br>

Probala con 'Nosotros estudiamos Data' y con 'Los otros estudian para Fullstack', cambiando el string que está en la variable frase.


frase = 'todos somos Henry'
palabras = frase.split()
traduccion = []

for palabra in palabras:
        if ?
        ...
        
frase_t = ?

print(frase_t)
'todes somes Henry'


### Resolución propuesta

palabras = frase.split()<br>
nueva_palabra = ""<br>
traduccion = []<br>

for palabra in palabras:<br>
    if  palabra[-1:] == "o":<br>
        nueva_palabra = palabra[:-1] + "e"<br>
    elif len(palabra) > 1 and palabra[-2] == "o": # si tiene mas de 1 letra, busco la palabra en -2 para evitar errores si hay palabras de una sola letra. en Python evalua la primera y si es falsa, deja de evaluar (lazy evaluation).<br>
        nueva_palabra = palabra[:-2] + "e" + palabra[-1]<br>
    else:<br>
        nueva_palabra = palabra<br>
    traduccion.append(nueva_palabra)<br>
    #print(palabra, nueva_palabra)<br>

frase_t = " ".join(traduccion)<br>

print(frase_t)<br>
