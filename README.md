🗂️ IS2-PANIAGUA.GUSTAVO.C12025  
 ┣ 📂 documentos  
 ┣ 📂 src  
 ┣ 📂 anexos  


📝Enunciado

💻Imaginá que estás diseñando un sistema de gestión para una biblioteca (préstamo de libros, registro de socios, devoluciones, etc.).

1. Identificá las tres capas principales del sistema (presentación, lógica de negocio, datos) y escribí qué tipo de funciones tendría cada una.

[Diseño Arquitectónico](anexos/Arquitectura_en_3_capas.png)
[Explicación de las funciones de la arquitectura en detalle](documentos/diseñoExplicacion.txt)

2. Elegí un problema sencillo del sistema (por ejemplo: acceso centralizado a la base de datos, control de usuarios o manejo de configuración) y explicá con tus palabras qué patrón de diseño podría ayudar a resolverlo (por ejemplo: Singleton, MVC, etc.).

🗂️Entrega

- Esquema gráfico (UML).
- Validación del modelo en el lenguaje de programación que usted elija.

💻Tecnologías utilizadas

- Python (3.12.4) #Como lenguaje de programación
- Flask (3.0.3) #Para backend
- UML #Para diseñar los diagramas estos se podrán ver en la carpeta anexos
- Postman #Para test de endpoints y autorización a través de token

⚙️Instalación

1. Para instalar flask, primero debemos crear el archivo requirements.txt, dentro de el poner Flask == 3.0.3
2. Luego desde la terminal ejecutar el siguiente comando
- pip install -r requirements.txt

🚀Ejecución del archivo
1. En primer lugar tenemos que tener todas las carpetas empaquetadas creando un archivo vacío con el nombre [Paquetes](__init__.py), esto nos define que se van a crear paquetes que luego van a ser importado en las distintas capas, para comunicarse entre ellas.

2. Para correr el archivo desde la terminal debemos hacer lo siguiente: 
- python -m app (esto hay que hacerlo dentro de la carpeta src)

🔍Test en postman
- Para realizar el test, tenemos que hacer lo que voy a describir a continuación:
1. New request
2. En el buscador poner una ruta, ejemplo: http://127.0.0.1:5000/libros/ con el método correspondiente, en este caso GET
3. En authorization definir el tipo de autorización, en este caso Bearer token, y en el campo token poner el token definido, en el código le asigné un token 12345ABC
4. Send (envíar) la solicitud
5. Responderá con un JSON, con los libros cargados en el repository




