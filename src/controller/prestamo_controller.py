from flask import Blueprint, request, jsonify
from src.service.prestamo_service import PrestamoService # Importación del Servicio
from flask_jwt_extended import jwt_required
from typing import Dict, Any

def crear_prestamo_controller(prestamo_service: PrestamoService):
    """
    Crea el Blueprint para la gestión de Préstamos.
    Asume que el prefix '/prestamos' se registra en app.py.
    """
    prestamo_bp = Blueprint("prestamo_bp", __name__)

    # --- RUTA 1: POST / (Crear Préstamo) ---
    # 🐛 CORRECCIÓN 1: Usar la ruta raíz '/'
    @prestamo_bp.route("/", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        
        # 💡 MEJORA 1: Manejo de errores de negocio
        try:
            # Asume que prestamo_service.crear devuelve un DTO
            return jsonify(prestamo_service.crear(data)), 201
        
        except ValueError as e:
            # Captura errores como 'Libro no disponible', 'Socio no encontrado'
            error_msg = str(e)
            if "no encontrado" in error_msg.lower():
                # 404 si la entidad referenciada no existe
                return jsonify({"msg": error_msg}), 404
            
            # 400 para otras reglas de negocio (libro ya prestado, etc.)
            return jsonify({"msg": error_msg}), 400
        except Exception as e:
            # Error interno genérico (500 Internal Server Error)
            return jsonify({"msg": f"Error interno al crear el préstamo: {str(e)}"}), 500


    # --- RUTA 2: GET / (Listar Préstamos) ---
    # 🐛 CORRECCIÓN 2: Usar la ruta raíz '/'
    @prestamo_bp.route("/", methods=["GET"])
    @jwt_required()
    def listar():
        # Asume que prestamo_service.listar devuelve una lista de DTOs
        # Nota: Aquí se podría añadir un filtro de rol (solo ADMIN puede ver todos)
        return jsonify(prestamo_service.listar()), 200

    return prestamo_bp