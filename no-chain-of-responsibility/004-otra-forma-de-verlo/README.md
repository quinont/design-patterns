# Ampliando la Cafetería

Continuamos con los mismos productos de antes.

Ahora tenemos:

- Café simple
- Café con leche
- Mocha
- Leche sola
- Café con canela

## El Código

Esta vez, queremos darle un giro al código, porque conforme la cafetería crezca, también crecerá la complejidad del menú.

Lo importante es que:

- Si un cliente pide algo que no tenemos, le avisemos amablemente.
- A medida que se preparan los pedidos, se vayan mostrando los pasos (“Agregando café”, “Agregando leche”, etc.).
- Al final, mostremos el resultado completo del pedido, como “Café Mocha preparado”.

## La Solución: Patrón de Diseño Cadena de Responsabilidad

Para organizar mejor el código y hacerlo más manejable, usaremos el patrón de diseño “Cadena de Responsabilidad”.

### Los Componentes del Patrón

1. **Solicitud:**

   - Esta será una clase que representa lo que el cliente quiere (por ejemplo, agregar café, leche o canela).
   - Además, lleva el estado del pedido, es decir, lo que ya se ha preparado hasta el momento.
   - En nuestro ejemplo, la llamaremos `CoffeeRequest`.

2. **Handler:**

   - Es una clase base (abstracta) que define un paso en el proceso. Por ejemplo, podría haber un `Coffee` para agregar café o un `Milk` para agregar leche.
   - Cada paso verifica si puede hacer algo con la solicitud y, si no puede, pasa la solicitud al siguiente handler.

3. **Factory:**

   - Para evitar código repetitivo, la “fábrica” nos ayudará a construir la solicitud inicial de manera sencilla.

### Ejemplo: Preparar un Mocha

Imagina que alguien pide un Mocha. El proceso sería algo como:

- La solicitud llega al `Coffee`, que agrega café.
- Luego pasa al `Milk`, que agrega leche.
- Después pasa al `Chocolate`, que agrega chocolate.
- Cuando llega al `Cinnamon`, como el Mocha no lleva canela, simplemente pasa al siguiente handler (y como es el último, devuelve el `CoffeeRequest`).
- Finalmente, el pedido completo se devuelve al cliente.

### Diagrama de Clases

Así es como luce la estructura de nuestro código:

![Diagrama de Clases](img/class.png)

### Diagrama de Secuencia

Y aquí está cómo interactúan las diferentes piezas cuando preparamos un café:

![Diagrama de Secuencia](img/seq.png)

## Conclusión

Con este enfoque:

- Podemos agregar nuevos ingredientes o tipos de café sin complicar mucho el código existente, facilitando el principio de Open-Closed.
- El flujo de preparación es claro y fácil de seguir.
- Siguiendo el patrón de diseño Cadena de Responsabilidad, tenemos un sistema flexible y escalable que crece junto con nuestra cafetería.
- Además, cada `Handler` se enfoca exclusivamente en su responsabilidad, cumpliendo con el principio de responsabilidad única.

