🗂️ IS2-PANIAGUA.GUSTAVO.C12025  
 ┣ 📂 documentos  
 ┣ 📂 src  
 ┣ 📂 anexos  


📝Enunciado

💻Imaginá que estás diseñando un sistema de gestión para una biblioteca (préstamo de libros, registro de socios, devoluciones, etc.).

1. Identificá las tres capas principales del sistema (presentación, lógica de negocio, datos) y escribí qué tipo de funciones tendría cada una.

- [Diseño Arquitectónico](anexos/Arquitectura_en_3_capas.png)
- [Explicación de las funciones de la arquitectura en detalle](documentos/diseñoExplicacion.txt)

2. Elegí un problema sencillo del sistema (por ejemplo: acceso centralizado a la base de datos, control de usuarios o manejo de configuración) y explicá con tus palabras qué patrón de diseño podría ayudar a resolverlo (por ejemplo: Singleton, MVC, etc.).

- [Explicación del patrón de diseño](documentos/patronExplicacion.txt)

🗂️Entrega

- Esquema gráfico (UML).
- Validación del modelo en el lenguaje de programación que usted elija.

💻Tecnologías utilizadas

- Python (3.12.4) #Como lenguaje de programación
- Flask (3.0.3) #Para backend
- Flask-JWT-Extended==4.6.0 #Para la generación de tokens de seguridad
- Flask-Bcrypt==1.0.1 #Para hasheo de contraseñas
- UML #Para diseñar los diagramas estos se podrán ver en la carpeta anexos
- Postman #Para test de endpoints y autorización a través de token

⚙️Instalación

1. Para instalar flask, primero debemos crear el archivo requirements.txt, dentro de el poner Flask == 3.0.3, Flask-JWT-Extended==4.6.0, Flask-Bcrypt==1.0.1
2. Luego desde la terminal ejecutar el siguiente comando
- pip install -r requirements.txt

🚀Ejecución del archivo
1. En primer lugar tenemos que tener todas las carpetas empaquetadas creando un archivo vacío con el nombre [Paquetes](__init__.py), esto nos define que se van a crear paquetes que luego van a ser importado en las distintas capas, para comunicarse entre ellas.

2. Para correr el archivo desde la terminal debemos hacer lo siguiente: 
- python -m src.app (desde la raíz del proyecto)

🔍Test en postman
- Para realizar el test, tenemos que hacer lo que voy a describir a continuación:
1. New request
2. En el buscador poner una ruta, ejemplo: http://127.0.0.1:5000/auth/register con el método, en este caso POST y send (envíar)
3. Se registra el socio/bibliotecario, esto va a depender el rol que le asignemos
4. Luego en el buscador, pondremos esta ruta http://127.0.0.1:5000/auth/login con el método, en este caso de nuevo POST y send (envíar)
5. Esto me genera un JSON con el token, para ser autorizado por cuestiones de seguridad
6. [Capturas de test se encuentran en:](anexos)

> 💡 **Nota Importante:** Si bien está agregada la capa repository, decidí utilizar una lista genérica para pruebas
con postman, a esta capa se la puede migrar con alembic a una BDD.

> 💡 **Nota Importante:** Implementé la capa seguridad, simulando un backend de una API, listo para integrarlo con un frontend.

> 💡 **Nota Importante:** El hasheo de contraseñas con Bcrypt lo podemos observar en la terminal cuando levantamos el server.





