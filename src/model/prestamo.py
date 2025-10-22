from datetime import date

class EstadoPrestamo:
    ACTIVO = "ACTIVO"
    DEVUELTO = "DEVUELTO"

class Prestamo:
    def __init__(self, id_prestamo, fecha_prestamo=date.today(), fecha_devolucion=None, estado=EstadoPrestamo.ACTIVO):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def registrar_prestamo(self, libro):
        libro.prestar_libro()
