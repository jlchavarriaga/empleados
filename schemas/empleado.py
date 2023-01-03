from pydantic import BaseModel, Field
from typing import Optional, List

class Empleado(BaseModel):
    id: Optional[int] = None
    primer_apellido: str = Field(default=..., min_length=1, max_length=20, pattern=r"^[a-zA-Z0-9-]*$")
    segundo_apellido: str = Field(default=...,min_length=1, max_length=20)
    primer_nombre : str = Field(default=...,min_length=1, max_length=20)
    otros_nombres : str = Field(min_length=1, max_length=50)
    pais: str = Field(min_length=5, max_length=15)
    tipo_identificacion: str = Field(min_length=5, max_length=35)
    numero_identificacion: str = Field(min_length=5, max_length=20)
    correo_electronico: str = Field(min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "primer_apellido": "PEREZ",
                "segundo_apellido": "ORTIZ",
                "primer_nombre": "JORGE",
                "otros_nombres": "LUIS",
                "pais": "COLOMBIA",
                "tipo_identificacion": "Cédula de Ciudadanía",
                "numero_identificacion":"COL1047437474",
                "correo_electronico" : "jorge.perez@cidenet.com.co "
            }
        }