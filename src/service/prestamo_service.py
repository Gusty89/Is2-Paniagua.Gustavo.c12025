from dto.prestamo_dto import PrestamoDTO
from model.prestamo import Prestamo

class PrestamoService:
    def __init__(self, repo_prestamo, repo_libro, repo_socio):
        self.pr_repo = repo_prestamo
        self.libro_repo = repo_libro
        self.socio_repo = repo_socio

    def crear(self, data):
        id_libro = data["id_libro"]
        id_socio = data["id_socio"]
        libro = self.libro_repo.find_by_id(id_libro)
        socio = self.socio_repo.find_by_id(id_socio)
        if not libro or not socio:
            return {"error": "Libro o socio no encontrado"}
        if libro.estado.name == "PRESTADO":
            return {"error": "Libro ya prestado"}
        prestamo = Prestamo(id_prestamo=None, id_libro=id_libro, id_socio=id_socio)
        saved = self.pr_repo.save(prestamo)
        libro.estado = libro.estado.__class__.PRESTADO
        socio.prestamos.append(saved)
        return PrestamoDTO(saved).to_dict()

    def listar(self):
        return [PrestamoDTO(p).to_dict() for p in self.pr_repo.find_all()]
