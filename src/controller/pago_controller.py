from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

def crear_pago_controller(pago_service):
    bp = Blueprint("pago_bp", __name__)

    @bp.route("/pagos", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        return jsonify(pago_service.crear(data)), 201

    @bp.route("/pagos", methods=["GET"])
    @jwt_required()
    def listar():
        return jsonify(pago_service.listar()), 200

    return bp
