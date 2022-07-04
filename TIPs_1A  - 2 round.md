# TIPs - Grupo A - Entrevista n°2 


## Preguntas teoricas:


* Pregunta 1: ¿Qué es una vista?

* Pregunta 2: ¿Sabes qué es una Primary Key?

* Pregunta 3: Explicar qué es una Unique Key.

* Pregunta 4: ¿Puedes decir que los valores NULL equivalen a cero?

* Pregunta 5: Se puede crear una tabla vacía a través de una existente?

* Pregunta 6: Como se puede selecciona un registro único de la tabla. 

* Pregunta 7 ¿Cómo recuperarías los primeros 3 caracteres de una cadena de caracteres?

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
