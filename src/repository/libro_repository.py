from src.model.libro import Libro

class LibroRepository:
    def __init__(self):
        self._map = {}
        self._next_id = 1 # Contador para auto-incremento

    def save(self, libro):
        # Si el libro NO tiene ID, asigna uno nuevo
        if not hasattr(libro, 'id_libro') or libro.id_libro is None:
            libro.id_libro = self._next_id
            self._next_id += 1
            
        self._map[libro.id_libro] = libro
        return libro
    def find_all(self):
        """Devuelve una lista de todos los libros."""
        return list(self._map.values())
    
    def find_by_id(self, id_):
        """Busca un libro por su ID."""
        return self._map.get(id_)
    
    def find_by_isbn(self, isbn: str):
        """Busca un libro por su número ISBN."""
        for libro in self._map.values():
            if libro.isbn == isbn:
                return libro
        return None