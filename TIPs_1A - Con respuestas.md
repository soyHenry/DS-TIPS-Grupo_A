# TIPs - Grupo A - Entrevista n°1

Recuerden que esto es una herramienta para practicar como seria una entrevista real<br>
Bajo ningun punto de vista queremos su compañero pase un mal momento, es simplemente guiarlo a traves de las preguntas<br>
Esto tampoco quiere decir que hay que darle las respuestas facilmente, se lo puede aconsejar, se lo puede guiar o incluso darle pistas

## Preguntas teoricas:
### 1)¿Cuál es la diferencia entre la lista y tupla?

Una lista puede ser alterada, no así una tupla. 
Una tupla puede ser utilizada como clave en un diccionario, no así una lista.
Una tupla consume menos espacio que una lista.

### 2)¿Cuántos tipos de datos nativos existen en el lenguaje Python?

El lenguaje Python posee cinco tipos diferentes de datos: 
	1.string
	2.lista
	3.número
	4.diccionario
	5.tuple

### 3)¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que seria la lista 1 [-1]?
"-1" siempre se refiere al último índice de la lista, por lo tanto la respuesta seria 3.


## Practico: 
Escribe un código que dado un numero entero positivo ingresado por teclado sume/reste los numeros hasta el 0 (cero) teniendo en cuenta estas consideraciones:<br>
*Si el numero es par, suma<br>
*Si el numero es impar, resta<br>

Informar el valor final y la lista de numeros pares ordernados<br>

Ejemplo: <br>
Numero ingresado = 5<br>

5--> resta <br>
4--> suma<br>
3--> resta<br>
2--> suma<br>
1--> resta<br>
valor final (-3) Se forma por (-5 +4 -3 +2 -1) <br>

El programa debe devolver  (-3) y [2,4] <br>

```
n=int(input("Cantidad de numeros: "))  
suma = 0 #inicializo la suma
par=[]
impar=[]
while n > 0:
   if n % 2 == 0:
    suma = suma + n
    par.append(n)
   else:
    suma = suma -n 
   n = n -1
   par.sort()
print(suma)
print(par)
```
