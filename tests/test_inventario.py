import pytest

from inventario import (
    agregar_equipo,
    eliminar_equipo,
    equipos_con_stock_bajo,
    valor_total,
    vender_equipo,
)

def test_agregar_equipo_nuevo():
    inv = {}
    agregar_equipo(inv, "Monitor KRK", 7800, 2)
    assert inv["Monitor KRK"] == {"precio": 7800, "stock": 2}

def test_agregar_limpia_espacios_del_nombre():
    inv = {}
    agregar_equipo(inv, " Monitor KRK ", 7800, 2)
    assert "Monitor KRK" in inv

def test_agregar_equipo_duplicado_lanza_error():
    inv = {"Monitor KRK": {"precio": 7800, "stock": 2}}
    with pytest.raises(ValueError, match="ya existe"):
        agregar_equipo(inv, "Monitor KRK", 7800, 1)

def test_agregar_precio_negativo_lanza_error():
    with pytest.raises(ValueError, match="negativos"):
        agregar_equipo({}, "Mic SM7B", -5, 1)

def test_vender_reduce_stock():
    inv = {"Mic SM7B": {"precio": 6200, "stock": 5}}
    vender_equipo(inv, "Mic SM7B", 2)
    assert inv["Mic SM7B"]["stock"] == 3

def test_vender_stock_insuficiente_lanza_error():
    inv = {"Mic SM7B": {"precio": 6200, "stock": 1}}
    with pytest.raises(ValueError, match="Stock insuficiente"):
        vender_equipo(inv, "Mic SM7B", 3)
    assert inv["Mic SM7B"]["stock"] == 1 # el stock no debe haber cambiado

def test_vender_equipo_inexistente_lanza_error():
    with pytest.raises(ValueError, match="no existe"):
        vender_equipo({}, "Fantasma", 1)

def test_valor_total():
    inv = {
        "A": {"precio": 100, "stock": 2},
        "B": {"precio": 50, "stock": 4}
    }
    assert valor_total(inv) == 400

def test_valor_total_inventario_vacío():
    assert valor_total({}) == 0

def test_vender_todo_el_stock_deja_cero():
    inv = {"Mic SM7B": {"precio": 6200, "stock": 2}}
    vender_equipo(inv, "Mic SM7B", 2)
    assert inv["Mic SM7B"]["stock"] == 0

def test_eliminar_equipo():
    inv = {"A": {"precio": 10, "stock": 1}}
    eliminar_equipo(inv, "A")
    assert inv == {}

def test_eliminar_equipo_inexistente_lanza_error():
    with pytest.raises(ValueError, match="no existe"):
        eliminar_equipo({}, "A")


def test_equipos_con_stock_bajo():
    inv = {
        "A": {"precio": 10, "stock": 1},
        "B": {"precio": 10, "stock": 5},
        "C": {"precio": 10, "stock": 2},
    }
    assert equipos_con_stock_bajo(inv, umbral=2) == {
        "A": {"precio": 10, "stock": 1},
        "C": {"precio": 10, "stock": 2},
    }
