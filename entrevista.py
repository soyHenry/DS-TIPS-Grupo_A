Preguntas teoricas:
1)¿Cuál es la diferencia entre la lista y tupla?

Una lista puede ser alterada, no así una tupla. 
Una tupla puede ser utilizada como clave en un diccionario, no así una lista.
Una tupla consume menos espacio que una lista.

2)¿Cuántos tipos de datos nativos existen en el lenguaje Python?

El lenguaje Python posee cinco tipos diferentes de datos: 
	1.string
	2.lista
	3.número
	4.diccionario
	5.tuple

3)¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que seria la lista 1 [-1]?
"-1" siempre se refiere al último índice de la lista, por lo tanto la respuesta seria 3.


Practico: 
Escribe un código que dado un numero entero positivo ingresado por teclado sume/reste los numeros hasta el 0 (cero) teniendo en cuenta estas consideraciones:
*Si el numero es par, suma
*Si el numero es impar, resta

Informar el valor final y la lista de numeros pares ordernados

Ejemplo: 
Numero ingresado = 5

5--> resta 
4--> suma
3--> resta
2--> suma
1--> resta
valor final (-3) Se forma por (-5 +4 -3 +2 -1) 

El programa debe devolver  (-3) y [2,4]

n=int(input("Cantidad de numeros: ")) #Cant de numeros a sumar
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
