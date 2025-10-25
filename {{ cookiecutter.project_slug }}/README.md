# {{ cookiecutter.project_title }}

**Autor:** {{ cookiecutter.project_author_name }}

## Descripción

{{ cookiecutter.project_description }}

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

## Requirements
Python {{ cookiecutter.python_version }}

## Licencia
{{ cookiecutter.open_source_license }}
