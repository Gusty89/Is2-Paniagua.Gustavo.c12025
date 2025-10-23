from src.model.prestamo import Prestamo
from typing import List, Optional

class PrestamoRepository:
    def __init__(self):
        self._map = {}
        self._next = 1

    def save(self, prestamo: Prestamo) -> Prestamo:
        # Asigna ID si es un nuevo registro
        if not hasattr(prestamo, 'id_prestamo') or prestamo.id_prestamo is None:
            prestamo.id_prestamo = self._next
            self._next += 1
            
        self._map[prestamo.id_prestamo] = prestamo
        return prestamo

    def find_by_id(self, id_) -> Optional[Prestamo]:
        """Busca un préstamo por su ID."""
        return self._map.get(id_)

    def find_all(self) -> List[Prestamo]:
        """Devuelve una lista de todos los préstamos."""
        return list(self._map.values())

    def find_by_socio_id(self, id_socio: int) -> List[Prestamo]:
        """
        Busca todos los préstamos asociados a un Socio específico.
        """
        return [p for p in self._map.values() if p.id_socio == id_socio]

    def find_by_libro_id(self, id_libro: int) -> List[Prestamo]:
        """
        Busca todos los préstamos asociados a un Libro específico.
        """
        return [p for p in self._map.values() if p.id_libro == id_libro]