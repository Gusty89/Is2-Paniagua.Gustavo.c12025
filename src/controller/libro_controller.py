from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

def crear_libro_controller(libro_service):
    libro_bp = Blueprint("libro_bp", __name__)

    @libro_bp.route("/libros", methods=["POST"])
    @jwt_required()
    def crear():
        data = request.get_json()
        return jsonify(libro_service.crear(data)), 201

    @libro_bp.route("/libros", methods=["GET"])
    def listar():
        return jsonify(libro_service.listar()), 200

    @libro_bp.route("/libros/<int:id_libro>/prestar", methods=["POST"])
    @jwt_required()
    def prestar(id_libro):
        res = libro_service.prestar(id_libro)
        if res == "YA_PRESTADO":
            return jsonify({"error": "Libro ya prestado"}), 400
        if res is None:
            return jsonify({"error": "Libro no encontrado"}), 404
        return jsonify(res), 200

    @libro_bp.route("/libros/<int:id_libro>/devolver", methods=["POST"])
    @jwt_required()
    def devolver(id_libro):
        res = libro_service.devolver(id_libro)
        if res is None:
            return jsonify({"error": "Libro no encontrado"}), 404
        return jsonify(res), 200

    return libro_bp
