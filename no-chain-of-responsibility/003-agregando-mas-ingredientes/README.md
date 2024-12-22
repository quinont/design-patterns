# Más Cafetería, Más Café

¡La cafetería está que arde! Estamos escuchando cada vez más a nuestros clientes (y sus peticiones a veces un poco locas), así que decidimos expandir nuestro catálogo.  

¡Y vaya que nos fuimos para arriba! Ahora ofrecemos:  
- **Café simple**  
- **Café con leche**  
- **Mocha**  
- **Leche sola**  
- **Café con canela**  

Y como somos ambiciosos, esto no termina aquí. ¡El cielo es el límite (y también nuestra paciencia con los `if`)!

---

## El Código

Nuestro enfoque actual sigue siendo el mismo:  
1. Si piden algo que está en el menú, lo hacemos.  
2. Si no, les decimos con cortesía que no lo tenemos y seguimos adelante.  

Como siempre, mostramos el proceso (*"Agregando café"*, *"Agregando leche"*, etc.) y al final devolvemos un producto listo: *"café"*, *"mocha"*, o lo que corresponda.

Todo sigue concentrado en nuestro querido método `make_coffee` dentro de `main.py`. Hasta aquí todo bien, ¿cierto? Bueno... más o menos.

---

## El Resultado: ¿Por qué los `if` ya no son tan buenos amigos?

Aunque esta estrategia ha sido nuestra fiel compañera, las cosas comienzan a ponerse feas. Aquí van algunas desventajas importantes de esta metodología:  

1. **Código Inflado:** A medida que agregamos más productos, los `if` comienzan a acumularse como cuentas pendientes después de las vacaciones.  
   - ¿Qué pasa si añadimos 20 productos más? ¿50? ¿100? No solo se vuelve inmanejable, sino que leer el código empieza a sentirse como leer una novela épica... sin capítulos.  

2. **Mantenimiento Pesado:**  
   - Tener toda la lógica concentrada en un solo método es como tener todos los muebles de tu casa apilados en una sola habitación.  
   - ¿Qué pasa si alguien quiere modificar una lógica específica? Peor aún, ¿qué pasa si lo hacen dos desarrolladores al mismo tiempo? ¡Conflictos de Git para todos! 

3. **Dificultad para Escalar:**  
   - La lógica de los `if` funciona, pero no escala. Imagina tener que añadir una nueva bebida con 10 pasos de preparación. ¿Dónde metemos toda esa lógica?  
   - Y si quieres reutilizar algún paso, buena suerte encontrándolo entre todo ese código.  

4. **Error Humano:**  
   - Más código significa más oportunidades de cometer errores. Una simple línea mal colocada puede arruinar todo el flujo.  

En resumen: nuestra estrategia actual **grita por una refactorización urgente.**  

---

## ¿Qué sigue?

¡No todo está perdido! En el próximo episodio, vamos a implementar un patrón de diseño que nos ayudará a resolver estos problemas: **la Cadena de Responsabilidad**.  

Con este enfoque, podremos delegar responsabilidades de manera más clara, hacer que el código sea más legible, y escalar nuestra cafetería sin morir en el intento.  

Prepárate para el cambio en [004-otra-forma-de-verlo](../004-otra-forma-de-verlo).  

¡El café nunca será el mismo después de esto!
