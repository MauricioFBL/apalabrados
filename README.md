# Apalabrados
Primer reto técnico platzi master, Es una aplicacion en Flask que evalua un input
Para este reto se debe crear una DB con las siguientes tablas:
- numeros. Columnas: número, acumulado
- texto. Columnas: texto, inicial, final
- caracteres: Columnas: caracter

Despues de tener la BD se creara una aplicacion que analice un input y de acuerdo al tipo de datos haga lo siguiente:

- Si es un número, lo guarda en la tabla numeros. En la columna número guardará el input y acumulará el valor con los valores anteriores de la misma tabla, este se almacenará en acumulado.
- Si es un texto, debe almacenar en la tabla texto. Guarda el input en la columna  texto, el caracter inicial se guarda en la columna inicial y el caracter final se guarda  en la columna final.
- Si el input tiene algún caracter especial como tilde, coma, punto y coma, punto,  numeral o parecidos, debe extraerlo del input y enviar el caracter a la tabla  caracteres, columna caracter. El resto del input se descarta.

## Solución
para la solución a este reto, se creo una bd respetando la estructura planteada anteriormente, el archivo [database_apalabrados.sql](database_apalabrados.sql) contiene el codigo usado para el desarrollo de esta bd en MSSQLS SERVER.
Una vez que la base de datos fue correctamente creada se creo un login y un usuario con permisos de insecion y consulta

Para el desarrollo de la aplicacion el primer punto trabajado fue la conexion a la base de datos que se puede ver en el archivo [db_connection.py](db_connection.py) que hace uso de pyodbc para obtener una conexion con el usurio, para el funcionamiento de esta conexion es necesarion archivo ".env" con la variables de conexion a la bd la estructura de dicho puto en se puede revisar en [.env.example](.env.example)

En cuanto a la logica que evalua el input dado por el usuario se encuentra en [apalabrados.py](apalabrados.py) basicamente aqui se evalua y hacen los llamdos a la bd las reglas queevaluan el input son las siguentes.
- Se intenta convertir el input en un numero, si no hay erros entonces se convierte en numero, y si hay un error es un texto
- Cuando se sabe que es un texto se hace un desglose caracter por caracter convirtiendolo a ascii y comparando con los rangos donde hay un carcater especial
- dependiendo de lo que pase en cada evaluacion sellama a una funcion que inserta lo que se especifica en el enunciado del reto

Por ultimo para la parte de la app se creo una aplicacion web en flask la cual se ejcuta mediante el archivo [run.py](run.py) el cual habilita un servidor que muestra la appp y manda el inputa a [apalabrados.py](apalabrados.py), tambien muestra lo que cada tabla tiene 
