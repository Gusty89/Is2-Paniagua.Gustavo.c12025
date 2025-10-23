from src.model.pago import Pago
# Asumo que el modelo Pago está en src.model.pago

class PagoDTO:
    """
    Data Transfer Object (DTO) para la entidad Pago.
    Serializa la instancia del modelo 'Pago' a un formato JSON seguro y estandarizado.
    """
    
    def __init__(self, pago: Pago):
        """
        Inicializa el DTO extrayendo y formateando los atributos del objeto Pago.
        """
        self.id_pago = pago.id_pago
        self.monto = pago.monto
        # Es CORRECTO convertir la fecha a string, ya que los objetos datetime no son serializables directamente a JSON.
        self.fecha_pago = str(pago.fecha_pago) 
        self.id_socio = pago.id_socio

    def to_dict(self):
        """
        Convierte la instancia del DTO a un diccionario serializable en JSON.
        
        El uso de vars(self) es una forma concisa de devolver un diccionario 
        que contiene todos los atributos del objeto DTO.
        """
        return vars(self)