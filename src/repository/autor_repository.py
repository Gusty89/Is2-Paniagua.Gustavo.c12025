from src.model.autor import Autor # Importa tu modelo Autor

class AutorRepository:
    def __init__(self):
        self._list = []
        self._next = 1

    def save(self, autor):
        # Mejora: Asegurar que el objeto es de la clase Autor
        if not isinstance(autor, Autor):
            raise TypeError("El objeto a guardar debe ser una instancia de Autor.")
            
        autor.id_autor = self._next
        self._next += 1
        self._list.append(autor)
        return autor
    
    def find_all(self):
        """Devuelve una lista de todos los autores."""
        return self._list
    
    def find_by_id(self, id_):
        """Busca un autor por su ID."""
        for autor in self._list:
            if autor.id_autor == id_:
                return autor
        return None
    