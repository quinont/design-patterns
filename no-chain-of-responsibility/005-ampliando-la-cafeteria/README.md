# Endulzando el Café

Hasta ahora, nuestros cafés siempre tuvieron ingredientes de excelente calidad, pero sentíamos que les faltaba algo importante: ¡un toque dulce!

Por eso, ahora todos los cafés de la cafetería tienen un ingrediente más, algo que los hace más dulces y personalizables. Eso sí, como sobre gustos no hay nada escrito, los clientes pueden elegir entre una variedad de endulzantes. 

## Tipos de Endulzantes

- **Azúcar normal**: Para los clásicos que no se complican.
- **Azúcar rubia**: Para quienes quieren sobresalir (y tienen onda).
- **Stevia**: Para las personas fit que no se saltan el gym ni un día.

Cada endulzante tiene su propio estilo al ser agregado:

- **Azúcar normal:** Batido normal, sin estrés.
- **Azúcar rubia:** Un batido más intenso para que se mezcle bien.
- **Stevia:** Se agrega sin batido (sí, ¡es así de simple!).

---

## ¿Cómo lo hacemos?

Ya usamos el patrón de diseño "Cadena de Responsabilidad" para manejar los pasos en la preparación del café. Ahora, para endulzar, necesitamos más flexibilidad porque cada tipo de endulzante tiene un proceso único. Aquí es donde entra en acción el **Patrón Estrategia**.

El patrón Estrategia nos permite elegir dinámicamente la forma de agregar el endulzante en tiempo de ejecución. 

Para facilitar esta elección y no acoplar directamente el handler de "endulzar" a una estrategia específica, utilizamos un **Factory** que selecciona la estrategia correcta a partir del tipo de endulzante.

### Diagrama de Clases

La estructura de clases queda más o menos así:

![Diagrama de Clases](img/class.png)

### Diagrama de Secuencia

El flujo de interacción entre las piezas al preparar un café es este:

![Diagrama de Secuencia](img/seq.png)

---

## Conclusión

La clave es que los patrones de diseño no son exclusivos; pueden (y deben) complementarse entre sí. Aquí combinamos la Cadena de Responsabilidad con el Patrón Estrategia para lograr un código flexible y escalable. 

Si en el futuro aparece otro endulzante con su propio método de batido (¡o sin batido!), solo tenemos que agregar otra estrategia. Sin cambios drásticos en el resto del código.

Por cierto, crear un único handler de "endulzar" fue nuestra decisión porque consideramos "endulzar" como un paso único. Pero otra opción habría sido generar un handler por cada tipo de endulzante. Ambas son válidas; lo importante es entender cómo funciona en el contexto del sistema.

No hay un camino perfecto, pero lo esencial es conocer las opciones, sus ventajas y desventajas, y elegir el mejor para el caso.

## Nota Final

Hay algo que comienza a generar ruido en el diseño actual: la relación entre `main()` y `make_coffee()`. Actualmente, `make_coffee()` también se encarga de generar los pedidos (`request_coffee`), lo que crea un acoplamiento fuerte entre las funciones. Esto sugiere que quizá la responsabilidad de crear los pedidos debería trasladarse a `main()`, reduciendo así el acoplamiento.

### ¿Qué otros ejemplos de acoplamiento detectamos?

Revisa el codigo y mira si puedes encontrar algun otro acoplamiento.

---

## Próximo Paso  

Ya no hay mas ejemplos, pero hay un par mas de ejercicios que se pueden hacer en la parte de [006-mas-para-practicar](../006-mas-para-practicar).