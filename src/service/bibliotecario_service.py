from src.repository.bibliotecario_repository import BibliotecarioRepository
from src.model.bibliotecario import Bibliotecario
from flask_bcrypt import Bcrypt 
from src.dto.bibliotecario_dto import BibliotecarioDTO # ⚠️ Descomentar esta línea

class BibliotecarioService:
    """
    Servicio para gestionar la lógica de negocio de los Bibliotecarios.
    """
    def __init__(self, repo: BibliotecarioRepository, bcrypt_instance: Bcrypt):
        self.repo = repo
        self.bcrypt = bcrypt_instance 

    def registrar(self, data):
        """Registra un nuevo bibliotecario hasheando su contraseña."""
        
        # ⚠️ Validación: Asegurarse de que el email no esté duplicado antes de hashear
        if self.repo.find_by_email(data["email"]):
             # Es buena práctica lanzar una excepción para que el controlador la capture
             raise ValueError("Ya existe un bibliotecario con este email.")

        password_plano = data["password"]
        hashed_password = self.bcrypt.generate_password_hash(password_plano).decode('utf-8')
        
        bibliotecario = Bibliotecario(
            id_rol=data.get("id_rol", 1), 
            nombre_apellido=data["nombre_apellido"],
            dni=data.get("dni"),
            email=data["email"],
            password=hashed_password, 
            direccion=data.get("direccion"),
            telefono=data.get("telefono"),
            # 🐛 CORRECCIÓN CLAVE: NO pasar id_bibliotecario. El repositorio lo asignará.
            id_bibliotecario=None 
        )
        
        # El repositorio guarda el objeto y asigna el ID (auto-incremento)
        self.repo.save(bibliotecario)
        
        # ✅ Optimización: Devolver el DTO del bibliotecario recién creado
        return BibliotecarioDTO(bibliotecario).to_dict() 

    def listar(self):
        """Lista todos los bibliotecarios y los mapea a DTOs."""
        # 💡 Optimización: Mapear la lista completa a DTOs antes de devolverla
        return [BibliotecarioDTO(b).to_dict() for b in self.repo.find_all()]

    def get_by_id(self, id_bibliotecario):
        """Busca un bibliotecario por su ID y devuelve el DTO."""
        bibliotecario = self.repo.find_by_id(id_bibliotecario)
        if bibliotecario:
             return BibliotecarioDTO(bibliotecario).to_dict()
        return None
    
    # Si quieres que el servicio maneje la autenticación directamente, añade:
    def login(self, email, password):
        """Autentica un bibliotecario usando bcrypt."""
        bibliotecario = self.repo.find_by_email(email)
        if bibliotecario and self.bcrypt.check_password_hash(bibliotecario.password, password):
            return bibliotecario
        return None