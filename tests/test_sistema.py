import unittest

from refugio.models.usuarios import Reportante, Voluntario
from refugio.patterns.factory import ExpedienteFactory
from refugio.patterns.singleton import GestorCasos
from refugio.patterns.state import TransicionInvalida


class PruebasRefugio(unittest.TestCase):
    def setUp(self):
        GestorCasos.reiniciar()
        self.g = GestorCasos()

    def test_singleton(self):
        self.assertIs(GestorCasos(), GestorCasos())

    def test_factory(self):
        self.assertEqual(ExpedienteFactory.crear("gato", "Luna").especie, "Gato")
        with self.assertRaises(ValueError):
            ExpedienteFactory.crear("dragon", "X")

    def test_observer(self):
        v = Voluntario("Ana")
        self.g.registrar_personal(v)
        self.g.crear_caso("perro", "Max", 2, "Parque", Reportante("Carlos"))
        self.assertEqual(len(v.notificaciones), 1)

    def test_state_valido_e_invalido(self):
        v = Voluntario("Ana")
        c = self.g.crear_caso("perro", "Max", 2, "Parque", Reportante("Carlos"))
        with self.assertRaises(TransicionInvalida):
            c.cambiar_estado("Adoptado")
        with self.assertRaises(ValueError):   # sin responsable
            c.cambiar_estado("En Tratamiento")
        c.asignar(v)
        c.cambiar_estado("En Tratamiento")
        self.assertEqual(c.estado.nombre, "En Tratamiento")
        self.assertGreaterEqual(len(c.historial), 3)


if __name__ == "__main__":
    unittest.main()
