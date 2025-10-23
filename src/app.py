from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# --- 1. Inicialización de la Aplicación y Extensiones ---

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "esta_es_una_clave_secreta"

# Inicialización de extensiones DESPUÉS de definir 'app'
# Nota: Asumo que 'jwt' se importa sin inicializar o es el objeto JWTManager
from src.seguridad.jwt_utils import jwt # Asumo que es JWTManager() sin app
jwt.init_app(app)

# Inicialización de Bcrypt. Debe ocurrir DESPUÉS de definir 'app'.
bcrypt = Bcrypt(app)


# --- 2. Importaciones Locales (Repositorios, Servicios, Controladores, DTOs) ---
# repositories
from src.repository.socio_repository import SocioRepository
from src.repository.autor_repository import AutorRepository
from src.repository.libro_repository import LibroRepository
from src.repository.prestamo_repository import PrestamoRepository
from src.repository.pago_repository import PagoRepository
from src.repository.bibliotecario_repository import BibliotecarioRepository
# services
from src.service.socio_service import SocioService
from src.service.autor_service import AutorService
from src.service.libro_service import LibroService
from src.service.prestamo_service import PrestamoService
from src.service.pago_service import PagoService
from src.service.bibliotecario_service import BibliotecarioService
# controllers
from src.controller.auth_controller import crear_auth_controller
from src.controller.socio_controller import crear_socio_controller
from src.controller.autor_controller import crear_autor_controller
from src.controller.libro_controller import crear_libro_controller
from src.controller.prestamo_controller import crear_prestamo_controller
from src.controller.pago_controller import crear_pago_controller
from src.controller.bibliotecario_controller import crear_bibliotecario_controller
# dto (generalmente no se necesitan en el __init__ de Flask, pero se dejan)
from src.dto.socio_dto import SocioDTO
from src.dto.autor_dto import AutorDTO
from src.dto.libro_dto import LibroDTO
from src.dto.prestamo_dto import PrestamoDTO
from src.dto.pago_dto import PagoDTO
from src.dto.bibliotecario_dto import BibliotecarioDTO


# --- 3. Instanciación de Capas (Repositorios y Servicios) ---

# crear repos
repo_socio = SocioRepository()
repo_autor = AutorRepository()
repo_libro = LibroRepository()
repo_prestamo = PrestamoRepository()
repo_pago = PagoRepository()
repo_biblio = BibliotecarioRepository()

# crear services
srv_socio = SocioService(repo_socio, bcrypt) # Posiblemente Bcrypt debe ir aquí
srv_biblio = BibliotecarioService(repo_biblio, bcrypt) # Inyección de Bcrypt
srv_autor = AutorService(repo_autor)
srv_libro = LibroService(repo_libro)
srv_prestamo = PrestamoService(repo_prestamo, repo_libro, repo_socio)
srv_pago = PagoService(repo_pago, repo_socio)


# --- 4. Registro de Controladores (Blueprints) ---

app.register_blueprint(crear_auth_controller(bcrypt), url_prefix="/auth") # Pasa bcrypt y usa prefijo
app.register_blueprint(crear_socio_controller(srv_socio), url_prefix="/socios") # Usa prefijo
app.register_blueprint(crear_autor_controller(srv_autor), url_prefix="/autores") # Usa prefijo
app.register_blueprint(crear_libro_controller(srv_libro), url_prefix="/libros") # Usa prefijo
app.register_blueprint(crear_prestamo_controller(srv_prestamo), url_prefix="/prestamos") # Usa prefijo
app.register_blueprint(crear_pago_controller(srv_pago), url_prefix="/pagos") # Usa prefijo
app.register_blueprint(crear_bibliotecario_controller(srv_biblio), url_prefix="/bibliotecarios") # Usa prefijo

if __name__ == "__main__":
    app.run(debug=True)