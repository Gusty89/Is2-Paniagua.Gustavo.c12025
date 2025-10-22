from datetime import date

class Pago:
    def __init__(self, id_pago, fecha_pago=date.today(), monto=0):
        self.id_pago = id_pago
        self.fecha_pago = fecha_pago
        self.monto = monto

    def realizar_pago(self):
        print(f"Pago de {self.monto} realizado en {self.fecha_pago}")
