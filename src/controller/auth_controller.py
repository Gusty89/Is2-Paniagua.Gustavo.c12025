from flask import Blueprint, request, jsonify
from src.seguridad.jwt_utils import generar_token
# No es necesario importar Bcrypt aquí si se inyecta

# --- Base de Datos Simulada Global ---
# Mantener la lista de usuarios como un elemento mutable global (o una clase Singleton)
# En una aplicación real, esta lista sería una clase de repositorio conectada a una BBDD.
USUARIOS = []

# --- Definición de la Función Controlador ---

def crear_auth_controller(bcrypt_instance):
    """
    Crea el Blueprint de autenticación y maneja las rutas /register y /login.
    Recibe el objeto Bcrypt inicializado como inyección de dependencia.
    """
    
    # Solo poblar la lista de usuarios iniciales si está vacía. 
    if not USUARIOS:
        USUARIOS_INICIALES_HASHED = [
            {"email": "admin@biblioteca.com", "password": bcrypt_instance.generate_password_hash("admin").decode('utf-8'), "rol": "ADMIN"},
            {"email": "socio@biblioteca.com", "password": bcrypt_instance.generate_password_hash("socio").decode('utf-8'), "rol": "SOCIO"}
        ]
        USUARIOS.extend(USUARIOS_INICIALES_HASHED)
        print("Usuarios Iniciales Cargados:")
        print(USUARIOS) #Imprime los usuarios con hashes
        
    auth_bp = Blueprint("auth_bp", __name__)

    # ------------------------------------------------------------------
    # RUTA: REGISTRO DE USUARIOS (Sin cambios)
    # ------------------------------------------------------------------
    @auth_bp.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"msg": "Faltan email y/o password"}), 400

        if any(u["email"] == email for u in USUARIOS):
            return jsonify({"msg": "El usuario ya está registrado"}), 409 # Conflict

        hashed_password = bcrypt_instance.generate_password_hash(password).decode('utf-8')

        nuevo_usuario = {
            "email": email,
            "password": hashed_password,
            "rol": "SOCIO" 
        }
        USUARIOS.append(nuevo_usuario)

        return jsonify({"msg": "Usuario registrado exitosamente. Ahora puede iniciar sesión."}), 201

    # ------------------------------------------------------------------
    # RUTA: LOGIN (CORREGIDA)
    # ------------------------------------------------------------------
    @auth_bp.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # 1. Buscar usuario por email
        user = next((u for u in USUARIOS if u["email"] == email), None)

        # 2. Verificar existencia del usuario Y la contraseña hasheada
        if user and bcrypt_instance.check_password_hash(user["password"], password):
            
            # 🛑 CORRECCIÓN: Separar la identidad (string) de los claims (dict)
            subject_id = user["email"]
            claims = {"rol": user["rol"]}
            
            # Contraseña correcta, genera el token usando la nueva firma
            token = generar_token(subject_id, claims)
            
            return jsonify({"token": token}), 200
        else:
            # Error genérico: "Credenciales inválidas"
            return jsonify({"msg": "Credenciales inválidas"}), 401

    return auth_bp