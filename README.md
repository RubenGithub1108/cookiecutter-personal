# cookiecutter-personal-template

**Autor:** Rubén Palma

## Descripción

Este repositorio proporciona una plantilla de **Cookiecutter** para proyectos de ciencia de datos.
Está diseñada para ayudarte a crear proyectos estructurados que incluyan scripts para la **preparación de datos**, la **ingeniería de características**, el **entrenamiento de modelos** y la **visualización de resultados**.

---

## Estructura del Proyecto

Al generar un nuevo proyecto con esta plantilla, tu repositorio tendrá la siguiente estructura:

```
├── data/
│   ├── raw/              # Datos crudos originales
│   └── processed/        # Datos limpios y conjuntos de entrenamiento/prueba
├── models/
│   ├── production/       # Modelo final listo para despliegue
│   └── preprocessor.joblib # Objeto de preprocesamiento guardado
├── notebooks/            # Notebooks de Jupyter
├── src/
│   ├── api/              # Código de la API (FastAPI)
│   ├── data/             # Carga y limpieza de datos
│   ├── features/         # Ingeniería de características
│   └── models/           # Entrenamiento y evaluación de modelos
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias gestionadas con pip
└── environment.yml       # Dependencias gestionadas con conda
```

---

## Requerimientos

Para usar esta plantilla, asegúrate de tener instaladas las siguientes herramientas:

- **Anaconda** >= 4.x  
- **git** >= 2.x  
- **Cookiecutter (paquete de Python)** >= 2.6.0  

Cookiecutter puede instalarse usando `pip` o `conda`, dependiendo de cómo manejes tus entornos:

```bash
pip install cookiecutter
```

o 
```bash
conda install -c conda-forge cookiecutter
```

---

## Uso de la Plantilla

Sigue los pasos a continuación para crear un nuevo proyecto utilizando esta plantilla:


1. **Crear proyecto desde repositorio local**

   ```bash
   git clone https://github.com/RubenGithub1108/cookiecutter-personal.git
   cd cookiecutter-personal
   cookiecutter .
   ```

3. **Crear proyecto directamente desde GitHub**

   ```bash
   cookiecutter https://github.com/RubenGithub1108/cookiecutter-personal.git
   ```

Durante la creación, Cookiecutter te pedirá completar algunos campos como el nombre del proyecto, autor y versión de Python.
Los valores predeterminados se pueden modificar en el archivo cookiecutter.json.

---

## Licencia

MIT License © 2025 — **Rubén Palma**

---

## Créditos

Plantilla basada en buenas prácticas de MLOps inspiradas en:

* [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
* [Made with ML](https://madewithml.com/)
* [FastAPI Best Practices](https://fastapi.tiangolo.com/)



