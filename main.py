"""Interfaz de línea de comandos del inventario de equipo de audio."""
import argparse
import sys

from almacenamiento import cargar_inventario, guardar_inventario
from inventario import (
    agregar_equipo,
    eliminar_equipo,
    equipos_con_stock_bajo,
    valor_total,
    vender_equipo,
)

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

    p_eliminar = subparsers.add_parser("eliminar", help="Elimina un equipo del inventario")
    p_eliminar.add_argument("nombre", help="Nombre del equipo")

    subparsers.add_parser("listar", help="Muestra el inventario")

    p_reporte = subparsers.add_parser("reporte", help="Muestra un resumen del inventario")
    p_reporte.add_argument("--umbral", type=int, default=2, help="Stock considerado bajo (por defecto 2)")

    return parser


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío")
        return
    print(f"{'Equipo':<25}{'Precio':>10}{'Stock':>8}")
    print("-" * 43)
    for nombre, datos in sorted(inventario.items()):
        print(f"{nombre:<25}{datos['precio']:>10.2f}{datos['stock']:>8}")


def mostrar_reporte(inventario, umbral):
    print(f"Equipos distintos: {len(inventario)}")
    print(f"Unidades totales: {sum(datos['stock'] for datos in inventario.values())}")
    print(f"Valor total del inventario: ${valor_total(inventario):,.2f}")

    if inventario:
        mas_caro = max(inventario, key=lambda nombre: inventario[nombre]["precio"])
        print(f"Equipo más caro: {mas_caro} (${inventario[mas_caro]['precio']:,.2f})")

    bajos = equipos_con_stock_bajo(inventario, umbral)
    if bajos:
        print(f"\nStock bajo (<= {umbral}):")
        for nombre, datos in bajos.items():
            print(f"  - {nombre}: {datos['stock']} unidad(es)")
    else:
        print(f"\nNingún equipo con stock <= {umbral}")


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
        elif args.comando == "eliminar":
            eliminar_equipo(inventario, args.nombre)
            guardar_inventario(inventario, args.archivo)
            print(f"Eliminado: {args.nombre}")
        elif args.comando == "listar":
            mostrar_inventario(inventario)
        elif args.comando == "reporte":
            mostrar_reporte(inventario, args.umbral)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
