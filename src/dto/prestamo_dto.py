class PrestamoDTO:
    def __init__(self, prestamo):
        self.id_prestamo = prestamo.id_prestamo
        self.id_libro = prestamo.id_libro
        self.id_socio = prestamo.id_socio
        self.fecha_prestamo = str(prestamo.fecha_prestamo)
        self.fecha_devolucion = str(prestamo.fecha_devolucion) if prestamo.fecha_devolucion else None
        self.estado = prestamo.estado

    def to_dict(self):
        return vars(self)
