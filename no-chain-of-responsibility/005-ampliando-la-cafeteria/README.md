# Endulzando el Café

Hasta ahora los ingredientes siempre fueron buenos, de excelente calidad, pero faltaba algo importante: ¡endulzantes!

Por lo tanto, ahora todos los cafés de la cafetería tienen un ingrediente más, algo que los vuelve más dulces.

Pero como sobre gustos no hay nada escrito, el endulzado no es solo endulzado, tenemos variedad para que los clientes puedan seleccionar cómo endulzar sus cafés.

## Tipos de Endulzantes

- Azúcar normal, para los clásicos.
- Azúcar rubia, para quienes quieren sobresalir.
- Stevia, para las personas fit.

Dependiendo del tipo de endulzante, el proceso cambia, ya que cada uno tiene una forma particular de ser agregado:

- **Azúcar normal:** Batido normal.
- **Azúcar rubia:** Un batido más fuerte.
- **Stevia:** No requiere batido.

## El Código

Dado que ya usamos el patrón de diseño de "Cadena de Responsabilidad", la idea es simplemente sumar un elemento más a la cadena: la parte de "endulzar".

Sin embargo, como cada tipo de endulzante requiere un tratamiento distinto, aquí entra en juego otro patrón de diseño: el **Patrón Estrategia**.

La principal ventaja del patrón Estrategia es que nos permite elegir, en tiempo de ejecución, la manera en que vamos a trabajar. Esto es útil porque solo sabemos cuál será el tipo de endulzante cuando el programa esté corriendo, por lo que este patrón nos da una forma completamente flexible de decidir qué hacer.

Para facilitar la elección de la estrategia y no atar el handler de endulzamiento a una estrategia en concreto, generamos una vez más un factory que flexibiliza la selección de la estrategia partiendo del nombre del endulzante.

### Diagrama de Clases

Así es como luce la estructura de nuestro código:

![Diagrama de Clases](img/class.png)

### Diagrama de Secuencia

Y aquí está cómo interactúan las diferentes piezas cuando preparamos un café:

![Diagrama de Secuencia](img/seq.png)

## Conclusión

Para ir cerrando, la idea principal es mostrar cómo los patrones de diseño se complementan entre sí. Aunque un patrón sea el "principal", podemos agregar más patrones y combinarlos para que el código sea más fácil de extender y mantener.

Si en el futuro aparece otro tipo de endulzante que requiera una forma particular de batir, simplemente agregamos otra estrategia.

Es importante destacar que crear un handler de "endulzar" es solo una forma de estructurar el código. También era posible generar tres handlers distintos, uno para cada tipo de endulzante con su batido correspondiente. La agrupación se dio porque consideramos "endulzar" como un único paso de la cadena. Lo esencial es entender cómo trabajan las personas en el contexto del sistema: ¿endulzar es un paso más o cada endulzante tiene un proceso completamente diferente?

No existe un camino perfecto. Siempre habrá ventajas y desventajas. Lo importante es conocerlas, entenderlas y aceptarlas.