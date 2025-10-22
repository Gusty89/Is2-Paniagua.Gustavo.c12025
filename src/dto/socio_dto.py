class SocioDTO:
    def __init__(self, socio):
        self.id_socio = socio.id_socio
        self.nombre_apellido = socio.nombre_apellido
        self.email = socio.email

    def to_dict(self):
        return {
            "id_socio": self.id_socio, 
            "nombre_apellido": self.nombre_apellido, 
            "email": self.email
            }
