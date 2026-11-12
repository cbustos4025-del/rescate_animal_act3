"""Patrón SINGLETON: instancia única del motor de gestión de casos (y su 'conexión a datos')."""
import threading

from refugio.models.caso import CasoRescate
from refugio.patterns.factory import ExpedienteFactory
from refugio.patterns.observer import Notificador


class GestorCasos:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:  # doble verificación: seguro con hilos
                if cls._instancia is None:
                    inst = super().__new__(cls)
                    inst._inicializar()
                    cls._instancia = inst
        return cls._instancia

    def _inicializar(self):
        self._casos: dict[int, CasoRescate] = {}   # repositorio en memoria
        self.notificador = Notificador()
        self.personal: list = []

    @classmethod
    def reiniciar(cls):
        """Solo para pruebas."""
        cls._instancia = None

    def registrar_personal(self, voluntario) -> None:
        self.personal.append(voluntario)
        self.notificador.suscribir(voluntario)          # Observer

    def crear_caso(self, especie, nombre, edad, ubicacion, reportante) -> CasoRescate:
        expediente = ExpedienteFactory.crear(especie, nombre, edad)   # Factory
        caso = CasoRescate(expediente, reportante, ubicacion)
        self._casos[caso.id] = caso
        self.notificador.notificar("NUEVO RESCATE", caso)             # Observer
        return caso

    def obtener(self, caso_id: int) -> CasoRescate:
        if caso_id not in self._casos:
            raise KeyError(f"No existe el caso #{caso_id}")
        return self._casos[caso_id]

    def listar(self) -> list[CasoRescate]:
        return list(self._casos.values())
