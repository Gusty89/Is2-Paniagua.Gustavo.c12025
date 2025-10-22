class AutorRepository:
    def __init__(self):
        self._list = []
        self._next = 1

    def save(self, autor):
        autor.id_autor = self._next
        self._next += 1
        self._list.append(autor)
        return autor

    def find_all(self):
        return self._list

    def find_by_id(self, id_autor):
        return next((a for a in self._list if a.id_autor == id_autor), None)
