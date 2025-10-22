class SocioRepository:
    def __init__(self):
        self._map = {}  # id_socio -> Socio

    def save(self, socio):
        self._map[socio.id_socio] = socio
        return socio

    def find_by_id(self, id_socio):
        return self._map.get(id_socio)

    def find_by_email(self, email):
        return next((s for s in self._map.values() if s.email == email), None)

    def find_all(self):
        return list(self._map.values())
