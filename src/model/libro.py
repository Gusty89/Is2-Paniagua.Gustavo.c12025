from enum import Enum

class EstadoLibro(Enum):
    DISPONIBLE = "DISPONIBLE"
    PRESTADO = "PRESTADO"

class Libro:
    def __init__(self, id_libro, titulo, isbn, estado=EstadoLibro.DISPONIBLE):
        self.id_libro = id_libro
        self.titulo = titulo
        self.isbn = isbn
        self.estado = estado

    def prestar_libro(self):
        self.estado = EstadoLibro.PRESTADO

    def devolver_libro(self):
        self.estado = EstadoLibro.DISPONIBLE
