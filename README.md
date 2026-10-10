# Componentes y Librerías Reutilizables (Tkinter & Python)

Este repositorio contiene una implementación modular en Python y Tkinter que demuestra cómo diseñar, organizar, empaquetar y consumir componentes reutilizables (tanto visuales como no visuales) siguiendo los estándares modernos de empaquetado (`pyproject.toml`).

## Objetivos
- Diferenciar claramente entre componentes, paquetes y librerías en desarrollo de software.
- Crear un componente visual reutilizable (`ValidatedEntry`) para validación de datos en tiempo real.
- Crear un componente no visual utilitario (`slugifier`) independiente de la interfaz gráfica.
- Empaquetar la solución localmente para ser consumida como un módulo importable en otras aplicaciones.

## Estructura del Repositorio
```text
guiutils-project/
│
├── guiutils/              
│   ├── __init__.py        
│   ├── validated_entry.py 
│   └── slugifier.py       
│
├── demo.py               
├── pyproject.toml         
└── README.md              
