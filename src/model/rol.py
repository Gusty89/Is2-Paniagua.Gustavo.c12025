class Rol:
    def __init__(self, id_rol, nombre_apellido, dni, email, password, direccion, telefono):
        self.id_rol = id_rol
        self.nombre_apellido = nombre_apellido
        self.dni = dni
        self.email = email
        self.password = password
        self.direccion = direccion
        self.telefono = telefono

    def registro(self):
        print(f"Registro de usuario: {self.nombre_apellido}")

    def sesion(self, email, password):
        return self.email == email and self.password == password
