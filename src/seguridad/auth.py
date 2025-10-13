from functools import wraps
from flask import request, jsonify

TOKEN_VALIDO = "12345ABC"

def requiere_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != f"Bearer {TOKEN_VALIDO}":
            return jsonify({"error": "Token inválido o ausente"}), 401
        return f(*args, **kwargs)
    return decorador
