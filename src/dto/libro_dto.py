from src.model.libro import Libro
# Asumo que el modelo Libro está en src.model.libro

class LibroDTO:
    """
    Data Transfer Object (DTO) para la entidad Libro.
    Serializa la instancia del modelo 'Libro' a un formato JSON seguro y estandarizado.
    """
    
    def __init__(self, libro: Libro):
        """
        Inicializa el DTO extrayendo los atributos clave del objeto Libro.
        """
        self.id_libro = libro.id_libro
        self.titulo = libro.titulo
        self.isbn = libro.isbn
        # Convierte el valor del Enum a su valor simple (string o int)
        # Esto es crucial para la serialización JSON.
        self.estado = libro.estado.value 

    def to_dict(self):
        """
        Convierte la instancia del DTO a un diccionario serializable en JSON.
        """
        return {
            "id_libro": self.id_libro, 
            "titulo": self.titulo, 
            "isbn": self.isbn, 
            "estado": self.estado
        }