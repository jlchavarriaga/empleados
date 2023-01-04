from fastapi import Query
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class Empleado(BaseModel):
    id: Optional[int] = None
    primer_apellido: str = Query(default=..., min_length=1, max_length=20, regex=r"^[A-Z ]{1,20}$")
    segundo_apellido: str = Field(default=...,min_length=1, max_length=20, regex=r"^[A-Z ]{1,20}$")
    primer_nombre : str = Field(default=...,min_length=1, max_length=20, regex=r"^[A-Z]{1,20}$")
    otros_nombres : str = Field(min_length=1, max_length=50, regex=r"^[A-Z ]{1,50}$")
    pais: str = Field(min_length=5, max_length=15)
    tipo_identificacion: str = Field(min_length=5, max_length=35)
    numero_identificacion: str = Query(min_length=5, max_length=20,regex=r"^[a-zA-Z0-9-]*$")
    area: str = Field(min_length=5, max_length=50)
    fecha_ingreso: date = None
    fecha_edicion:datetime = None
    fecha_hora_creacion:datetime = None


    class Config:
        schema_extra = {
            "example": {
                "primer_apellido": "PEREZ",
                "segundo_apellido": "ORTIZ",
                "primer_nombre": "JORGE",
                "otros_nombres": "LUIS",
                "pais": "Colombia",
                "tipo_identificacion": "Cédula de Ciudadanía",
                "numero_identificacion":"COL1047437474",
                "area" : "Financiera",
                "fecha_ingreso" : "2023-01-03"
            }
        }