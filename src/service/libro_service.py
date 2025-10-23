from src.dto.libro_dto import LibroDTO
from src.model.libro import Libro, EstadoLibro

class LibroService:
    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):
        libro = Libro(id_libro=data["id_libro"], titulo=data["titulo"], isbn=data.get("isbn"), autores=data.get("autores"))
        self.repo.save(libro)
        return LibroDTO(libro).to_dict()

    def listar(self):
        return [LibroDTO(l).to_dict() for l in self.repo.find_all()]

    def prestar(self, id_libro):
        libro = self.repo.find_by_id(id_libro)
        if not libro:
            return None
        if libro.estado == EstadoLibro.PRESTADO:
            return "YA_PRESTADO"
        libro.estado = EstadoLibro.PRESTADO
        return LibroDTO(libro).to_dict()

    def devolver(self, id_libro):
        libro = self.repo.find_by_id(id_libro)
        if not libro: return None
        libro.estado = EstadoLibro.DISPONIBLE
        return LibroDTO(libro).to_dict()
