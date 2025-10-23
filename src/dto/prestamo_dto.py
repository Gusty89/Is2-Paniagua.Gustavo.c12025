from src.model.prestamo import Prestamo
# Asumo que el modelo Prestamo está en src.model.prestamo

class PrestamoDTO:
    """
    Data Transfer Object (DTO) para la entidad Préstamo.
    Serializa la instancia del modelo 'Prestamo' a un formato JSON seguro y estandarizado.
    """
    
    def __init__(self, prestamo: Prestamo):
        """
        Inicializa el DTO extrayendo y formateando los atributos del objeto Prestamo.
        """
        self.id_prestamo = prestamo.id_prestamo
        self.id_libro = prestamo.id_libro
        self.id_socio = prestamo.id_socio
        # Convierte la fecha obligatoria a string
        self.fecha_prestamo = str(prestamo.fecha_prestamo)
        
        # Gestión del campo opcional: 
        # Si existe, lo convierte a string; si no (es None), mantiene None.
        self.fecha_devolucion = str(prestamo.fecha_devolucion) if prestamo.fecha_devolucion else None
        
        # Asumiendo que 'estado' ya es un string o un valor serializable (o Enum.value)
        self.estado = prestamo.estado 

    def to_dict(self):
        """
        Convierte la instancia del DTO a un diccionario serializable en JSON.
        El uso de vars(self) devuelve de forma concisa todos los atributos del DTO.
        """
        return vars(self)