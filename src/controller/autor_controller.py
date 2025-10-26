from flask import Blueprint, request, jsonify
from src.service.autor_service import AutorService # 👈 Add missing service import (assuming it exists)
from flask_jwt_extended import jwt_required

def crear_autor_controller(autor_service: AutorService):
    """
    Crea el Blueprint para la gestión de Autores.
    Asume que el prefix '/autores' se registra en app.py.
    """
    autor_bp = Blueprint("autor_bp", __name__)

    # --- RUTA 1: POST / (Crear Autor) ---
    # CORRECCIÓN 1: Usar la ruta raíz '/'
    @autor_bp.route("/", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        
        # MEJORA: Añadir manejo de errores
        try:
            # Asume que autor_service.crear devuelve un DTO
            return jsonify(autor_service.crear(data)), 201
        except ValueError as e:
            # Si el servicio lanza un ValueError (ej. campo faltante)
            return jsonify({"msg": str(e)}), 400 
        except Exception as e:
            # Error interno genérico
            return jsonify({"msg": f"Error interno al crear el autor: {str(e)}"}), 500


    # --- RUTA 2: GET / (Listar Autores) ---
    # CORRECCIÓN 2: Usar la ruta raíz '/'
    # Nota: Esta ruta está abierta al público (sin @jwt_required())
    @autor_bp.route("/", methods=["GET"])
    def listar():
        # Asume que autor_service.listar devuelve una lista de DTOs
        return jsonify(autor_service.listar()), 200

    return autor_bp