🗂️ IS2-PANIAGUA.GUSTAVO.C12025  
 ┣ 📂 documentos  
 ┣ 📂 src  
 ┣ 📂 anexos  


📝Enunciado

💻Imaginá que estás diseñando un sistema de gestión para una biblioteca (préstamo de libros, registro de socios, devoluciones, etc.).

1. Identificá las tres capas principales del sistema (presentación, lógica de negocio, datos) y escribí qué tipo de funciones tendría cada una.

2. Elegí un problema sencillo del sistema (por ejemplo: acceso centralizado a la base de datos, control de usuarios o manejo de configuración) y explicá con tus palabras qué patrón de diseño podría ayudar a resolverlo (por ejemplo: Singleton, MVC, etc.).

🗂️Entrega

- Esquema gráfico (UML).
- Validación del modelo en el lenguaje de programación que usted elija.

💻Tecnologías utilizadas

- Python (3.12.4) #Como lenguaje de programación
- Flask (3.0.3) #Para backend
- UML #Para diseñar los diagramas estos se podrán ver en la carpeta documentos
- Postman #Para test de endpoints y autorización a través de token

⚙️Instalación

1. Para instalar flask, primero debemos crear el archivo requirements.txt, dentro de el poner Flask == 3.0.3
2. Luego desde la terminal ejecutar el siguiente comando
- pip install -r requirements.txt

🚀Ejecución del archivo
1. En primer lugar tenemos que tener todas las carpetas empaquetadas creando un archivo vacío con el nombre __init__.py, esto nos define que se van a crear paquetes que luego van a ser importado en las distintas capas, para comunicarse entre ellos.

2. Para correr el archivo desde la terminal debemos hacer lo siguiente: 
- python -m app (esto hay que hacerlo dentro de la carpeta src)

🔍Test en postman
Para realizar el test, tenemos que hacer lo que voy a describir a continuación:
1. New request
2. En el buscador poner una ruta, ejemplo: http://127.0.0.1:5000/libros/ con el método correspondiente, en este caso GET
3. En authorization definir el tipo de autorización, en este caso Bearer token, y en el campo token poner el token definido, en el código le asigné un token 12345ABC
4. Send (envíar) la solicitud
5. Responderá con un JSON, con los libros cargados en el repository


Presentación del proyecto

- En este proyecto, decidí utilizar una arquitectura en capas, ya que había trabajado en otra materia con esta misma arquitectura, la ventaja que encuentro es tener todo bien estructurado, y bien separado en responsabilidades. 

- Las tres capas (presentación, lógica de negocio, capa de acceso a datos) se explican a continuación:

Capa de presentación (src/controller)

- Esta capa es la responsable de recibir las solicitudes del cliente (Frontend), y enviar las respuestas
(request) y (response).

Funciones

- Definir los enpoints y los métodos HTTP (GET, POST, PUT, DELETE)
- Validaciones de parámetros de entrada básicos
- Llamada a los servicios correspondientes
- Devolver respuestas JSON, o mensajes de error a través de estados (Ej: 404 Not Found)

Ejemplo en código [Listar libro por ID](src/controller/libro_controller.py)


Capa de lógica de negocio (src/service)

- Esta capa es la que contiene las reglas de negocio, define como funciona el sistema, y decide que hacer
con los datos que recibe del controller, antes de que se acceda a la base de datos.

Funciones

- Procesar y validar la información antes de guardarla
- Aplica reglas o restriciones (Ej: si el model tiene una entidad que refiere a otra tabla, 
eliminar un atributo de una entidad, estaría rompiendo la integridad referencial, por lo tanto, no se podría)
- Coordina la comunicación con el repository
- Implementa validaciones, transformaciones, o cálculos

Ejemplo en código [Crear libro](src/service/libro_service.py)


Capa de acceso a datos (src/repository)

- Esta capa es la encargada de acceder, manipular, y guardar los datos en la base de datos
traduce las operaciones de la lógica de negocio a consultas concretas.

Funciones

- Guarda, actualiza, elimina un libro por ID
- Consulta todos los libros
- Interactúa directamente con la base de datos

Ejemplo en código [Guardar libro](src/repository/libro_repository.py)





