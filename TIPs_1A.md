# Checkpoint - Módulo 3

Cómo responder: <br>
* Cuando se pida una respuesta numérica, redondear al segundo decimal. <br>
   Ejemplo: 1.3421 -> 1.34;<br>
            1.8888 -> 1.89;<br>
            3 -> 3.00.<br>

## Responder Verdadero ó Falso

### 1) Un índice SQL es una tabla de búsqueda rápida para poder encontrar los registros que los usuarios necesitan buscar con mayor frecuencia.
Verdadero<br>
### 2) La regla de las 3 sigmas para detección de Outliers está basada en la Mediana.
Falso<br>
### 3) Las tablas Maestros registran las operaciones ocurridas, todo tipo de transacciones donde intervienen las diferentes entidades del modelo.
Falso<br>

## Elegir la opción correcta en base a la observación del siguiente DER:

<img src="DER.jpg"  height="400">

### 4) ¿Cuál de las siguientes no es una tabla que representa una dimensión?
   1- cliente<br>
   2- calendario<br>
   3- venta<br>
   4- provincia<br>
Rta = 3<br>
### 5) El DER presentado...
   1- es un Modelo Estrella, porque tiene una sóla tabla de hechos.<br>
   2- no es un Modelo Estrella, ya que contiene referencias circulares.<br>
   3- es un Modelo Copo de Nieve.<br>
Rta = 2<br>
## Resuelve los siguientes ejercicios:

### En tu motor de base de datos MySQL, ejecutá las instrucciones del script 'Checkpoint_Create_Insert.sql' (Si no trabajas con MySQL es posible que tengas que realizar algunos ajustes en el script. También están provistas las tablas en formato csv dentro de la carpeta 'tablas_cp').

### 6) La ganancia neta por sucursal es las ventas menos los gastos (Ganancia = Venta - Gasto) ¿Cuál es la sucursal con mayor ganancia neta en 2020? 
#### Elige la opción correcta:
   1- Alberdi<br>
   2- Flores<br>
   3- Corrientes<br>
Rta = 2<br>
### 7) La ganancia neta por producto es las ventas menos las compras (Ganancia = Venta - Compra) ¿Cuál es el tipo de producto con mayor ganancia neta en 2020?
#### Elige la opción correcta:
   1- Informática<br>
   2- Impresión<br>
   3- Grabacion<br>
Rta = 1<br>
### 8) Del total de clientes que realizaron compras en 2020 ¿Qué porcentaje lo hizo sólo en una única sucursal?
Rta = 0.34<br>
### 9) Del total de clientes que realizaron compras en 2020 ¿Qué porcentaje no había realizado compras en 2019?
Rta = 0.41<br>
### 10) Del total de clientes que realizaron compras en 2019 ¿Qué porcentaje lo hizo también en 2020?
Rta = 0.85<br>
### 11) ¿Qué cantidad de clientes realizó compras sólo por el canal OnLine entre 2019 y 2020?
Rta = 564<br>
### 12) ¿Cuál es la sucursal que más Venta (Precio * Cantidad) hizo en 2020 a clientes que viven fuera de su provincia?
#### Elige la opción correcta:
   1- Córdoba Quiroz<br>
   2- San Justo<br>
   3- Bariloche<br>
Rta = 1<br>
### 13) ¿Cuál fué el mes del año 2020, de mayor crecimiento con respecto al mismo mes del año 2019 si se toman en cuenta a nivel general Ventas (Precio * Cantidad) - Compras (Precio * Cantidad) - Gastos? 
#### Responder el Número del Mes:
Rta = 12<br>
### 14) Considerando que se requiere consultar las ventas por Rangos Etarios de Productos que corresponden a los tipos 'Estucheria', 'Informatica', 'Impresión' y 'Audio', hechas por Sucursales ubicadas en la Provincia de Buenos Aires durante la segunda mitad del año 2020 y a travéz del Canal de Venta OnLine.
#### Elegir la opción correcta en términos de desempeño o performance:
#Revisar este código en detalle porque da igual resultado el 2 y 3.
1)
```sql
Select	cl.Rango_Etario,
		   tp.TipoProducto,
        sum(v.Precio * v.Cantidad) as Venta
from 	venta v Join cliente cl
		On (v.IdCliente = cl.IdCliente)
	Join producto p
		On (v.IdProducto = p.IdProducto)
	Join tipo_producto tp
		On (p.IdTipoProducto = tp.IdTipoProducto)
	Join canal_venta cp
		On (cp.IdCanal = v.IdCanal)
	Join sucursal s
		On (s.IdSucursal = v.IdSucursal)
	Join localidad lo
		On (s.IdLocalidad = lo.IdLocalidad)
	Join provincia pr
		On (lo.IdProvincia = pr.IdProvincia)
Where 	Year(v.Fecha) = 2020
		   And Month(v.Fecha) >= 6
		   And cp.Canal = 'OnLine'
         And pr.Provincia = 'Buenos Aires'
         And TipoProducto In ('Estucheria','Informatica','Impresión','Audio')
Group by cl.Rango_Etario,
		tp.TipoProducto
Order by cl.Rango_Etario,
		Venta Desc;
```
2)
```sql
Select	cl.Rango_Etario,
		tp.TipoProducto,
        sum(v.Precio * v.Cantidad) as Venta
from 	venta v Join cliente cl
		On (v.IdCliente = cl.IdCliente
			And Year(v.Fecha) = 2020
            And Month(v.Fecha) >= 6)
	Join producto p
		On (v.IdProducto = p.IdProducto)
	Join tipo_producto tp
		On (p.IdTipoProducto = tp.IdTipoProducto
			And TipoProducto In ('Estucheria','Informatica','Impresión','Audio'))
	Join canal_venta cp
		On (cp.IdCanal = v.IdCanal
			And cp.Canal = 'OnLine')
	Join sucursal s
		On (s.IdSucursal = v.IdSucursal)
	Join localidad lo
		On (s.IdLocalidad = lo.IdLocalidad)
	Join provincia pr
		On (lo.IdProvincia = pr.IdProvincia
			And pr.Provincia = 'Buenos Aires')
Group by cl.Rango_Etario,
		tp.TipoProducto
Order by cl.Rango_Etario,
		Venta Desc;
```
3)
```sql
Select	cl.Rango_Etario,
		   tp.TipoProducto,
        sum(v.Precio * v.Cantidad) as Venta
from 	venta v Join cliente cl
		On (v.IdCliente = cl.IdCliente
			And Year(v.Fecha) = 2020
         And Month(v.Fecha) >= 6)
	Join producto p
		On (v.IdProducto = p.IdProducto)
	Join tipo_producto tp
		On (p.IdTipoProducto = tp.IdTipoProducto
			And TipoProducto In ('Estucheria','Informatica','Impresión','Audio'))
	Join canal_venta cp
		On (cp.IdCanal = v.IdCanal
			And cp.Canal = 'OnLine')
	Join sucursal s
		On (s.IdSucursal = v.IdSucursal)
	Join localidad lo
		On (cl.IdLocalidad = lo.IdLocalidad)
	Join provincia pr
		On (lo.IdProvincia = pr.IdProvincia
			And pr.Provincia = 'Buenos Aires')
Group by cl.Rango_Etario,
		tp.TipoProducto
Order by cl.Rango_Etario,
		Venta Desc;
```
Rta = 2<br>
### 15) El negocio suele requerir con gran frecuencia consultas a nivel trimestral tanto sobre las ventas, como las compras y los gastos...
#### Elige la opción correcta:
   1- Con los índices creados existentes, sólo sobre las claves primarias y foráneas, sería suficiente para cubrir cualquier necesidad de consulta.<br>
   2- Sería aduecuado colocar un índice sobre el campo trimestre de la tabla calendario aunque este no sea una clave foránea.<br>
   3- No se puede crear índices sobre campos que no son clave.<br>
Rta = 2<br> 

### Cada una de las sucursales de la provincia de Córdoba, disponibilizaron un excel donde registraron el porcentaje de comisión que se le otorgó a cada uno de los empleados sobre la venta que realizaron. Es necesario incluir esas tablas (Comisiones Córdoba Centro.xlsx, Comisiones Córdoba Quiróz.xlsx y Comisiones Córdoba Cerro de las Rosas.xlsx) en el modelo y contestar las siguientes preguntas:
### 16) ¿Cuál es el código de empleado del empleado que mayor comisión obtuvo en diciembre del año 2020?
Rta = 3875
### 17) ¿Cuál es la sucursal que menos comisión pagó en el año 2020?
#### Elige la opción correcta:
	1- Córdoba Centro.<br>
	2- Córdoba Quiroz.<br>
	3- Cerro De Las Rosas.<br>
Rta = 2
### 18) La ganancia neta por sucursal es las ventas menos los gastos (Ganancia = Venta - Gasto) ¿Cuál es la sucursal con mayor ganancia neta en 2020 en la provincia de Córdoba si además quitamos los pagos por comisiones? 
#### Elige la opción correcta:
   1- Córdoba Quiroz<br>
   2- Cerro De Las Rosas<br>
   3- Córdoba Centro<br>
Rta = 3
