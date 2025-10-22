from .rol import Rol

class Bibliotecario(Rol):
    def __init__(self, id_rol, nombre_apellido, dni, email, password, direccion, telefono, id_bibliotecario):
        super().__init__(id_rol, nombre_apellido, dni, email, password, direccion, telefono)
        self.id_bibliotecario = id_bibliotecario
