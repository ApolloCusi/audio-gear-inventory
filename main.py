"""Interfaz de línea de comandos del inventario de equipo de audio."""
import argparse
import sys 

from almacenamiento import cargar_inventario, guardar_inventario
from inventario import agregar_equipo, vender_equipo

RUTA_DATOS = "inventario.json"

def crear_parser():
    parser = argparse.ArgumentParser(description="Inventario de equipo de audio")
    parser.add_argument("--archivo", default=RUTA_DATOS, help="Ruta del archivo JSON de datos")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    p_agregar = subparsers.add_parser("agregar", help="Agrega un equipo nuevo")
    p_agregar.add_argument("nombre", help="Nombre del equipo (entre comillas si tiene espacios)")
    p_agregar.add_argument("--precio", type=float, required=True)
    p_agregar.add_argument("--stock", type=int, required=True)

    p_vender = subparsers.add_parser("vender", help="Registra una venta")
    p_vender.add_argument("nombre", help="Nombre del equipo")
    p_vender.add_argument("--cantidad", type=int, default=1)

    subparsers.add_parser("listar", help="Muestra el inventario")

    return parser

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío")
        return
    print(f"{'Equipo':<25}{'Precio':>10}{'Stock':>8}")
    print("-" * 43)
    for nombre, datos in sorted(inventario.items()):
        print(f"{nombre:<25}{datos['precio']:>10.2f}{datos['stock']:>8}")

def main():
    args = crear_parser().parse_args()

    try:
        inventario = cargar_inventario(args.archivo)

        if args.comando == "agregar":
            agregar_equipo(inventario, args.nombre, args.precio, args.stock)
            guardar_inventario(inventario, args.archivo)
            print(f"Agregado: {args.nombre.strip()}")
        elif args.comando == "vender":
            vender_equipo(inventario, args.nombre, args.cantidad)
            guardar_inventario(inventario, args.archivo)
            print(f"Venta registrada: {args.cantidad} x {args.nombre}")
        elif args.comando == "listar":
            mostrar_inventario(inventario)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
