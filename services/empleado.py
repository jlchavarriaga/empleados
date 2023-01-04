import datetime
from http.client import HTTPException

from starlette import status

from models.empleado import Empleado as EmpleadoModel
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.empleado import Empleado
from datetime import datetime

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
        #validacion si ya existe
        si_existe = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.tipo_identificacion == new_empleado.tipo_identificacion,
            EmpleadoModel.numero_identificacion == new_empleado.numero_identificacion
        ).all()
        if (si_existe.__len__() > 0):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Este Usuario ya esta creado",
                                headers={"X-Error": "Este Usuario ya esta creado"})
        else:
            pass

        #validacion de la fecha
        hoy = datetime.now()
        fecha_actual = hoy.date()
        diferencia_dias = fecha_actual-new_empleado.fecha_ingreso
        if(new_empleado.fecha_ingreso  > fecha_actual ):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="la fecha es mayor a la fecha actual",
                                headers={"X-Error": "Fecha mayor a la actual"})
        elif(diferencia_dias.days >30):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="la fecha es menor en mas de un mes a la fecha actual",
                                headers={"X-Error": "Fecha menor en mas de un mes a la actual"})
        else:
            # validamos el correo electronico
            if (new_empleado.pais == "Colombia"):
                dominio = ".co"
            else:
                dominio = ".us"

            nombres_apellidos=new_empleado.primer_nombre.lower() + new_empleado.primer_apellido.replace(" ","").lower()
            correo_generado = nombres_apellidos + "@" + "cidenet.com" + dominio
            result = self.db.query(EmpleadoModel).filter(EmpleadoModel.correo_electronico == correo_generado).all()

            if (result.__len__() > 0):
                switch = True
                indicador = 0
                while switch == True:
                    indicador +=1
                    indicador_s=str(indicador)
                    correo_generado = nombres_apellidos + str(indicador) + "@" + "cidenet.com" + dominio
                    result = self.db.query(EmpleadoModel).filter(
                        EmpleadoModel.correo_electronico == correo_generado).all()
                    if (result.__len__() == 0):
                        new_empleado.correo_electronico = correo_generado
                        switch = False
            else:
                new_empleado.correo_electronico = correo_generado
            self.db.add(new_empleado)
            self.db.commit()
        return

    def get_correo_electronico(empleado: Empleado):
        pass

    def update_empleado(self, id: int, data: Empleado):
        empleado = self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).first()
        empleado.primer_apellido = data.primer_apellido
        empleado.segundo_apellido = data.segundo_apellido
        empleado.primer_nombre = data.primer_nombre
        empleado.otros_nombres = data.otros_nombres
        empleado.fecha_ingreso = data.fecha_ingreso
        empleado.pais = data.pais
        empleado.tipo_identificacion = data.tipo_identificacion
        empleado.numero_identificacion = data.numero_identificacion
        empleado.area = data.area
        empleado.fecha_edicion = datetime.now()

        #validacion si ya existe
        si_existe = self.db.query(EmpleadoModel).filter(
            EmpleadoModel.tipo_identificacion == empleado.tipo_identificacion,
            EmpleadoModel.numero_identificacion == empleado.numero_identificacion
        ).all()
        if (si_existe.__len__() > 0):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Este Usuario ya esta creado",
                                headers={"X-Error": "Este Usuario ya esta creado"})
        else:
            pass

        #validacion de la fecha
        hoy = datetime.now()
        fecha_actual = hoy.date()
        diferencia_dias = fecha_actual-empleado.fecha_ingreso
        if(empleado.fecha_ingreso  > fecha_actual ):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="la fecha es mayor a la fecha actual",
                                headers={"X-Error": "Fecha mayor a la actual"})
        elif(diferencia_dias.days >30):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="la fecha es menor en mas de un mes a la fecha actual",
                                headers={"X-Error": "Fecha menor en mas de un mes a la actual"})




        # validamos el correo electronico
        if (empleado.pais == "Colombia"):
            dominio = ".co"
        else:
            dominio = ".us"

        nombres_apellidos = empleado.primer_nombre.lower() + empleado.primer_apellido.replace(" ", "").lower()
        correo_generado = nombres_apellidos + "@" + "cidenet.com" + dominio
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.correo_electronico == correo_generado).all()

        if (result.__len__() > 0):
            switch = True
            indicador = 0
            while switch == True:
                indicador += 1
                indicador_s = str(indicador)
                correo_generado = nombres_apellidos + str(indicador) + "@" + "cidenet.com" + dominio
                result = self.db.query(EmpleadoModel).filter(
                    EmpleadoModel.correo_electronico == correo_generado).all()
                if (result.__len__() == 0):
                    empleado.correo_electronico = correo_generado
                    switch = False
        else:
            empleado.correo_electronico = correo_generado
        #empleado.correo_electronico = #get_correo_electronico(self,empleado)#data.correo_electronico
        self.db.commit()
        return

    def delete_empleado(self, id: int):
        self.db.query(EmpleadoModel).filter(EmpleadoModel.id == id).delete()
        self.db.commit()
        return
