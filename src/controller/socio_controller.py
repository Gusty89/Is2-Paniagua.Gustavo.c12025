from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

def crear_socio_controller(socio_service):
    socio_bp = Blueprint("socio_bp", __name__)

    @socio_bp.route("/socios", methods=["POST"])
    def registrar():
        data = request.get_json()
        dto = socio_service.registrar(data)
        return jsonify(dto), 201

    @socio_bp.route("/socios", methods=["GET"])
    @jwt_required()
    def listar():
        return jsonify(socio_service.listar())

    @socio_bp.route("/socios/<int:id_socio>", methods=["GET"])
    @jwt_required()
    def get_socio(id_socio):
        s = socio_service.get_by_id(id_socio)
        if not s: return jsonify({"error":"no encontrado"}), 404
        return jsonify({"id_socio": s.id_socio, "nombre_apellido": s.nombre_apellido, "email": s.email})
    return socio_bp
