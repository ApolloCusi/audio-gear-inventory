# Audio Gear Inventory

Herramienta de línea de comandos para llevar el inventario de equipo de audio: agregar equipos, registrar ventas, eliminar, listar y generar reportes con alertas de stock bajo. Los datos se guardan en un archivo JSON.

## Instalación
```bash
git clone https://github.com/ApolloCusi/audio-gear-inventory.git
cd audio-gear-inventory
pip install -r requirements.txt
```

## Uso
```bash
python main.py agregar "Interfaz Focusrite" --precio 4500 --stock 3
python main.py vender "Interfaz Focusrite" --cantidad 1
python main.py listar
python main.py reporte --umbral 2
python main.py eliminar "Interfaz Focusrite"
```

## Pruebas
```bash
python -m pytest -v
```

## Estructura
- `inventario.py`: lógica del inventario (agregar, vender, eliminar, reportes)
- `almacenamiento.py`: lectura y escritura del archivo JSON
- `main.py`: interfaz de línea de comandos
- `tests/`: pruebas automáticas con pytest

## Decisiones de diseño
- La lógica lanza errores (`ValueError`) y la interfaz decide cómo mostrarlos, así la lógica se puede probar sin imprimir nada.
- Los datos (`inventario.json`) no se suben al repositorio.

## ¿Por qué lo construí?
Como productor e ingeniero, necesitaba una forma simple de controlar mi equipo y mi stock. Lo construí también para practicar manejo de archivos, pruebas automáticas y diseño de herramientas de terminal en Python.