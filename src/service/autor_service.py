from dto.autor_dto import AutorDTO
from model.autor import Autor

class AutorService:
    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):
        autor = Autor(id_autor=None, nombre_apellido=data["nombre_apellido"], nacionalidad=data.get("nacionalidad"))
        saved = self.repo.save(autor)
        return AutorDTO(saved).to_dict()

    def listar(self):
        return [AutorDTO(a).to_dict() for a in self.repo.find_all()]
