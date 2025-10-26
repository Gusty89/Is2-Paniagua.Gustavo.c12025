from flask import Blueprint, request, jsonify
from src.service.bibliotecario_service import BibliotecarioService
from flask_jwt_extended import jwt_required, get_jwt_identity

def crear_bibliotecario_controller(srv_bibliotecario: BibliotecarioService):
    """
    Crea el Blueprint para la gestión de Bibliotecarios.
    Todas las rutas están protegidas con JWT y control de rol ADMIN.
    """
    bibliotecario_bp = Blueprint("bibliotecario_bp", __name__)

    # --- RUTA PROTEGIDA: Listar todos los Bibliotecarios ---
    # CORRECCIÓN 1: La ruta debe ser solo "/", asumiendo que el prefix en app.py es "/bibliotecarios"
    @bibliotecario_bp.route("/", methods=["GET"]) 
    @jwt_required()
    def listar_bibliotecarios():
        identidad = get_jwt_identity()
        
        # Solo permite listar si el usuario es un ADMIN
        if identidad.get("rol") != "ADMIN":
            return jsonify({"msg": "Permiso denegado. Se requiere rol de ADMIN."}), 403 
            
        return jsonify(srv_bibliotecario.listar()), 200

    # --- RUTA PROTEGIDA: Registrar un nuevo Bibliotecario (solo por ADMIN) ---
    # CORRECCIÓN 2: La ruta debe ser solo "/", ya que crear recursos es la raíz del endpoint.
    @bibliotecario_bp.route("/", methods=["POST"])
    @jwt_required()
    def registrar_bibliotecario():
        identidad = get_jwt_identity()
        
        # Solo permite registrar si el usuario es un ADMIN
        if identidad.get("rol") != "ADMIN":
            return jsonify({"msg": "Permiso denegado. Se requiere rol de ADMIN."}), 403 

        data = request.get_json()
        
        # Validación básica de datos
        if not data.get('email') or not data.get('password'):
            return jsonify({"msg": "Faltan campos obligatorios (email, password)."}), 400
            
        try:
            nuevo_bibliotecario = srv_bibliotecario.registrar(data)
            return jsonify(nuevo_bibliotecario), 201
            
        # MEJORA: Capturar ValueError si el servicio lo lanza (ej. email duplicado)
        except ValueError as e:
            return jsonify({"msg": str(e)}), 409 # 409 Conflict
        except Exception as e:
            # Manejo de errores genéricos (ej. si el modelo no puede construirse)
            return jsonify({"msg": f"Error interno al registrar: {str(e)}"}), 500

    return bibliotecario_bp