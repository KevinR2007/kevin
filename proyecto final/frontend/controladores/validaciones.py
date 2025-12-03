import re
from datetime import datetime

class Validaciones:

    # ===========================
    # VALIDACIONES GENERALES
    # ===========================

    def campo_vacio(self, valor):
        return valor is None or str(valor).strip() == ""

    def limpiar_fecha(self, fecha):
        """Limpia espacios y caracteres invisibles que Tkinter puede agregar"""
        if fecha is None:
            return ""
        return fecha.strip().replace("\u200b", "").replace("\xa0", "")

    def validar_fecha(self, fecha):
        """
        Acepta formatos:
        - YYYY-MM-DD
        - YYYY/MM/DD
        - ISO 8601: YYYY-MM-DDTHH:MM
        - ISO 8601: YYYY-MM-DDTHH:MM:SS
        """
        if self.campo_vacio(fecha):
            return False

        fecha = self.limpiar_fecha(fecha)

        formatos = [
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%Y-%m-%dT%H:%M",
            "%Y-%m-%dT%H:%M:%S",
        ]

        for f in formatos:
            try:
                datetime.strptime(fecha, f)
                return True
            except:
                pass

        return False

    def validar_texto(self, valor):
        """Solo letras y espacios"""
        return bool(re.match(r"^[A-Za-zÁÉÍÓÚÑáéíóúñ ]+$", valor))

    def validar_codigo(self, valor):
        """Letras, números, guiones y guion bajo"""
        return bool(re.match(r"^[A-Za-z0-9_\-]+$", valor))


    # ===========================
    # VALIDACIONES HERRAMIENTAS
    # ===========================

    def validar_herramienta(self, data):
        errores = []

        # Código
        if self.campo_vacio(data.get("codigo")):
            errores.append("El código no puede estar vacío.")
        elif not self.validar_codigo(data.get("codigo")):
            errores.append("El código solo puede contener letras, números y guiones.")

        # Nombre
        if self.campo_vacio(data.get("nombre")):
            errores.append("El nombre no puede estar vacío.")
        elif not self.validar_texto(data.get("nombre")):
            errores.append("El nombre solo puede contener letras.")

        # Categoría
        if self.campo_vacio(data.get("categoria")):
            errores.append("La categoría es obligatoria.")

        # Ubicación
        if self.campo_vacio(data.get("ubicacion")):
            errores.append("La ubicación es obligatoria.")

        # Estado
        if data.get("estado") not in ["Disponible", "Ocupada", "Dañada"]:
            errores.append("El estado no es válido.")

        return errores


    # ===========================
    # VALIDACIONES PRÉSTAMOS
    # ===========================

    def validar_prestamo(self, data):
        errores = []

        # Número
        if self.campo_vacio(data.get("numero")):
            errores.append("El número del préstamo no puede estar vacío.")
        elif not str(data["numero"]).isdigit():
            errores.append("El número del préstamo debe ser numérico.")

        # Código herramienta
        if self.campo_vacio(data.get("herramienta_codigo")):
            errores.append("Debe especificar la herramienta.")

        # Responsable
        if self.campo_vacio(data.get("responsable")):
            errores.append("El responsable es obligatorio.")
        elif not self.validar_texto(data["responsable"]):
            errores.append("El responsable solo puede contener letras.")

#(1)   
        # Fechas obligatorias 
        for campo in ["fecha_salida", "fecha_esperada", "fecha_devolucion"]:
            valor = data.get(campo)

            # Validar vacío
            if self.campo_vacio(valor):
                errores.append(f"La {campo.replace('_', ' ')} es obligatoria.")
                continue  # Importante para no seguir validando formato

            # Validar formato fecha
            if not self.validar_fecha(valor):
                errores.append(
                    f"La {campo.replace('_', ' ')} debe tener formato válido (ISO 8601 o YYYY-MM-DD)."
                )
                
        return errores
#(2)
"""
        # Fechas obligatorias (salida y esperada)
        for campo in ["fecha_salida", "fecha_esperada"]:
            valor = data.get(campo)
            if self.campo_vacio(valor):
                errores.append(f"La {campo.replace('_', ' ')} es obligatoria.")
            elif not self.validar_fecha(valor):
                errores.append(f"La {campo.replace('_', ' ')} debe tener formato válido (ISO 8601 o YYYY-MM-DD).")
"""
#(0)
"""
        # Fecha devolución opcional
        if data.get("fecha_devolucion"):
            if not self.validar_fecha(data["fecha_devolucion"]):
                errores.append("La fecha de devolución debe tener un formato válido.")

        return errores
"""

#la fecha de devluvion es obligatoria, si queremos que sea al reves, solo descomenrtar
#este bloque, el (0) y descomentar el bloque #(2) y comentartar el bloque #(1)

#(2)
"""
        # Fechas obligatorias (salida y esperada)
        for campo in ["fecha_salida", "fecha_esperada"]:
            valor = data.get(campo)
            if self.campo_vacio(valor):
                errores.append(f"La {campo.replace('_', ' ')} es obligatoria.")
            elif not self.validar_fecha(valor):
                errores.append(f"La {campo.replace('_', ' ')} debe tener formato válido (ISO 8601 o YYYY-MM-DD).")
"""