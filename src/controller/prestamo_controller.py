from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

def crear_prestamo_controller(prestamo_service):
    bp = Blueprint("prestamo_bp", __name__)

    @bp.route("/prestamos", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        return jsonify(prestamo_service.crear(data)), 201

    @bp.route("/prestamos", methods=["GET"])
    @jwt_required()
    def listar():
        return jsonify(prestamo_service.listar()), 200

    return bp
