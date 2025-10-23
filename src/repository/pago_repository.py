from src.model.pago import Pago
from typing import Optional, List

class PagoRepository:
    def __init__(self):
        self._map = {}
        self._next = 1

    def save(self, pago: Pago) -> Pago:
        # Asigna el ID si es un nuevo registro
        if not hasattr(pago, 'id_pago') or pago.id_pago is None:
            pago.id_pago = self._next
            self._next += 1
            
        self._map[pago.id_pago] = pago
        return pago

    def find_all(self) -> List[Pago]:
        return list(self._map.values())

    def find_by_id(self, id_pago) -> Optional[Pago]:
        """Busca un pago por su ID único."""
        return self._map.get(id_pago)
    
    def find_by_socio_id(self, id_socio: int) -> List[Pago]:
        """
        Busca y devuelve todos los pagos realizados por un socio específico.
        """
        # Itera sobre los valores y filtra por id_socio
        return [p for p in self._map.values() if p.id_socio == id_socio]