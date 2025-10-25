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
