from datetime import datetime
from itertools import count

from refugio.patterns.state import EstadoCaso, Rescatado

_ids = count(1)


class CasoRescate:
    def __init__(self, expediente, reportante, ubicacion: str):
        self.id = next(_ids)
        self.expediente = expediente
        self.reportante = reportante
        self.ubicacion = ubicacion
        self.responsable = None
        self.estado: EstadoCaso = Rescatado()
        self.historial: list[str] = []
        self._log("Caso creado en estado Rescatado")

    def _log(self, texto: str) -> None:  # trazabilidad
        self.historial.append(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {texto}")

    def _set_estado(self, nuevo: EstadoCaso) -> None:
        self._log(f"Estado: {self.estado} -> {nuevo}")
        self.estado = nuevo

    def asignar(self, responsable) -> None:
        self.responsable = responsable
        self._log(f"Responsable asignado: {responsable}")

    def cambiar_estado(self, destino: str) -> None:
        if destino == "En Tratamiento" and self.responsable is None:
            raise ValueError("Debe asignar un responsable antes de iniciar el tratamiento")
        self.estado.transicionar(self, destino)

    def __str__(self):
        resp = self.responsable.nombre if self.responsable else "Sin asignar"
        return f"#{self.id} | {self.expediente} | {self.estado} | Resp: {resp} | {self.ubicacion}"
