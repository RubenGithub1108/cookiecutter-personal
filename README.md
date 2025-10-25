# cookiecutter-personal-template

**Autor:** Rubén Palma

## Descripción

Este repositorio contiene una plantilla de Cookiecutter para proyectos de ciencia de datos. Utiliza esta plantilla para crear proyectos estructurados con scripts para la preparación de datos, la creación de características, el entrenamiento de modelos y la visualización.

---

## Estructura del Proyecto

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
git clone https://github.com/tuusuario/cookiecutter-mlops-template.git
cd cookiecutter-mlops-template
```

2. Genera un nuevo proyecto:
```bash
cookiecutter .
```
