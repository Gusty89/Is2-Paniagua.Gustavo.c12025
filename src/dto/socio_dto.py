from src.model.socio import Socio
# Asumo que el modelo Socio está en src.model.socio

class SocioDTO:
    """
    Data Transfer Object (DTO) para la entidad Socio.
    Se utiliza para serializar el objeto del modelo 'Socio' a un diccionario
    seguro para la respuesta JSON, excluyendo el hash de la contraseña.
    """
    
    def __init__(self, socio: Socio):
        """Inicializa el DTO con una instancia del modelo Socio."""
        self.socio = socio

    def to_dict(self):
        """
        Convierte el objeto Socio a un diccionario seguro para la API.
        """
        return {
            "id_socio": self.socio.id_socio,
            "id_rol": self.socio.id_rol,
            "nombre_apellido": self.socio.nombre_apellido,
            "dni": self.socio.dni,
            "email": self.socio.email,
            "direccion": self.socio.direccion,
            "telefono": self.socio.telefono,
            # NOTA: No incluir self.socio.password (el hash)
        }