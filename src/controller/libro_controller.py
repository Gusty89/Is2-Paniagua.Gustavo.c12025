from flask import Blueprint, jsonify, request
from src.seguridad.auth import requiere_token
from src.service.libro_service import LibroService

libro_bp = Blueprint("libros", __name__)
service = LibroService()

@libro_bp.route("/", methods=["GET"])
@requiere_token
def listar_libros():
    return jsonify(service.obtener_todos())

@libro_bp.route("/<int:id>", methods=["GET"])
@requiere_token
def obtener_libro(id):
    libro = service.obtener_por_id(id)
    return jsonify(libro) if libro else (jsonify({"error": "No encontrado"}), 404)

@libro_bp.route("/", methods=["POST"])
@requiere_token
def crear_libro():
    data = request.get_json()
    nuevo = service.crear_libro(data)
    return jsonify(nuevo), 201

@libro_bp.route("/<int:id>", methods=["DELETE"])
@requiere_token
def eliminar_libro(id):
    return jsonify(service.eliminar_libro(id))
