class BibliotecarioRepository:
    def __init__(self):
        self._map = {}

    def save(self, bibliotecario):
        self._map[bibliotecario.id_bibliotecario] = bibliotecario
        return bibliotecario

    def find_by_id(self, id_):
        return self._map.get(id_)
