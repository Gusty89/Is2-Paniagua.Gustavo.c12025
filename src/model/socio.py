from .rol import Rol

class Socio(Rol):
    def __init__(self, id_rol, nombre_apellido, dni, email, password, direccion, telefono, id_socio):
        super().__init__(id_rol, nombre_apellido, dni, email, password, direccion, telefono)
        self.id_socio = id_socio
        self.prestamos = []

    def solicitar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def efectuar_pago(self, pago):
        print(f"Pago realizado por {self.nombre_apellido}")

    def consultar_prestamos(self):
        return [p.__dict__ for p in self.prestamos]
