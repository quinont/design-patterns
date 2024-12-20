# Ampliando la cafeteria

Continuamos con los mismos productos de antes

Ahora tenemos:
- Cafe simple
- Cafe con leche
- Mocha
- Leche sola
- Cafe con canela

## El codigo

La idea esta vez es darle otra mirada al codigo, esto va a ir creciendo de forma desproporcionada.

Como siempre, si no piden algo de eso, entonces hay que avisarles que no lo tenemos.

Es necesario ir mostrando las cosas que se van haciendo (ejemplo: "Agregando cafe") pero tambien al final de todo mostrar que se devuelve: "cafe".


## El resultado

La idea aqui es refactorizar el codigo siguiendo el patron de diseño de cadena de responsabilidad.

Primero, la solicitud se transforma en una clase que nos indica cual es el ingrediente que se quiere agregar y que tiene el resultado.

Segundo, se genera una clase abs Handler, la idea es que todos los pasos que agregan ingredientes partan a partir de esta clase.

Tercero, para facilitar la construccion de la solicitud se genero un factory.

Si, es necesario dividir esto en mas pasos.
