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
para la solución a este reto, se creo una bd respetando la estructura planteada anteriormente, el archivo [a relative link](database_apalabrados.sql) contiene el codigo usado para el desarrollo de esta bd en MSSQLS SERVER
