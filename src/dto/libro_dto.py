class LibroDTO:
    def __init__(self, libro):
        self.id_libro = libro.id_libro
        self.titulo = libro.titulo
        self.isbn = libro.isbn
        self.estado = libro.estado.value

    def to_dict(self):
        return {
            "id_libro": self.id_libro, 
            "titulo": self.titulo, 
            "isbn": self.isbn, 
            "estado": self.estado
            }
