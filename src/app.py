from flask import Flask
from flask_jwt_extended import JWTManager
# security
from seguridad.jwt_utils import jwt
# repositories
from repository.socio_repository import SocioRepository
from repository.autor_repository import AutorRepository
from repository.libro_repository import LibroRepository
from repository.prestamo_repository import PrestamoRepository
from repository.pago_repository import PagoRepository
from repository.bibliotecario_repository import BibliotecarioRepository
# services
from service.socio_service import SocioService
from service.autor_service import AutorService
from service.libro_service import LibroService
from service.prestamo_service import PrestamoService
from service.pago_service import PagoService
# controllers
from controller.auth_controller import crear_auth_controller
from controller.socio_controller import crear_socio_controller
from controller.autor_controller import crear_autor_controller
from controller.libro_controller import crear_libro_controller
from controller.prestamo_controller import crear_prestamo_controller
from controller.pago_controller import crear_pago_controller

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "esta_es_una_clave_secreta"
jwt.init_app(app)

# crear repos
repo_socio = SocioRepository()
repo_autor = AutorRepository()
repo_libro = LibroRepository()
repo_prestamo = PrestamoRepository()
repo_pago = PagoRepository()
repo_biblio = BibliotecarioRepository()

# crear services
srv_socio = SocioService(repo_socio)
srv_autor = AutorService(repo_autor)
srv_libro = LibroService(repo_libro)
srv_prestamo = PrestamoService(repo_prestamo, repo_libro, repo_socio)
srv_pago = PagoService(repo_pago, repo_socio)

# registrar controllers (blueprints)
app.register_blueprint(crear_auth_controller(), url_prefix="")
app.register_blueprint(crear_socio_controller(srv_socio), url_prefix="")
app.register_blueprint(crear_autor_controller(srv_autor), url_prefix="")
app.register_blueprint(crear_libro_controller(srv_libro), url_prefix="")
app.register_blueprint(crear_prestamo_controller(srv_prestamo), url_prefix="")
app.register_blueprint(crear_pago_controller(srv_pago), url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)
