from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

def crear_autor_controller(autor_service):
    autor_bp = Blueprint("autor_bp", __name__)

    @autor_bp.route("/autores", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        return jsonify(autor_service.crear(data)), 201

    @autor_bp.route("/autores", methods=["GET"])
    def listar():
        return jsonify(autor_service.listar()), 200

    return autor_bp
