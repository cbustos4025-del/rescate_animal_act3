"""CONTROLADOR (MVC): coordina Vista y Modelo."""
from refugio.models.usuarios import Reportante, Veterinario, Voluntario
from refugio.patterns.factory import ExpedienteFactory
from refugio.patterns.singleton import GestorCasos


class CasoController:
    def __init__(self, vista):
        self.vista = vista
        self.gestor = GestorCasos()

    def registrar_personal(self, nombre, tipo):
        p = Veterinario(nombre) if tipo == "veterinario" else Voluntario(nombre)
        self.gestor.registrar_personal(p)
        self.vista.mostrar(f"Registrado: {p}")
        return p

    def reportar(self, nombre_reportante, especie, nombre, edad, ubicacion):
        try:
            caso = self.gestor.crear_caso(especie, nombre, edad, ubicacion, Reportante(nombre_reportante))
            self.vista.mostrar(f"Caso creado -> {caso}")
            self.vista.mostrar("Protocolo inicial: " + "; ".join(caso.expediente.protocolo_inicial()))
            return caso
        except ValueError as e:
            self.vista.error(str(e))

    def asignar(self, caso_id, indice_personal):
        try:
            caso = self.gestor.obtener(caso_id)
            caso.asignar(self.gestor.personal[indice_personal])
            self.vista.mostrar(f"Asignado -> {caso}")
        except (KeyError, IndexError) as e:
            self.vista.error(f"Datos inválidos: {e}")

    def cambiar_estado(self, caso_id, estado):
        try:
            caso = self.gestor.obtener(caso_id)
            caso.cambiar_estado(estado)
            self.vista.mostrar(f"Actualizado -> {caso}")
            if caso.estado.nombre == "En Adopción":
                self.vista.mostrar("Requisitos: " + "; ".join(caso.expediente.requisitos_adopcion()))
        except Exception as e:
            self.vista.error(str(e))

    def listar(self):
        self.vista.listar_casos(self.gestor.listar())

    def historial(self, caso_id):
        try:
            self.vista.mostrar("\n".join(self.gestor.obtener(caso_id).historial))
        except KeyError as e:
            self.vista.error(str(e))

    def notificaciones(self):
        for p in self.gestor.personal:
            self.vista.mostrar(f"{p}: {len(p.notificaciones)} notificación(es)")
            for n in p.notificaciones:
                self.vista.mostrar(f"   {n}")

    def especies(self):
        return ExpedienteFactory.especies()
