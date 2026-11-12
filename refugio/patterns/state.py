"""Patrón STATE: ciclo de vida del caso (Rescatado -> En Tratamiento -> En Adopción -> Adoptado)."""
from abc import ABC


class TransicionInvalida(Exception):
    pass


class EstadoCaso(ABC):
    nombre = ""
    permitidos: tuple[str, ...] = ()

    def transicionar(self, caso, destino: str) -> None:
        if destino not in self.permitidos:
            raise TransicionInvalida(
                f"No se puede pasar de '{self.nombre}' a '{destino}'. "
                f"Permitidos: {', '.join(self.permitidos) or 'ninguno'}"
            )
        caso._set_estado(crear_estado(destino))

    def __str__(self):
        return self.nombre


class Rescatado(EstadoCaso):
    nombre = "Rescatado"
    permitidos = ("En Tratamiento",)


class EnTratamiento(EstadoCaso):
    nombre = "En Tratamiento"
    permitidos = ("En Adopción",)


class EnAdopcion(EstadoCaso):
    nombre = "En Adopción"
    permitidos = ("Adoptado", "En Tratamiento")


class Adoptado(EstadoCaso):
    nombre = "Adoptado"
    permitidos = ()


_ESTADOS = {c.nombre: c for c in (Rescatado, EnTratamiento, EnAdopcion, Adoptado)}


def crear_estado(nombre: str) -> EstadoCaso:
    if nombre not in _ESTADOS:
        raise TransicionInvalida(f"Estado desconocido: {nombre}")
    return _ESTADOS[nombre]()
