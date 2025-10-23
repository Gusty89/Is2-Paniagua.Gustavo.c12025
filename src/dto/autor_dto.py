from src.model.autor import Autor
# Asumo que el modelo Autor está en src.model.autor

class AutorDTO:
    """
    Data Transfer Object (DTO) para la entidad Autor.
    Se utiliza para serializar una instancia del modelo 'Autor' a un diccionario
    seguro y estandarizado para ser enviado como respuesta JSON.
    """
    
    def __init__(self, autor: Autor):
        """
        Inicializa el DTO extrayendo los atributos clave del objeto Autor.
        """
        # Mapping de atributos
        self.id_autor = autor.id_autor
        self.nombre_apellido = autor.nombre_apellido
        self.nacionalidad = autor.nacionalidad

    def to_dict(self):
        """
        Convierte la instancia del DTO a un diccionario serializable en JSON.
        """
        return {
            "id_autor": self.id_autor, 
            "nombre_apellido": self.nombre_apellido, 
            "nacionalidad": self.nacionalidad
        }