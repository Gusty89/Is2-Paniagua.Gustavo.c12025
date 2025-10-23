"""
Manejo de la configuración y generación de JWT.
"""

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from typing import Dict, Any

jwt = JWTManager()

def generar_token(subject_id: str, claims: Dict[str, Any]) -> str:
    """
    Genera un token JWT de acceso.

    - subject_id (str): El valor principal de la identidad (ej., el email).
      Esto cumple con el requisito de que el 'Subject' debe ser una cadena.
    - claims (dict): El diccionario de datos adicionales, como el 'rol'.
    """
    # 🛑 CORRECCIÓN: Usamos 'identity' para el subject (string) y 
    # 'additional_claims' para el resto del diccionario (el rol).
    return create_access_token(identity=subject_id, additional_claims=claims)