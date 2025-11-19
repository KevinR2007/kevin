import requests

class Comunicacion:
    def __init__(self):
        self.data = []
        self.auto_id = 1

    def guardar(self, deporte, marca, diametro, fecha):
        """
        Guarda un balón en memoria basado en el modelo Balon.
        """
        registro = {
            "id": self.auto_id,
            "deporte": deporte,
            "marca": marca,
            "diametro": diametro,
            "fecha_de_creacion": fecha
        }
        self.data.append(registro)
        self.auto_id += 1
        return True

    def consultar(self, id_):
        try:
            id_int = int(id_)
        except:
            return {"error": "ID inválido"}

        for r in self.data:
            if r["id"] == id_int:
                return r
        return {"error": "No encontrado"}

    def consultar_todo(self):
        """
        Devuelve todos los registros.
        """
        return list(self.data)

    def eliminar(self, id_):
        try:
            id_int = int(id_)
        except:
            return False

        antes = len(self.data)
        self.data = [r for r in self.data if r["id"] != id_int]
        return len(self.data) < antes

    def actualizar(self, id_, deporte, marca, diametro, fecha):
        try:
            id_int = int(id_)
        except:
            return None

        for r in self.data:
            if r["id"] == id_int:
                r["deporte"] = deporte
                r["marca"] = marca
                r["diametro"] = diametro
                r["fecha_de_creacion"] = fecha
                return r

        return None
