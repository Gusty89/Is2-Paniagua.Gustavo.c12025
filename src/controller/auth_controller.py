"""
En todos los controllers (Blueprints)se usa from flask_jwt_extended import jwt_required, get_jwt_identity para rutas protegidas
He incluido @jwt_required() donde corresponde (listar, crear recursos sensibles). 
Puedes ajustar permisos por rol posteriormente.
"""



from flask import Blueprint, request, jsonify
from seguridad.jwt_utils import generar_token
# Simple store of users for demo:
USUARIOS = [
    {"email": "admin@biblioteca.com", "password": "admin", "rol": "ADMIN"},
    {"email": "socio@biblioteca.com", "password": "socio", "rol": "SOCIO"}
]

def crear_auth_controller():
    auth_bp = Blueprint("auth_bp", __name__)

    @auth_bp.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        user = next((u for u in USUARIOS if u["email"] == data.get("email") and u["password"] == data.get("password")), None)
        if not user:
            return jsonify({"msg": "Credenciales inválidas"}), 401
        token = generar_token({"email": user["email"], "rol": user["rol"]})
        return jsonify({"token": token})
    return auth_bp
