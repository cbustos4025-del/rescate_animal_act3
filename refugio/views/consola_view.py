"""VISTA (MVC): solo entrada/salida por consola, sin lógica de negocio."""


class ConsolaView:
    def mostrar(self, texto: str) -> None:
        print(texto)

    def error(self, texto: str) -> None:
        print(f"[ERROR] {texto}")

    def listar_casos(self, casos) -> None:
        if not casos:
            print("No hay casos registrados.")
        for c in casos:
            print(c)

    def pedir(self, mensaje: str) -> str:
        return input(mensaje).strip()

    def menu(self) -> str:
        print("""
===== REFUGIO ANIMAL =====
1. Registrar voluntario/veterinario
2. Reportar rescate
3. Asignar responsable a caso
4. Cambiar estado de caso
5. Listar casos
6. Ver historial (trazabilidad)
7. Ver notificaciones
0. Salir""")
        return self.pedir("Opción: ")
