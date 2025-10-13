from src.dto.libro_dto import LibroDTO
from src.repository.libro_repository import LibroRepository
from src.model.libro import Libro

class LibroService:
    def __init__(self):
        self.repository = LibroRepository()

    def obtener_todos(self):
        return [LibroDTO(l.id, l.titulo, l.autor).to_dict() for l in self.repository.find_all()]

    def obtener_por_id(self, id):
        libro = self.repository.find_by_id(id)
        if libro:
            return LibroDTO(libro.id, libro.titulo, libro.autor).to_dict()
        return None

    def crear_libro(self, data):
        nuevo = Libro(id=len(self.repository.libros)+1, titulo=data["titulo"], autor=data["autor"])
        self.repository.save(nuevo)
        return LibroDTO(nuevo.id, nuevo.titulo, nuevo.autor).to_dict()

    def eliminar_libro(self, id):
        self.repository.delete(id)
        return {"mensaje": f"Libro con id {id} eliminado"}
