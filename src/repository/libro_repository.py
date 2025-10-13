from src.model.libro import Libro

class LibroRepository:
    def __init__(self):
        self.libros = [
            Libro(1, "1984", "George Orwell"),
            Libro(2, "Cien años de soledad", "Gabriel García Márquez"),
            Libro(3, "El Principito", "Antoine de Saint-Exupéry")
        ]

    def find_all(self):
        return self.libros

    def find_by_id(self, id):
        return next((l for l in self.libros if l.id == id), None)

    def save(self, libro):
        self.libros.append(libro)
        return libro

    def delete(self, id):
        self.libros = [l for l in self.libros if l.id != id]
