class Comunicacion:
    def __init__(self):
        self.data = []      
        self.auto_id = 1     

    def guardar(self, modelo, marca, talla, fecha):
        zapato = {
            "id": self.auto_id,
            "modelo": modelo,
            "marca": marca,
            "talla": talla,
            "fecha": fecha
        }
        self.data.append(zapato)
        self.auto_id += 1
        print(f"Zapato guardado: {zapato}")
        return zapato

    def consultar(self, id_):
        try:
            id_int = int(id_)
        except ValueError:
            return {"error": "ID inválido"}

        for r in self.data:
            if r["id"] == id_int:
                return r
        return {"error": "No se encontró el zapato"}

    def consultarTodo(self):
        return self.data.copy()  

    def actualizar(self, id_, modelo, marca, talla, fecha):
        try:
            id_int = int(id_)
        except ValueError:
            return None

        for r in self.data:
            if r["id"] == id_int:
                r["modelo"] = modelo
                r["marca"] = marca
                r["talla"] = talla
                r["fecha"] = fecha
                return r
        return None

    def eliminar(self, id_):
        """Elimina un zapato por ID"""
        try:
            id_int = int(id_)
        except ValueError:
            return False
            
        for i, r in enumerate(self.data):
            if r["id"] == id_int:
                del self.data[i]
                print(f"Zapato con ID {id_int} eliminado")
                return True
        return False