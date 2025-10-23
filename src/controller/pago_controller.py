from flask import Blueprint, request, jsonify
from src.service.pago_service import PagoService # Importación del Servicio
from flask_jwt_extended import jwt_required
from typing import Dict, Any

def crear_pago_controller(pago_service: PagoService):
    """
    Crea el Blueprint para la gestión de Pagos.
    Asume que el prefix '/pagos' se registra en app.py.
    """
    pago_bp = Blueprint("pago_bp", __name__)

    # --- RUTA 1: POST / (Crear Pago) ---
    # 🐛 CORRECCIÓN 1: Usar la ruta raíz '/'
    @pago_bp.route("/", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        
        # 💡 MEJORA 1: Manejo de errores de negocio
        try:
            # Asume que pago_service.crear devuelve un DTO
            return jsonify(pago_service.crear(data)), 201
        
        except ValueError as e:
            # Captura errores como 'Socio no encontrado', 'Monto inválido' (400 Bad Request)
            return jsonify({"msg": str(e)}), 400
        except Exception as e:
            # Error interno genérico (500 Internal Server Error)
            return jsonify({"msg": f"Error interno al registrar el pago: {str(e)}"}), 500


    # --- RUTA 2: GET / (Listar Pagos) ---
    # 🐛 CORRECCIÓN 2: Usar la ruta raíz '/'
    @pago_bp.route("/", methods=["GET"])
    @jwt_required()
    def listar():
        # Asume que pago_service.listar devuelve una lista de DTOs
        # Nota: Aquí se podría añadir un filtro de rol (solo ADMIN puede ver todos los pagos)
        return jsonify(pago_service.listar()), 200

    return pago_bp