class AutorDTO:
    def __init__(self, autor):
        self.id_autor = autor.id_autor
        self.nombre_apellido = autor.nombre_apellido
        self.nacionalidad = autor.nacionalidad

    def to_dict(self):
        return {
            "id_autor": self.id_autor, 
            "nombre_apellido": self.nombre_apellido, 
            "nacionalidad": self.nacionalidad
            }
