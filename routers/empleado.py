from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from configuracion.database import Session
from models.empleado import Empleado as EmpleadoModel
from fastapi.encoders import jsonable_encoder
from services.empleado import EmpleadoService
from schemas.empleado import Empleado

empleado_router = APIRouter()

@empleado_router.get('/empleados', tags=['empleados'], response_model=List[Empleado], status_code=200)
def get_empleados() -> List[Empleado]:
    db = Session()
    result = EmpleadoService(db).get_empleados()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.get('/empleados/{id}', tags=['empleados'], response_model=Empleado)
def get_empleado(id: int = Path(ge=1, le=2000)) -> Empleado:
    db = Session()
    result = EmpleadoService(db).get_empleado(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.get('/empleados/', tags=['empleados'], response_model=List[Empleado])
def get_empleados_by_identificacion(identificacion: str = Query(min_length=5, max_length=20)) -> List[Empleado]:
    db = Session()
    result = EmpleadoService(db).get_empleados_by_identificacion(identificacion)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.post('/empleados', tags=['empleados'], response_model=dict, status_code=201)
def create_empleado(empleado: Empleado) -> dict:
    db = Session()
    EmpleadoService(db).create_empleado(empleado)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el empleado"})


@empleado_router.put('/empleados/{id}', tags=['empleados'], response_model=dict, status_code=200)
def update_empleado(id: int, empleado: Empleado) -> dict:
    db = Session()
    result = EmpleadoService(db).get_empleado(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})

    EmpleadoService(db).update_empleado(id, empleado)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el empleado"})


@empleado_router.delete('/empleados/{id}', tags=['empleados'], response_model=dict, status_code=200)
def delete_empleado(id: int) -> dict:
    db = Session()
    result: EmpleadoModel = db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    EmpleadoService(db).delete_empleado(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el empleado"})