"""Punto de entrada. Uso:  python main.py          (menú interactivo)
                          python main.py --demo   (demostración automática)"""
import sys

from refugio.controllers.caso_controller import CasoController
from refugio.views.consola_view import ConsolaView


def demo(c: CasoController):
    c.registrar_personal("Ana Mora", "voluntario")
    c.registrar_personal("Dr. Luis Vera", "veterinario")
    c.reportar("Carlos Pico", "perro", "Max", 3, "Parque La Rotonda")
    c.reportar("María Zambrano", "gato", "Luna", 1, "Mercado Central")
    c.reportar("Pedro Loor", "fauna", "Mono aullador", 5, "Vía Portoviejo-Crucita")
    c.asignar(1, 1)
    c.cambiar_estado(1, "En Adopción")   # transición inválida (State)
    c.cambiar_estado(1, "En Tratamiento")
    c.cambiar_estado(1, "En Adopción")
    c.listar()
    c.historial(1)
    c.notificaciones()


def interactivo(c: CasoController, v: ConsolaView):
    while True:
        op = v.menu()
        if op == "0":
            break
        elif op == "1":
            c.registrar_personal(v.pedir("Nombre: "), v.pedir("Tipo (voluntario/veterinario): ").lower())
        elif op == "2":
            esp = v.pedir(f"Especie ({'/'.join(c.especies())}): ")
            edad = v.pedir("Edad aprox. (años): ")
            c.reportar(v.pedir("Su nombre: "), esp, v.pedir("Nombre del animal: "),
                       int(edad) if edad.isdigit() else 0, v.pedir("Ubicación: "))
        elif op == "3":
            for i, p in enumerate(c.gestor.personal):
                v.mostrar(f"  {i}. {p}")
            cid, idx = v.pedir("ID caso: "), v.pedir("N° de responsable: ")
            if cid.isdigit() and idx.isdigit():
                c.asignar(int(cid), int(idx))
            else:
                v.error("Ingrese números")
        elif op == "4":
            cid = v.pedir("ID caso: ")
            est = v.pedir("Nuevo estado (En Tratamiento / En Adopción / Adoptado): ")
            c.cambiar_estado(int(cid), est) if cid.isdigit() else v.error("Ingrese un número")
        elif op == "5":
            c.listar()
        elif op == "6":
            cid = v.pedir("ID caso: ")
            c.historial(int(cid)) if cid.isdigit() else v.error("Ingrese un número")
        elif op == "7":
            c.notificaciones()
        else:
            v.error("Opción inválida")


if __name__ == "__main__":
    vista = ConsolaView()
    ctrl = CasoController(vista)
    demo(ctrl) if "--demo" in sys.argv else interactivo(ctrl, vista)
