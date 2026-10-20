import pytest

from almacenamiento import cargar_inventario, guardar_inventario

def test_guardar_y_cargar_devuelve_lo_mismo(tmp_path):
    ruta = tmp_path / "inv.json"
    inv = {"Interfaz Focusrite": {"precio": 4500, "stock": 3}}
    guardar_inventario(inv, ruta)
    assert cargar_inventario(ruta) == inv

def test_cargar_archivo_inexistente_devuelve_vacio(tmp_path):
    assert cargar_inventario(tmp_path / "no existe.json") == {}

def test_cargar_json_danado_lanza_error(tmp_path):
    ruta = tmp_path / "malo.json"
    ruta.write_text("esto no es json", encoding="utf-8")
    with pytest.raises(ValueError, match="dañado"):
        cargar_inventario(ruta)