# cookiecutter-personal-template

**Autor:** Rubén Palma

## Descripción

Este repositorio contiene una plantilla de Cookiecutter para proyectos de ciencia de datos. Utiliza esta plantilla para crear proyectos estructurados con scripts para la preparación de datos, la creación de características, el entrenamiento de modelos y la visualización.

---

## Estructura del Proyecto

Una vez que utilices esta plantilla para crear un proyecto, la estructura de tu repositorio será la siguiente:

```
├── data/
│   ├── raw/              # Datos crudos originales
│   └── processed/        # Datos limpios y conjuntos de train/test
├── models/
│   ├── production/       # Modelo final listo para despliegue
│   └── preprocessor.joblib
├── notebooks/            # Notebooks de Jupyter
├── src/
│   ├── api/              # Código FastAPI
│   ├── data/             # Limpieza y carga de datos
│   ├── features/         # Ingeniería de características
│   └── models/           # Entrenamiento de modelos
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias pip
└── environment.yml       # Dependencias conda
```

## Cómo usar la plantilla

1. Clona o descomprime la plantilla:

```bash
git clone https://github.com/RubenGithub1108/cookiecutter-personal.git
cd cookiecutter-personal
```

2. Genera un nuevo proyecto:
```bash
cookiecutter .
```
