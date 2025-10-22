class PagoDTO:
    def __init__(self, pago):
        self.id_pago = pago.id_pago
        self.monto = pago.monto
        self.fecha_pago = str(pago.fecha_pago)
        self.id_socio = pago.id_socio

    def to_dict(self):
        return vars(self)
