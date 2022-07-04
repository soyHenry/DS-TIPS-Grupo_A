# TIPs - Grupo A - Entrevista n°2 

Recuerden que esto es una herramienta para practicar como seria una entrevista real<br>
Bajo ningun punto de vista queremos su compañero pase un mal momento, es simplemente guiarlo a traves de las preguntas<br>
Esto tampoco quiere decir que hay que darle las respuestas facilmente, se lo puede aconsejar, se lo puede guiar o incluso darle pistas

## Preguntas teoricas:


* Pregunta 1: ¿Qué es una vista?
Una vista es simplemente una representación virtual de una tabla.
 Además, las vistas pueden tener los datos de más de una tabla representados y combinados - dependerá mucho de la situación y la relación.

* Pregunta 2: ¿Sabes qué es una Primary Key?
Primary Key, es una columna o conjunto de columnas que identifican de manera única cada fila de la tabla.

* Pregunta 3: Explicar qué es una Unique Key.
Unique Key, es lo que identifica de manera única una sola fila en la tabla como se mencionó anteriormente en la explicación de Primary Key.

* Pregunta 4: ¿Puedes decir que los valores NULL equivalen a cero?
No, no puedes.
Un ¨cero¨ tiene una forma numérica, mientras que NULL significa la inexistencia de un carácter, ya sea porque es desconocido o no está disponible. Siguiendo la misma lógica. NULL tampoco es lo mismo que un espacio en blanco, es simplemente un carácter.

* Pregunta 5: Se puede crear una tabla vacía a través de una existente?
Si.
Este sería un ejemplo de cómo hacerlo:

Select * into employeecopy from employee where 1=2

* Pregunta 6: Como se puede selecciona un registro único de la tabla. 
La manera en la que seleccionas registros únicos de una sola tabla es utilizando el comando ¨distinct¨. Aquí tienes un ejemplo:

Select DISTINCT employeeID from Employee

Se podria llegar al mismo resultado con un group by? Si

* Pregunta 7 ¿Cómo recuperarías los primeros 3 caracteres de una cadena de caracteres?
Existen varias maneras de hacer eso, pero una de las más populares y fáciles es:

Select SUBSTRING(EmployeeSurname,1,5) as employeesurname from employee
# la palabra reservada SUBSTRING va a depender del motor, puede ser substr tambien

## Practico: 
#El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:


#1 Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
#2 Mostrar por pantalla los datos del pasajero con identificador 148.
#3 Mostrar por pantalla las filas pares del DataFrame.
#4 Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
#5 Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
#6 Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
#7 Mostrar por pantalla el porcentaje de cada sexo que sobrevivieron en primera clase.

import pandas as pd 
titanic = pd.read_csv('titanic.csv')

#1 Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
print('Dimensiones:', titanic.shape)
print('Número de elemntos:', titanic.size)
print('Nombres de columnas:', titanic.columns)
print('Nombres de filas:', titanic.index)
print('Tipos de datos:\n', titanic.dtypes)
print('Primeras 10 filas:\n', titanic.head(10))
print('Últimas 10 filas:\n', titanic.tail(10))

#2 Mostrar por pantalla los datos del pasajero con identificador 148
print(titanic.loc[148])

#3 Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(0,titanic.shape[0],2)])

#4 Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(titanic[titanic["Pclass"]==1]['Name'].sort_values())	

#5 Mostrar la edad media de las mujeres que viajaban en cada clase.
print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

#6 Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic['Young'] = titanic['Age'] < 18
