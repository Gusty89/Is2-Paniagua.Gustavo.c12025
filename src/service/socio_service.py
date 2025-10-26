from src.dto.socio_dto import SocioDTO
from src.model.socio import Socio
from src.repository.socio_repository import SocioRepository
from flask_bcrypt import Bcrypt 
from typing import Optional, List, Dict, Any

class SocioService:
    def __init__(self, repo: SocioRepository, bcrypt_instance: Bcrypt):
        self.repo = repo
        self.bcrypt = bcrypt_instance

    def registrar(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registra un nuevo socio, hasheando la contraseña y verificando duplicidad de email.
        """
        # OPTIMIZACIÓN 1: Verificar si el email ya existe
        if self.repo.find_by_email(data["email"]):
            raise ValueError("Ya existe un socio registrado con este email.")

        password_plano = data["password"]
        
        # Generar hash de la contraseña
        hashed_password = self.bcrypt.generate_password_hash(password_plano).decode('utf-8')
        
        socio = Socio(
            id_rol=data.get("id_rol", 2),
            nombre_apellido=data["nombre_apellido"],
            dni=data.get("dni"),
            email=data["email"],
            password=hashed_password,
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            # El ID debe ser None. El Repositorio se encarga de asignarlo (auto-incremento).
            id_socio=None 
        )
        
        # El repositorio guarda y asigna el ID al objeto 'socio'
        self.repo.save(socio)
        
        # Devolver el DTO del socio recién creado
        return SocioDTO(socio).to_dict()

    def login(self, email: str, password: str) -> Optional[Socio]:
        """
        Busca al socio por email y verifica la contraseña hasheada.
        """
        socio = self.repo.find_by_email(email)
        
        # Verificar existencia del socio y coincidencia del hash
        if socio and self.bcrypt.check_password_hash(socio.password, password):
            return socio # Devuelve el objeto modelo para que el AuthController genere el JWT
            
        return None

    def listar(self) -> List[Dict[str, Any]]:
        """
        Lista todos los socios y los mapea a DTOs.
        """
        return [SocioDTO(s).to_dict() for s in self.repo.find_all()]

    def get_by_id(self, id_socio: int) -> Optional[Socio]: 
        """
        Busca un socio por ID. Devuelve el objeto modelo.
        """
        # No se mapea a DTO aquí, se devuelve el modelo. Si el controlador necesita el DTO, lo mapeará.
        return self.repo.find_by_id(id_socio)