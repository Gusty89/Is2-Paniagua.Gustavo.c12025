from src.model.bibliotecario import Bibliotecario
# Asumo que tienes un DTO base o que todos los modelos tienen atributos similares

class BibliotecarioDTO:
    """
    Data Transfer Object (DTO) para la entidad Bibliotecario.
    Se utiliza para serializar (convertir) el objeto del modelo a un diccionario
    seguro para ser enviado como respuesta JSON, excluyendo datos sensibles como el hash de la contraseña.
    """
    
    def __init__(self, bibliotecario: Bibliotecario):
        """Inicializa el DTO con una instancia del modelo Bibliotecario."""
        self.bibliotecario = bibliotecario

    def to_dict(self):
        """
        Convierte el objeto Bibliotecario a un diccionario.
        """
        return {
            "id_bibliotecario": self.bibliotecario.id_bibliotecario,
            "id_rol": self.bibliotecario.id_rol,
            "nombre_apellido": self.bibliotecario.nombre_apellido,
            "dni": self.bibliotecario.dni,
            "email": self.bibliotecario.email,
            "direccion": self.bibliotecario.direccion,
            "telefono": self.bibliotecario.telefono,
            # NOTA: La contraseña (password hash) NUNCA debe ser incluida en el DTO de respuesta.
        }