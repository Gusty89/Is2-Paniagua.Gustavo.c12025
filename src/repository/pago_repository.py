class PagoRepository:
    def __init__(self):
        self._map = {}
        self._next = 1

    def save(self, pago):
        pago.id_pago = self._next
        self._next += 1
        self._map[pago.id_pago] = pago
        return pago

    def find_all(self):
        return list(self._map.values())
