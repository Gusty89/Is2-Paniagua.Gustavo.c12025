class PrestamoRepository:
    def __init__(self):
        self._map = {}
        self._next = 1

    def save(self, prestamo):
        prestamo.id_prestamo = self._next
        self._next += 1
        self._map[prestamo.id_prestamo] = prestamo
        return prestamo

    def find_by_id(self, id_):
        return self._map.get(id_)

    def find_all(self):
        return list(self._map.values())
