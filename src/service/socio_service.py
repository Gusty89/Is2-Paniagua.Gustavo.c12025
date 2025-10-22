from dto.socio_dto import SocioDTO
from model.socio import Socio
from repository.socio_repository import SocioRepository

class SocioService:
    def __init__(self, repo: SocioRepository):
        self.repo = repo

    def registrar(self, data):
        socio = Socio(
            id_rol=data.get("id_rol", 2),
            nombre_apellido=data["nombre_apellido"],
            dni=data.get("dni"),
            email=data["email"],
            password=data["password"],
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            id_socio=data["id_socio"]
        )
        self.repo.save(socio)
        return SocioDTO(socio).to_dict()

    def login(self, email, password):
        socio = self.repo.find_by_email(email)
        if socio and socio.password == password:
            return socio
        return None

    def listar(self):
        return [SocioDTO(s).to_dict() for s in self.repo.find_all()]

    def get_by_id(self, id_socio):
        return self.repo.find_by_id(id_socio)
