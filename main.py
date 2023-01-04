from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from configuracion.database import engine, Base
from routers.empleado import empleado_router


app = FastAPI()
app.title = "Empleados"
app.version = "0.0.1"

app.include_router(empleado_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Prueba Tecnica, Cidenet S.A.S</h1>')