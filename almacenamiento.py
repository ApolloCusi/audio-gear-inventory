"""Lectura y escritura del inventario en un archivo JSON."""
import json
from pathlib import Path

def cargar_inventario(ruta):
    """Lee el inventario desde un JSON. Si el archivo no existe, devuelve un inventario vacío."""
    ruta = Path(ruta)
    if not ruta.exists():
        return {}
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError as error:
        raise ValueError(f"El archivo '{ruta}' está dañado o no es JSON válido")

def guardar_inventario(inventario, ruta):
    """Guarda el inventario en un archivo JSON legible."""
    ruta = Path(ruta)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=2, ensure_ascii=False)