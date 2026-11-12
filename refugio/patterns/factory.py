"""Patrón FACTORY METHOD: creación de expedientes según la especie.
Registro extensible: agregar una especie no modifica código existente (OCP)."""
from refugio.models.expedientes import (Expediente, ExpedienteFauna,
                                        ExpedienteGato, ExpedientePerro)


class ExpedienteFactory:
    _registro: dict[str, type[Expediente]] = {
        "perro": ExpedientePerro,
        "gato": ExpedienteGato,
        "fauna": ExpedienteFauna,
    }

    @classmethod
    def registrar(cls, clave: str, tipo: type[Expediente]) -> None:
        cls._registro[clave.lower()] = tipo

    @classmethod
    def crear(cls, especie: str, nombre: str, edad_aprox: int = 0, **extra) -> Expediente:
        tipo = cls._registro.get(especie.lower())
        if tipo is None:
            raise ValueError(f"Especie no soportada: {especie}. Opciones: {', '.join(cls._registro)}")
        return tipo(nombre, edad_aprox, **extra)

    @classmethod
    def especies(cls) -> list[str]:
        return list(cls._registro)
