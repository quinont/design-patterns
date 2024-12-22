# Ampliando la Cafetería: Ejercicios para Practicar  

¡Enhorabuena! Hemos recorrido un largo camino explorando patrones de diseño aplicados al ejemplo de una cafetería virtual. Vimos cómo implementar patrones como **Factory**, **Cadena de Responsabilidad**, y **Estrategia**, y logramos un código más limpio y modular.  

Ahora, la pelota está en tu cancha. Si quieres seguir practicando y mejorar tu entendimiento de estos conceptos (y de paso, convertirte en el *barista* del código), aquí tienes algunos ejercicios para seguir ampliando la cafetería.  

---

## Ejercicios para Ampliar el Código  

Todos los ejercicios son incrementales: la idea es resolverlos uno a la vez y en orden, construyendo sobre lo que ya tienes. ¡Vamos por partes!  

### 1. **Agregar un Nuevo Ingrediente**  

El café es versátil, y nuestra cafetería debería ser igual. Agrega más opciones de ingredientes, como:  
- Miel  
- Jengibre  
- Nuez moscada  
- Vainilla  
- Hielo  

**Recomendación:**  
- Crea nuevos handlers en tu cadena de responsabilidad para manejar estos ingredientes.  
- Asegúrate de que los ingredientes se agreguen en el orden correcto.  

---

### 2. **Café Personalizado**  

Actualmente, el cliente solo puede pedir opciones predefinidas del menú. Cambia esto para que pueda construir su café paso a paso, eligiendo los ingredientes que prefiera, o seguir con los cafe "pre hechos".  

**Pistas:**  
- Implementa un sistema de selección donde el usuario elija los ingredientes desde la consola.  
- Haz que cada ingrediente seleccionado pase por la cadena de responsabilidad para su preparación.  

---

### 3. **Separar el Código en Archivos**  

Tener todo el código en un único archivo puede ser cómodo al principio, pero pronto se vuelve difícil de manejar. Divide el código en módulos bien organizados.  

**Sugerencia:**  
- Crea archivos separados para los handlers, la solicitud (`CoffeeRequest`), y cualquier lógica auxiliar (como la fábrica).  
- Usa una estructura de carpetas que refleje las responsabilidades de cada componente.  

---

### 4. **Quitar los `print` del Código**  

Aunque los `print` son útiles para depuración, no son la mejor práctica. Deleguemos esta tarea a un sistema de registro (logging).  

**Pasos a seguir:**  
- Investiga el módulo `logging` de Python.  
- Reemplaza los `print` con llamadas a `logger.info()` o similares.  
- Crea diferentes niveles de log (info, warning, error) para mayor flexibilidad.  

---

### 5. **Control de Stock**  

¿Qué tal si llevamos un control del inventario de nuestra cafetería?  

**Objetivos:**  
- Cada ingrediente tiene una cantidad inicial (por ejemplo, 10 unidades).  
- A medida que se preparan pedidos, el stock se reduce.  
- Al final del día, genera un reporte de los ingredientes usados y cuáles necesitan ser reabastecidos.  

---

### 6. **Crear una Interfaz Web**  

La línea de comandos está bien, pero... ¡es hora de modernizarse! Implementa una interfaz web sencilla usando un framework de Python como Flask o Django.  

**Ideas:**  
- Crea un formulario donde el usuario pueda seleccionar ingredientes.  
- Muestra un resumen del pedido antes de procesarlo.  
- Implementa un botón para preparar el café y devuelve el resultado en la página.  

---

## Mensaje Final  

¡Gracias por haber llegado hasta aquí! Este curso es solo el inicio de lo que puedes lograr aplicando patrones de diseño en Python. Recuerda, escribir buen código no se trata solo de resolver problemas, sino de hacerlo de manera que otros puedan entender, ampliar y mantener tu trabajo.  

Si tienes ideas o mejoras para este ejemplo, no dudes en hacer un **Pull Request**. ¡Estamos siempre abiertos a sugerencias y nuevas formas de ampliar este proyecto!  

**¡Nos vemos en el siguiente café! ☕**
