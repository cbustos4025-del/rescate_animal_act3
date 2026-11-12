"""Actores del sistema: Reportante, Voluntario, Veterinario, Administrador."""
from refugio.patterns.observer import Observador


class Persona:
    def __init__(self, nombre: str, contacto: str = ""):
        self.nombre = nombre
        self.contacto = contacto

    @property
    def rol(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol})"


class Reportante(Persona):
    """Ciudadano que reporta un animal en situación de rescate."""


class Voluntario(Persona, Observador):
    """Recibe notificaciones (Observer) y puede ser responsable de un caso."""

    def __init__(self, nombre: str, contacto: str = ""):
        super().__init__(nombre, contacto)
        self.notificaciones: list[str] = []

    def actualizar(self, evento: str, caso) -> None:
        msg = f"[{evento}] Caso #{caso.id}: {caso.expediente.especie} en {caso.ubicacion}"
        self.notificaciones.append(msg)


class Veterinario(Voluntario):
    def __init__(self, nombre: str, contacto: str = "", especialidad: str = "General"):
        super().__init__(nombre, contacto)
        self.especialidad = especialidad


class Administrador(Persona):
    """Gestiona el refugio: registra personal y supervisa los casos."""
