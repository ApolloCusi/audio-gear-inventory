"""Lógica del inventario: Funciones que operan sobre un diccionario en memoria."""

def agregar_equipo(inventario, nombre, precio, stock):
    """Agrega un equipo nuevo. Lanza ValueError si los datos son inválidos o ya existe."""
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    if precio < 0 or stock < 0:
        raise ValueError("El precio y el stock no pueden ser negativos")
    if nombre in inventario:
        raise ValueError(f"'{nombre}' ya existe en el inventario")
    inventario[nombre] = {"precio": precio, "stock": stock}


def vender_equipo(inventario, nombre, cantidad):
    """Resta unidades del stock. Lanza ValueError si no existe o no alcanza el stock."""
    if nombre not in inventario:
        raise ValueError(f"'{nombre}' no existe en el inventario")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a 0")
    if inventario[nombre]["stock"] < cantidad:
        raise ValueError(f"Stock insuficiente de '{nombre}' (hay {inventario[nombre]['stock']})")
    inventario[nombre]["stock"] -= cantidad


def valor_total(inventario):
    """Devuelve la suma de precio x stock de todos los equipos."""
    return sum(datos["precio"] * datos["stock"] for datos in inventario.values())


