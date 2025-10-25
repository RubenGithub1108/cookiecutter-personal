from fastapi import FastAPI

app = FastAPI(title="{{ cookiecutter.project_title }}")

@app.get("/")
def root():
    return {"message": "API del modelo {{ cookiecutter.project_title }} funcionando correctamente."}
