from src.model.socio import Socio
from typing import Optional, List

class SocioRepository:
    def __init__(self):
        self._map = {}  # id_socio -> Socio
        self._next_id = 1 # 🆕 Añadir contador

    def save(self, socio: Socio) -> Socio:
        # 🆕 Asignar ID si es un nuevo registro
        if not hasattr(socio, 'id_socio') or socio.id_socio is None:
            socio.id_socio = self._next_id
            self._next_id += 1
            
        self._map[socio.id_socio] = socio
        return socio

    def find_by_id(self, id_socio) -> Optional[Socio]:
        return self._map.get(id_socio)

    def find_by_email(self, email: str) -> Optional[Socio]:
        email_lower = email.lower() # Mejorar la búsqueda (case-insensitive)
        return next((s for s in self._map.values() if s.email.lower() == email_lower), None)

    def find_all(self) -> List[Socio]:
        return list(self._map.values())