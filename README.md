# LangGraph Base Project

Base limpia para empezar a construir un agente con LangGraph desde cero.

## Requisitos

- Python 3.11
- `uv` 0.10.5 o superior

## Instalacion

```bash
uv venv
uv sync
```

## Configuracion

Crea un archivo `.env` en la raiz del proyecto:

```env
OPENAI_API_KEY=tu_clave
```

## Ejecutar

```bash
uv run python main.py
```

## Estructura

```text
.
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```
