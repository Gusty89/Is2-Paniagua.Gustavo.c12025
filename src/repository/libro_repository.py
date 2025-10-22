class LibroRepository:
    def __init__(self):
        self._map = {}

    def save(self, libro):
        self._map[libro.id_libro] = libro
        return libro

    def find_by_id(self, id_libro):
        return self._map.get(id_libro)

    def find_all(self):
        return list(self._map.values())
