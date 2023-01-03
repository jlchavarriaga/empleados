from configuracion.database import Base
from sqlalchemy import Column, Integer, String, Float

class Empleado(Base):

    __tablename__ = "empleados"

    id = Column(Integer, primary_key = True)
    primer_apellido = Column(String)
    segundo_apellido = Column(String)
    primer_nombre = Column(String)
    otros_nombres = Column(String)
    pais = Column(String)
    tipo_identificacion = Column(String)
    numero_identificacion = Column(String)
    correo_electronico = Column(String)
