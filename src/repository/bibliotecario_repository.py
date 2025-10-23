from src.model.bibliotecario import Bibliotecario
# Asumo que el modelo Bibliotecario está importado

class BibliotecarioRepository:
    def __init__(self):
        self._map = {}
        # Puedes añadir un contador si no usas UUIDs
        self._next_id = 1 

    def save(self, bibliotecario: Bibliotecario):
        # Asignación de ID si no tiene (simulando autoincremento de BBDD)
        if not hasattr(bibliotecario, 'id_bibliotecario') or bibliotecario.id_bibliotecario is None:
            bibliotecario.id_bibliotecario = self._next_id
            self._next_id += 1
            
        self._map[bibliotecario.id_bibliotecario] = bibliotecario
        return bibliotecario

    def find_all(self):
        """Devuelve una lista de todos los objetos Bibliotecario."""
        # Devuelve solo los valores del diccionario
        return list(self._map.values())

    def find_by_id(self, id_):
        """Busca un bibliotecario por su ID."""
        return self._map.get(id_)
    
    def find_by_email(self, email: str):
        """
        Busca un bibliotecario por su dirección de email (usado para login).
        Como es un diccionario, debemos iterar sobre los valores.
        """
        email_lower = email.lower()
        for bibliotecario in self._map.values():
            if bibliotecario.email.lower() == email_lower:
                return bibliotecario
        return None