"""Patrón OBSERVER: notificaciones automáticas a voluntarios ante nuevos rescates."""
from abc import ABC, abstractmethod


class Observador(ABC):
    """Interfaz de quien desea ser notificado (ISP / DIP)."""

    @abstractmethod
    def actualizar(self, evento: str, caso) -> None: ...


class Notificador:
    """Sujeto observable. Mantiene suscriptores y los notifica."""

    def __init__(self):
        self._observadores: list[Observador] = []

    def suscribir(self, obs: Observador) -> None:
        if obs not in self._observadores:
            self._observadores.append(obs)

    def desuscribir(self, obs: Observador) -> None:
        if obs in self._observadores:
            self._observadores.remove(obs)

    def notificar(self, evento: str, caso) -> None:
        for obs in list(self._observadores):
            obs.actualizar(evento, caso)

    @property
    def total(self) -> int:
        return len(self._observadores)
