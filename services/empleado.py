from models.empleado import Empleado as EmpleadoModel
from schemas.empleado import Empleado

class EmpleadoService():
    def __init__(self, db) -> None:
        self.db = db

    def get_empleados(self):
        result = self.db.query(EmpleadoModel).all()
        return result

    def get_empleado(self, id):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
        return result

    def get_empleados_by_identificacion(self, identificacion):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.numero_identificacion == identificacion).all()
        return result

    def create_empleado(self, empleado: Empleado):
        new_empleado = EmpleadoModel(**empleado.dict())
        self.db.add(new_empleado)
        self.db.commit()
        return

    def update_empleado(self, id: int, data: Empleado):
        empleado = self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
        empleado.primer_apellido = data.primer_apellido
        empleado.segundo_apellido = data.segundo_apellido
        empleado.primer_nombre = data.primer_nombre
        empleado.otros_nombres = data.otros_nombres
        empleado.pais = data.pais
        empleado.tipo_identificacion = data.tipo_identificacion
        empleado.numero_identificacion = data.numero_identificacion
        empleado.correo_electronico = data.correo_electronico
        self.db.commit()
        return

    def delete_empleado(self, id: int):
        self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).delete()
        self.db.commit()
        return
