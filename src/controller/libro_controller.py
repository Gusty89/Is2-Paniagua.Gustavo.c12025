from flask import Blueprint, request, jsonify
from src.service.libro_service import LibroService # Importación del Servicio
from flask_jwt_extended import jwt_required
from typing import Dict, Any

def crear_libro_controller(libro_service: LibroService):
    """
    Crea el Blueprint para la gestión de Libros y Préstamos/Devoluciones.
    Asume que el prefix '/libros' se registra en app.py.
    """
    libro_bp = Blueprint("libro_bp", __name__)

    # --- RUTA 1: POST / (Crear Libro) ---
    # 🐛 CORRECCIÓN 1: Usar la ruta raíz '/'
    @libro_bp.route("/", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        
        # 💡 MEJORA 1: Manejo de errores (ej. ISBN duplicado, datos faltantes)
        try:
            # Asume que libro_service.crear devuelve un DTO
            return jsonify(libro_service.crear(data)), 201
        except ValueError as e:
            # Error 400 Bad Request o 409 Conflict (si es por unicidad)
            return jsonify({"msg": str(e)}), 400 
        except Exception as e:
            return jsonify({"msg": f"Error interno al crear el libro: {str(e)}"}), 500


    # --- RUTA 2: GET / (Listar Libros) ---
    # 🐛 CORRECCIÓN 2: Usar la ruta raíz '/'
    @libro_bp.route("/", methods=["GET"])
    def listar():
        # Asume que libro_service.listar devuelve una lista de DTOs
        return jsonify(libro_service.listar()), 200


    # --- RUTA 3: POST /<id_libro>/prestar (Prestar Libro) ---
    # 🐛 CORRECCIÓN 3: Usar solo el segmento de la ruta, asumiendo /libros/{id}/prestar
    @libro_bp.route("/<int:id_libro>/prestar", methods=["POST"])
    @jwt_required()
    def prestar(id_libro: int):
        data = request.get_json() or {} # Obtener datos (podría incluir id_socio)
        
        try:
            # 💡 MEJORA 2: Pasar el ID de socio (o el token) para registrar el préstamo
            res = libro_service.prestar(id_libro, data.get('id_socio')) 
            return jsonify(res), 200
            
        except ValueError as e:
            # Captura errores como "Libro ya prestado", "Socio inválido"
            error_msg = str(e)
            if "ya prestado" in error_msg.lower():
                 return jsonify({"error": error_msg}), 400
            if "no encontrado" in error_msg.lower() or "socio inválido" in error_msg.lower():
                 return jsonify({"error": error_msg}), 404
            
            return jsonify({"error": error_msg}), 400
        except Exception as e:
            return jsonify({"msg": f"Error interno en el préstamo: {str(e)}"}), 500


    # --- RUTA 4: POST /<id_libro>/devolver (Devolver Libro) ---
    # 🐛 CORRECCIÓN 4: Usar solo el segmento de la ruta
    @libro_bp.route("/<int:id_libro>/devolver", methods=["POST"])
    @jwt_required()
    def devolver(id_libro: int):
        # La devolución no suele requerir body, solo el ID.
        try:
            res = libro_service.devolver(id_libro)
            return jsonify(res), 200
            
        except ValueError as e:
            # Captura errores como "Libro no estaba prestado"
            return jsonify({"error": str(e)}), 400 
        except Exception as e:
            return jsonify({"msg": f"Error interno en la devolución: {str(e)}"}), 500

    return libro_bp