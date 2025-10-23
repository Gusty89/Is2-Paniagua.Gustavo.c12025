# src/controller/socio_controller.py

from flask import Blueprint, request, jsonify
from src.service.socio_service import SocioService
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity 

def crear_socio_controller(socio_service: SocioService):
    """
    Crea el Blueprint para la gestión de Socios.
    Asume que el prefix '/socios' se registra en app.py.
    """
    socio_bp = Blueprint("socio_bp", __name__)

    # --- RUTA 1: POST / (Crear Socio) ---
    @socio_bp.route("/", methods=["POST"])
    def registrar():
        """
        Permite registrar un nuevo socio.
        Nota: Esta ruta NO requiere JWT, ya que los usuarios se registran libremente.
        """
        data = request.get_json()
        
        try:
            dto = socio_service.registrar(data)
            return jsonify(dto), 201
        except ValueError as e:
            # Error 409 Conflict si el email ya existe
            return jsonify({"msg": str(e)}), 409
        except Exception as e:
            # Error genérico si falla la construcción del modelo o el hash
            return jsonify({"msg": f"Error interno al registrar el socio: {str(e)}"}), 500


    # --- RUTA 2: GET / (Listar Socios) ---
    @socio_bp.route("/", methods=["GET"])
    @jwt_required()
    def listar():
        """
        Lista todos los socios. Restringido solo al rol ADMIN (Bibliotecario).
        """
        # 1. Obtener los Claims (incluye el rol)
        claims = get_jwt()
        rol_usuario = claims.get("rol")
        
        # 2. IMPLEMENTACIÓN RBAC: Verificar el rol
        if rol_usuario != "ADMIN":
            return jsonify({
                "msg": "Permiso denegado. Se requiere rol de ADMIN para listar todos los socios."
            }), 403
            
        return jsonify(socio_service.listar()), 200


    # --- RUTA 3: GET /<id_socio> (Buscar por ID) ---
    @socio_bp.route("/<int:id_socio>", methods=["GET"])
    @jwt_required()
    def get_socio(id_socio):
        """
        Busca un socio por ID. Acceso: ADMIN o el propio socio.
        """
        # 1. Obtener el rol de los claims y el email del subject
        claims = get_jwt()
        rol_usuario = claims.get("rol")
        email_usuario_token = get_jwt_identity() # Subject (email)
        
        s = socio_service.get_by_id(id_socio)
        
        if not s: 
            return jsonify({"error": f"Socio con ID {id_socio} no encontrado"}), 404

        socio_email = s.email

        # RBAC en GET individual
        # Permite si es ADMIN O si el email del token coincide con el email del socio buscado
        if rol_usuario != "ADMIN" and email_usuario_token != socio_email:
             return jsonify({
                "msg": "Permiso denegado. Solo puedes ver tus propios datos."
            }), 403

        return jsonify(socio_service.socio_to_dto(s)), 200
        
    return socio_bp