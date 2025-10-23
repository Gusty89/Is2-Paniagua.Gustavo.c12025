from src.dto.pago_dto import PagoDTO
from src.model.pago import Pago

class PagoService:
    def __init__(self, repo_pago, repo_socio):
        self.repo_pago = repo_pago
        self.repo_socio = repo_socio

    def crear(self, data):
        pago = Pago(id_pago=None, monto=data["monto"], id_socio=data["id_socio"])
        saved = self.repo_pago.save(pago)
        socio = self.repo_socio.find_by_id(pago.id_socio)
        if socio:
            socio.pagos.append(saved)
        return PagoDTO(saved).to_dict()

    def listar(self):
        return [PagoDTO(p).to_dict() for p in self.repo_pago.find_all()]
