from configuracion.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean,Date, DateTime
from datetime import datetime


class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(Integer, primary_key = True,index=True)
    primer_apellido = Column(String,nullable=False)
    segundo_apellido = Column(String)
    primer_nombre = Column(String,nullable=False)
    otros_nombres = Column(String,nullable=True)
    pais = Column(String)
    tipo_identificacion = Column(String,nullable=False)
    numero_identificacion = Column(String,unique=True,nullable=False)
    correo_electronico = Column(String, unique=True,nullable=False)
    area =Column(String,nullable=False)
    fecha_ingreso= Column(Date)
    fecha_edicion= Column(DateTime,default=datetime.now,onupdate=datetime.now)
    fecha_hora_creacion= Column(DateTime, default=datetime.now) #Excluir de la edicion
    estado = Column(Boolean, default=True)#Excluir de la edicion

