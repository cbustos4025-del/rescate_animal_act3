"""Productos del Factory Method: un expediente distinto por especie."""
from abc import ABC, abstractmethod


class Expediente(ABC):
    especie = ""

    def __init__(self, nombre: str, edad_aprox: int = 0, **extra):
        self.nombre = nombre
        self.edad_aprox = edad_aprox
        self.extra = extra

    @abstractmethod
    def protocolo_inicial(self) -> list[str]: ...

    @abstractmethod
    def requisitos_adopcion(self) -> list[str]: ...

    def __str__(self):
        return f"{self.especie}: {self.nombre} (~{self.edad_aprox} años)"


class ExpedientePerro(Expediente):
    especie = "Perro"

    def protocolo_inicial(self):
        return ["Desparasitación", "Vacuna múltiple y antirrábica", "Chequeo general"]

    def requisitos_adopcion(self):
        return ["Cédula del adoptante", "Espacio adecuado", "Compromiso de esterilización"]


class ExpedienteGato(Expediente):
    especie = "Gato"

    def protocolo_inicial(self):
        return ["Prueba FIV/FeLV", "Desparasitación", "Vacuna triple felina"]

    def requisitos_adopcion(self):
        return ["Cédula del adoptante", "Mallas en ventanas/balcones", "Compromiso de esterilización"]


class ExpedienteFauna(Expediente):
    especie = "Fauna Silvestre"

    def protocolo_inicial(self):
        return ["Evaluación por veterinario especializado", "Aviso a la autoridad ambiental",
                "Cuarentena y manejo mínimo"]

    def requisitos_adopcion(self):
        return ["NO apto para adopción: liberación o centro autorizado (Ministerio del Ambiente)"]
